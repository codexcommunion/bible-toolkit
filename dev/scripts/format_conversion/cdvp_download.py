import os
import json
import requests
from pathlib import Path
from bs4 import BeautifulSoup

TARGET_DIR = os.path.join("assets", "cpdv")

def download(address):
    """Download a file from the given URL and save it with the last segment of the URL as filename."""
    filename = address.split("/")[-1]
    try:
        response = requests.get(address, stream=True)
        response.raise_for_status()
        
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    except requests.RequestException as e:
        print(f"Error downloading {address}: {e}")

def to_json(book_name, bible_map):
    """Convert the downloaded HTML content of a book to JSON format."""
    url = to_url(book_name)
    download(url)
    
    file_html_path = Path(f"{book_name}.htm")
    if not file_html_path.exists():
        print(f"File {file_html_path} not found.")
        return
    
    try:
        with file_html_path.open("r", encoding="windows-1252", errors="replace") as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading {file_html_path}: {e}")
        return
    
    # Parse the HTML to extract text content
    soup = BeautifulSoup(content, "html.parser")
    book = {}
    
    for br in soup.find_all("br"):
        br.replace_with("\n")  # Convert <br> tags to newlines for easier processing
    
    text = soup.get_text("\n", strip=True)
    lines = text.split("\n")
    
    for line in lines:
        try:
            if line.startswith("{") and "}" in line:
                end_meta = line.index("}")
                meta = line[:end_meta+1]
                content_text = line[end_meta+1:].strip()
                
                chapter, verse = meta[1:-1].split(":")
                
                if chapter not in book:
                    book[chapter] = {}
                
                book[chapter][verse] = content_text
        except Exception as e:
            print(f"Error processing line: {line}\n{e}")
    
    if bible_map is not None and "_" in book_name:
        bible_map[book_name.split("_")[1]] = book.copy()
    
    book["charset"] = "UTF-8"
    
    try:
        with open(f"{TARGET_DIR}/{book_name}.json", "w", encoding="utf-8") as json_file:
            json.dump(book, json_file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error writing JSON file for {book_name}: {e}")
    
    try:
        file_html_path.unlink()  # Delete the file after processing
    except Exception as e:
        print(f"Error deleting file {file_html_path}: {e}")

def to_url(book_name):
    """Generate the URL for downloading the book."""
    host = "https://www.sacredbible.org/catholic/"
    return f"{host}{book_name}.htm"

if __name__ == "__main__":
    print("Encoding Bible-CPDV to JSON")
    
    bible_map = {"charset": "UTF-8"}
    books = [
        "OT-01_Genesis", "OT-02_Exodus", "OT-03_Leviticus", "OT-04_Numbers", "OT-05_Deuteronomy", 
        "OT-06_Joshua", "OT-07_Judges", "OT-08_Ruth", "OT-09_1-Samuel", "OT-10_2-Samuel", 
        "OT-11_1-Kings", "OT-12_2-Kings", "OT-13_1-Chronicles", "OT-14_2-Chronicles", "OT-15_Ezra", 
        "OT-16_Nehemiah", "OT-17_Tobit", "OT-18_Judith", "OT-19_Esther", "OT-20_Job", "OT-21_Psalms", 
        "OT-22_Proverbs", "OT-23_Ecclesiastes", "OT-24_Song2", "OT-25_Wisdom", "OT-26_Sirach", 
        "OT-27_Isaiah", "OT-28_Jeremiah", "OT-29_Lamentations", "OT-30_Baruch", "OT-31_Ezekiel", 
        "OT-32_Daniel", "OT-33_Hosea", "OT-34_Joel", "OT-35_Amos", "OT-36_Obadiah", "OT-37_Jonah", 
        "OT-38_Micah", "OT-39_Nahum", "OT-40_Habakkuk", "OT-41_Zephaniah", "OT-42_Haggai", "OT-43_Zechariah", "OT-44_Malachi", 
        "OT-45_1-Maccabees", "OT-46_2-Maccabees", "NT-01_Matthew", "NT-02_Mark", "NT-03_Luke", "NT-04_John", 
        "NT-05_Acts", "NT-06_Romans", "NT-07_1-Corinthians", "NT-08_2-Corinthians", "NT-09_Galatians", 
        "NT-10_Ephesians", "NT-11_Philippians", "NT-12_Colossians", "NT-13_1-Thessalonians", "NT-14_2-Thessalonians", 
        "NT-15_1-Timothy", "NT-16_2-Timothy", "NT-17_Titus", "NT-18_Philemon", "NT-19_Hebrews", "NT-20_James", 
        "NT-21_1-Peter", "NT-22_2-Peter", "NT-23_1-John", "NT-24_2-John", "NT-25_3-John", "NT-26_Jude", "NT-27_Revelation"
    ]
    
    import time
    start_time = time.time()
    
    for book in books:
        to_json(book, bible_map)
    
    end_time = time.time()
    print(f"Finished encoding CPDV Bible to JSON - {int((end_time - start_time) * 1000)}ms")
    
    try:
        with open(f"{TARGET_DIR}/cpdv.json", "w", encoding="utf-8") as json_file:
            json.dump(bible_map, json_file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error writing entire Bible JSON file: {e}")