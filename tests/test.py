import pytest
import pandas as pd
from file_converter import FileConverter

# File paths used for testing
CSV_FILE = "tests/test_files/example.csv"
JSON_FILE = "tests/test_files/example.json"
TXT_FILE = "tests/test_files/example.txt"

# Sample DataFrame for testing
SAMPLE_DF = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [30, 25]
})

@pytest.fixture
def create_test_files():
    SAMPLE_DF.to_csv(CSV_FILE, index=False)
    SAMPLE_DF.to_json(JSON_FILE, orient="records", lines=True)
    SAMPLE_DF.to_csv(TXT_FILE, sep="\t", index=False)

def test_csv_to_json(create_test_files):
    output_json = "tests/test_files/output.json"
    FileConverter.csv_to_json(CSV_FILE, output_json)
    
     
    converted_data = pd.read_json(output_json, lines=True)
    pd.testing.assert_frame_equal(converted_data, SAMPLE_DF)

def test_json_to_csv(create_test_files):
    output_csv = "tests/test_files/output.csv"
    FileConverter.json_to_csv(JSON_FILE, output_csv)
    
     
    converted_data = pd.read_csv(output_csv)
    pd.testing.assert_frame_equal(converted_data, SAMPLE_DF)

def test_csv_to_txt(create_test_files):
    output_txt = "tests/test_files/output.txt"
    FileConverter.csv_to_txt(CSV_FILE, output_txt)
    
     
    converted_data = pd.read_csv(output_txt, sep="\t")
    pd.testing.assert_frame_equal(converted_data, SAMPLE_DF)

def test_txt_to_csv(create_test_files):
    output_csv = "tests/test_files/output_from_txt.csv"
    FileConverter.txt_to_csv(TXT_FILE, output_csv)
    
     
    converted_data = pd.read_csv(output_csv)
    pd.testing.assert_frame_equal(converted_data, SAMPLE_DF)

def test_txt_to_json(create_test_files):
    output_json = "tests/test_files/output_from_txt.json"
    FileConverter.txt_to_json(TXT_FILE, output_json)
    
     
    converted_data = pd.read_json(output_json, lines=True)
    pd.testing.assert_frame_equal(converted_data, SAMPLE_DF)
