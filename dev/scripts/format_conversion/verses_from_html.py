import os
import re
import json
import yaml
import argparse
import datetime
from bs4 import BeautifulSoup

def extract_usfm_code(filename):
    match = re.match(r"([1-3]?[A-Z]{2,3})(\d+)?", filename)  # Allow optional chapter numbers
    if match:
        return match.group(1)
    print(f"Skipping {filename}: Invalid filename format")
    return None  # Skip invalid filenames

def extract_verse_text(verse_tag):
    """Extracts verse text, handling cases where text is split across multiple spans, including non-integer verse numbering."""
    text_parts = []
    current_element = verse_tag.next_sibling
    
    while current_element:
        if current_element.name == "span" and "verse" in current_element.get("class", []):
            break  # Stop at the next verse tag
        
        if isinstance(current_element, str):
            text_parts.append(current_element.strip())
        elif current_element.name == "span":
            text_parts.append(current_element.get_text(strip=True))
        
        current_element = current_element.next_sibling
    
    return " ".join(filter(None, text_parts))

def parse_html_to_json_yaml(html_file, output_directory, language_code, index_list, book_set, verse_count):
    with open(html_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    # Extract USFM book code from filename
    base_name = os.path.splitext(os.path.basename(html_file))[0]
    usfm_code = extract_usfm_code(base_name)
    if usfm_code is None:
        return  # Skip processing if filename is invalid
    
    # Extract book name from the <title> tag
    title_tag = soup.title
    title = title_tag.text.strip() if title_tag else "Unknown"
    
    # Extract chapter number from the <div class_='chapterlabel'> tag
    chapter = soup.find("div", class_="chapterlabel")
    chapter_number = chapter.text.strip() if chapter else "Unknown"
    
    # Ensure chapter number is a valid integer
    if not chapter_number.isdigit():
        print(f"Skipping {html_file}: Invalid chapter number: {chapter_number}")
        return  # Skip invalid chapters
    chapter_number = int(chapter_number)
    
    # Extract verses, preserving non-integer verse numbering (e.g., 1a, 1b)
    verses = []
    for verse_tag in soup.find_all("span", class_="verse"):
        verse_text_content = verse_tag.get_text(strip=True).replace("\xa0", "")  # Normalize & remove non-breaking spaces
        
        # Preserve verse numbering exactly as it appears in the HTML
        verse_number = verse_text_content if verse_text_content else "Unknown"
        
        verse_text = extract_verse_text(verse_tag)
        
        verses.append({
            "book": title,
            "usfm_code": usfm_code,
            "chapter": chapter_number,
            "verse": verse_number,  # Now correctly extracted from tag content and normalized
            "text": verse_text,
            "iso-639-2_language_code": language_code
        })
    
    # If no valid verses were found, skip file
    if not verses:
        print(f"Skipping {html_file}: No valid verses found")
        return
    
    # Define output file paths using USFMCode_ChapterNumber format
    os.makedirs(output_directory, exist_ok=True)
    json_filename = f"{usfm_code}{chapter_number:02}.json"
    yaml_filename = f"{usfm_code}{chapter_number:02}.yaml"
    json_file = os.path.join(output_directory, json_filename)
    yaml_file = os.path.join(output_directory, yaml_filename)
    
    # Save JSON output
    with open(json_file, "w", encoding="utf-8") as jf:
        json.dump(verses, jf, ensure_ascii=False, indent=4)
    
    # Save YAML output
    with open(yaml_file, "w", encoding="utf-8") as yf:
        yaml.dump(verses, yf, allow_unicode=True, default_flow_style=False)
    
    # Add to index and book set
    index_list.append({
        "book_usfm_code": usfm_code,
        "chapter_number": str(chapter_number),
        "json_filename": json_filename
    })
    book_set.add(usfm_code)
    verse_count.append(len(verses))
    
    print(f"Conversion complete! JSON: {json_file}, YAML: {yaml_file}")

# Main execution block
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Default directories
    default_input_dir = os.path.join(script_dir, "..", "..", "..", "assets", "septaugint", "brenton", "greek_koine_html")
    default_output_dir = os.path.join(script_dir, "..", "..", "..", "data", "septuagint", "brenton", "greek_koine")
    default_language_code = "grc"
  
    # Default directories
    # default_input_dir = os.path.join(script_dir, "..", "..", "..", "assets", "septaugint", "brenton", "english_html")
    # default_output_dir = os.path.join(script_dir, "..", "..", "..", "data", "septuagint", "brenton", "english")
    # default_language_code = "eng"
    
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Convert Septuagint HTML to JSON/YAML")
    parser.add_argument("--input", type=str, default=default_input_dir)
    parser.add_argument("--output", type=str, default=default_output_dir)
    parser.add_argument("--language", type=str, default=default_language_code)
    
    args = parser.parse_args()
    input_directory = args.input
    output_directory = args.output
    language_code = args.language
    
    index_list = []
    book_set = set()
    verse_count = []
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".htm") or filename.endswith(".html"):
            try:
                parse_html_to_json_yaml(os.path.join(input_directory, filename), output_directory, language_code, index_list, book_set, verse_count)
            except Exception as e:
                print(f"Skipping {filename}: {e}")
    
    print("Index and metadata files created successfully!")
