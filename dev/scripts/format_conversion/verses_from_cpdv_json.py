import os
import json
import yaml
import argparse
from collections import defaultdict

def load_usfm_codes(usfm_json_path, usfm_yaml_path):
    if usfm_json_path and os.path.exists(usfm_json_path):
        with open(usfm_json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif usfm_yaml_path and os.path.exists(usfm_yaml_path):
        with open(usfm_yaml_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        raise FileNotFoundError("Neither USFM JSON nor YAML file found.")

def normalize_book_name(book):
    """ Normalize book names to match USFM codes """
    book = book.replace("-", " ")
    book_replacements = {
        "Esther": "Esther Greek",  # CPDV uses the longer Septuagint version
        "Song2": "Song of Songs",  # Map 'Song2' to 'Song of Songs' (SNG)
        "Wisdom":"Wisdom of Solomon",
        "Daniel": "Daniel Greek"
    }
    return book_replacements.get(book, book)

def clean_text(text):
    """ Fix character encoding issues """
    try:
        return text.encode("latin1").decode("utf-8")
    except UnicodeEncodeError:
        return text  # If no encoding issue, return as is

def load_json_safely(json_file_path):
    """ Read JSON while handling encoding issues """
    with open(json_file_path, "r", encoding="latin1") as file:
        raw_text = file.read()
    return json.loads(raw_text.encode("utf-8").decode("utf-8"))

def process_bible_file(json_file_path, output_directory, usfm_codes, language_code):
    bible_data = load_json_safely(json_file_path)
    
    index_json_data = []
    index_yaml_data = []
    meta_data = {
        "scripture_name": "Catholic Public Domain Version",
        "abbreviation": "CPDV",
        "language": language_code,
        "description": "The Catholic Public Domain Version (CPDV) is a modern, public-domain translation of the Bible.",
        "structure": {
            "type": "structured_verses",
            "format": ["json", "yaml"],
            "index_file": "_index.json"
        },
        "creation_date": "2025-03-16",
        "generator": "CodexCommunion",
        "notes": "This dataset is structured to allow efficient retrieval of individual verses.",
        "stats": {
            "book_count": 0,
            "chapter_count": 0,
            "verse_count": 0
        }
    }
    
    total_chapters = 0
    total_verses = 0
    
    for book, chapters in bible_data.items():
        if book == "charset":
            continue  # Skip metadata
        
        normalized_book = normalize_book_name(book)
        usfm_code = next((code for code, details in usfm_codes.items() if details["name"] == normalized_book), None)
        
        if not usfm_code:
            raise ValueError(f"Book name '{book}' not found in USFM codes.")
        
        chapter_count = len(chapters)
        meta_data["stats"]["book_count"] += 1
        meta_data["stats"]["chapter_count"] += chapter_count
        
        verse_counter = 0  # Counter for handling non-integer verse numbers
        for chapter_key, verses in chapters.items():
            chapter_num = chapter_key if chapter_key.isdigit() else chapter_key  # Keep as string if it's not a number
            json_filename = f"{usfm_code}{chapter_num}.json"
            yaml_filename = f"{usfm_code}{chapter_num}.yaml"
            
            index_json_data.append({"book_usfm_code": usfm_code, "chapter_number": chapter_num, "json_filename": json_filename})
            index_yaml_data.append({"book_usfm_code": usfm_code, "chapter_number": chapter_num, "yaml_filename": yaml_filename})
            
            chapter_data = []
            for verse_key, verse_text in verses.items():
                verse_counter += 1
                verse_number = verse_key if verse_key.isdigit() else f"1{chr(96 + verse_counter)}"  # Convert to 1a, 1b, etc.
                
                verse_data = {
                    "book_title": book,
                    "book_usfm_code": usfm_code,
                    "chapter_number": chapter_num,
                    "verse_number": verse_number,
                    "verse_text": clean_text(verse_text),
                    "iso-639-2_language_code": language_code,
                }
                chapter_data.append(verse_data)
                total_verses += 1
            
            with open(os.path.join(output_directory, json_filename), "w", encoding="utf-8") as json_file:
                json.dump(chapter_data, json_file, indent=4, ensure_ascii=False)
            
            with open(os.path.join(output_directory, yaml_filename), "w", encoding="utf-8") as yaml_file:
                yaml.dump(chapter_data, yaml_file, allow_unicode=True)
    
    meta_data["stats"]["verse_count"] = total_verses
    
    # Save index files
    with open(os.path.join(output_directory, "_index.json"), "w", encoding="utf-8") as index_file:
        json.dump(index_json_data, index_file, indent=4, ensure_ascii=False)
    
    with open(os.path.join(output_directory, "_index.yaml"), "w", encoding="utf-8") as index_file:
        yaml.dump(index_yaml_data, index_file, allow_unicode=True)
    
    # Save meta files
    with open(os.path.join(output_directory, "_meta.json"), "w", encoding="utf-8") as meta_file:
        json.dump(meta_data, meta_file, indent=4, ensure_ascii=False)
    
    with open(os.path.join(output_directory, "_meta.yaml"), "w", encoding="utf-8") as meta_file:
        yaml.dump(meta_data, meta_file, allow_unicode=True)

if __name__ == "__main__":
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Default directories and language
    default_input_file = os.path.join("assets", "cpdv", "cpdv.json")
    default_output_dir = os.path.join("data", "cpdv")
    default_usfm_json = os.path.join(script_dir, "usfm_codes.json")
    default_usfm_yaml = os.path.join(script_dir, "usfm_codes.yaml")
    default_language_code = "eng"  # English

    # Argument parser setup
    parser = argparse.ArgumentParser(description="Process CPDV Bible JSON into structured JSON/YAML")
    parser.add_argument("--input", type=str, default=default_input_file, help="Path to the input JSON file")
    parser.add_argument("--output", type=str, default=default_output_dir, help="Path to the output directory")
    parser.add_argument("--usfm_json", type=str, default=default_usfm_json, help="Path to the USFM codes JSON file")
    parser.add_argument("--usfm_yaml", type=str, default=default_usfm_yaml, help="Path to the USFM codes YAML file")
    parser.add_argument("--language", type=str, default=default_language_code, help="ISO 639-2 language code for the text")
    
    args = parser.parse_args()
    
    usfm_codes = load_usfm_codes(args.usfm_json, args.usfm_yaml)
    process_bible_file(args.input, args.output, usfm_codes, args.language)
    print("Processing complete. JSON, YAML files, index, and meta files are saved in the output directory.")
