import pandas as pd
import json

class JSONConverter:
    
    @staticmethod
    def json_to_txt(json_filepath, txt_filepath, sep="\t"):
        """
        Converts a JSON file to a TXT file.
        
        Parameters:
            json_filepath (str): Path to the input JSON file.
            txt_filepath (str): Path to the output TXT file.
            sep (str): String of length 1. Field delimiter for the output file.
        """
        try:
            # Read JSON file
            data = pd.read_json(json_filepath, lines=True)
            
            # Save as TXT file
            data.to_csv(txt_filepath, sep=sep, index=False, header=False)
            
            print(f"File converted successfully and saved at {txt_filepath}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    

    @staticmethod
    def txt_to_json(txt_filepath, json_filepath, sep="\t", orient="records", lines=True):
        """
        Converts a TXT file to a JSON file.
        
        Parameters:
            txt_filepath (str): Path to the input TXT file.
            json_filepath (str): Path to the output JSON file.
            sep (str): String of length 1. Field delimiter for the input file.
            orient (str): Indication of expected JSON string format.
            lines (bool): Whether to write JSON as line delimited.
        """
        try:
            # Read TXT file
            data = pd.read_csv(txt_filepath, sep=sep)

            # Save as JSON file
            data.to_json(json_filepath, orient=orient, lines=lines)

            print(f"File converted successfully and saved at {json_filepath}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
    def json_to_csv(json_filepath, csv_filepath):
        """
        Converts a JSON file to a CSV file.

        Parameters:
            json_filepath (str): Path to the input JSON file.
            csv_filepath (str): Path to the output CSV file.
        """
        try:
            # Load JSON data
            data = pd.read_json(json_filepath, lines=True)

            # Save as a CSV file
            data.to_csv(csv_filepath, index=False)
            
            print(f"File converted successfully and saved at {csv_filepath}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

# example usage:
# JSONConverter.json_to_csv("input_file.json", "output_file.csv")
