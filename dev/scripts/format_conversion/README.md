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

## Usage

### Running the Script

```sh
python convert_septuagint_html.py
```

By default, the script will:
- Read `.htm`/`.html` files from `./input/`
- Convert them into structured JSON and YAML files
- Save them in `./output/`

### Customizing Input & Output Directories

Modify these lines in the script to specify different locations:
```python
input_directory = "./your_input_directory"
output_directory = "./your_output_directory"
```

## Output Format
Each output file is a list of verses in the following format:
```json
[
  {
    "book": "ΠΑΡΑΛΕΙΠΟΜΕΝΩΝ Α",  
    "usfm_code": "1CH",
    "chapter": 1,
    "verse": 1,
    "text": "ἈΔΑΜ, Σὴθ, Ἐνὼς, ...",
    "iso-639-2_language_code": "grc"
  },
  ...
]
```

## Language Code & USFM Code References
- **ISO 639-2 Language Codes (Ancient Greek: `grc`)**: [Library of Congress ISO-639-2 Code List](https://www.loc.gov/standards/iso639-2/php/code_list.php)
- **USFM Book Codes Reference**: [USFM Documentation for Books](https://ubsicap.github.io/usfm/identification/books.html)

## Error Handling
- The script **raises an error** if a file has **invalid chapter or verse numbers**.
- Files that don’t match the expected format are **skipped** with a warning.

## License
This script is released under the **MIT License**.

