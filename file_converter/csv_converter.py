import pandas as pd
import json

class CSVConverter:

    @staticmethod
    def csv_to_json(csv_filepath, json_filepath, orient="records", lines=True):
        """
        Converts a CSV file to a JSON file.
        
        Parameters:
            csv_filepath (str): Path to the input CSV file.
            json_filepath (str): Path to the output JSON file.
            orient (str): Indication of expected JSON string format.
            lines (bool): Whether to write JSON as line delimited.
        """
        try:
            # Read CSV file
            data = pd.read_csv(csv_filepath)

            # Save as JSON file
            data.to_json(json_filepath, orient=orient, lines=lines)

            print(f"File converted successfully and saved at {json_filepath}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def csv_to_txt(csv_filepath, txt_filepath, sep="\t"):
        """
        Converts a CSV file to a TXT file.
        
        Parameters:
            csv_filepath (str): Path to the input CSV file.
            txt_filepath (str): Path to the output TXT file.
            sep (str): String of length 1. Field delimiter for the output file.
        """
        try:
            # Read CSV file
            data = pd.read_csv(csv_filepath)
            
            # Save as TXT file
            data.to_csv(txt_filepath, sep=sep, index=False)
            
            print(f"File converted successfully and saved at {txt_filepath}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def json_to_csv(json_filepath, csv_filepath):
        """
        Converts a JSON file to a CSV file.

        Parameters:
            json_filepath (str): Path to the input JSON file.
            csv_filepath (str): Path to the output CSV file.
        """
        try:
            # Read JSON file
            data = pd.read_json(json_filepath, lines=True)

            # Save as CSV file
            data.to_csv(csv_filepath, index=False)

            print(f"File converted successfully and saved at {csv_filepath}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
    @staticmethod
    def txt_to_csv(txt_filepath, csv_filepath, sep="\t"):
        """
        Converts a TXT file to a CSV file.
        
        Parameters:
            txt_filepath (str): Path to the input TXT file.
            csv_filepath (str): Path to the output CSV file.
            sep (str): String of length 1. Field delimiter for the input file.
        """
        try:
            # Read TXT file
            data = pd.read_csv(txt_filepath, sep=sep)

            # Save as CSV file
            data.to_csv(csv_filepath, index=False)
            
            print(f"File converted successfully and saved at {csv_filepath}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

# Example usage:

# Convert TXT to CSV
# CSVConverter.txt_to_csv("input_file.txt", "output_file.csv")