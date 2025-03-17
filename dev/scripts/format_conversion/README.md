# Convert Septuagint HTML to JSON/YAML

This script processes **Septuagint HTML files** and extracts structured verse data into **JSON** and **YAML** formats.

## Installation

### Installing Python
If you do not have Python installed, download and install it from the official sources:
- **Windows/macOS/Linux:** [Python Downloads](https://www.python.org/downloads/)

Ensure you have **Python 3.7+** installed before proceeding.

### Setting Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

1. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - **PowerShell:**
     ```powershell
     venv\Scripts\Activate.ps1
     ```

     or if execution is typically disabled on your system

     ```powershell
     powershell -ExecutionPolicy Bypass -File .\venv\Scripts\Activate.ps1
     ```
   - **Mac/Linux:**
     ```sh
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Script

### Default Behavior

By default, the script:

- Reads `.htm`/`.html` files from the **Greek Koine Septuagint source** located in:
  ```
  ../../../assets/septuagint/brenton/greek_koine_html
  ```
- Converts them into structured **JSON and YAML** files.
- Saves the output in:
  ```
  ../../../data/septuagint/brenton/greek_koine
  ```
- Uses **"grc"** (Ancient Greek, Koine) as the language code.

### Basic Usage

To run the script with default settings:

```sh
python verses_from_html.py
```

### Customizing Input and Output

You can specify a custom input directory, output directory, and language code using command-line arguments.

```sh
python verses_from_html.py --input /path/to/input --output /path/to/output --language eng
```

**Example for English Texts:**
```sh
python verses_from_html.py --input ../../../assets/septuagint/brenton/english_html --output ../../../data/septuagint/brenton/english --language eng
```

### Error Handling

- If the input filenames are not in the expected format, they will be skipped.
- If the chapter number is invalid, the file will be ignored.
- If no valid verses are found, the file will be skipped.
- Any unexpected errors will be reported, and processing will continue for other files.

### Notes

- This script is **tested only on Greek and English HTML files** formatted similarly. Other languages may not be compatible.
- The extracted output is formatted using **USFM** book codes and structured with:
  - `book_title` (Extracted from HTML title)
  - `book_usfm_code` (Derived from the filename)
  - `chapter_number`
  - `verse_number`
  - `verse_text`
  - `iso-639-2_language_code`




## Language Code & USFM Code References
- **ISO 639-2 Language Codes (Ancient Greek: `grc`)**: [Library of Congress ISO-639-2 Code List](https://www.loc.gov/standards/iso639-2/php/code_list.php)
- **USFM Book Codes Reference**: [USFM Documentation for Books](https://ubsicap.github.io/usfm/identification/books.html)


## License
This script is released under the **MIT License**.

