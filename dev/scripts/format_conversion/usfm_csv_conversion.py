import csv
import json
import os
import re
import yaml

# File paths
base_path = os.path.join("dev", "scripts", "format_conversion")
csv_file =  os.path.join(base_path, "usfm_codes_eng.csv")
json_file = os.path.join(base_path, "usfm_codes.json")
yaml_file = os.path.join(base_path, "usfm_codes.yaml")

def clean_quotes(value):
    """Remove extraneous quotes from a string."""
    return re.sub(r'^"|"$', '', value.strip())

def convert_csv_to_json_yaml(csv_filepath, json_filepath, yaml_filepath):
    data = {}
    
    with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) < 4:
                continue  # Skip malformed rows
            identifier = clean_quotes(row[1])
            english_name = clean_quotes(row[2])
            notes = clean_quotes(row[3]) if len(row) > 3 else ""
            
            data[identifier] = {
                "code": identifier,
                "name": english_name,
                "notes": notes
            }
    
    # Save JSON
    with open(json_filepath, "w", encoding="utf-8") as jsonf:
        json.dump(data, jsonf, indent=4, ensure_ascii=False)
    
    # Save YAML
    with open(yaml_filepath, "w", encoding="utf-8") as yamlf:
        yaml.dump(data, yamlf, allow_unicode=True)
    
    print("Conversion complete: JSON and YAML files created.")

# Run the conversion
convert_csv_to_json_yaml(csv_file, json_file, yaml_file)