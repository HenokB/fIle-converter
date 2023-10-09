import pandas as pd

class FileConverter:

    @staticmethod
    def json_to_txt(json_filepath, txt_filepath, sep="\t"):
        try:
            data = pd.read_json(json_filepath, lines=True)
            data.to_csv(txt_filepath, sep=sep, index=False, header=False)
            print(f"File converted successfully and saved at {txt_filepath}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def txt_to_json(txt_filepath, json_filepath, sep="\t", orient="records", lines=True):
        try:
            data = pd.read_csv(txt_filepath, sep=sep)
            data.to_json(json_filepath, orient=orient, lines=lines)
            print(f"File converted successfully and saved at {json_filepath}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def csv_to_json(csv_filepath, json_filepath, orient="records", lines=True):
        try:
            data = pd.read_csv(csv_filepath)
            data.to_json(json_filepath, orient=orient, lines=lines)
            print(f"File converted successfully and saved at {json_filepath}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def json_to_csv(json_filepath, csv_filepath):
        try:
            data = pd.read_json(json_filepath, lines=True)
            data.to_csv(csv_filepath, index=False)
            print(f"File converted successfully and saved at {csv_filepath}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def csv_to_txt(csv_filepath, txt_filepath, sep="\t"):
        try:
            data = pd.read_csv(csv_filepath)
            data.to_csv(txt_filepath, sep=sep, index=False)
            print(f"File converted successfully and saved at {txt_filepath}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def txt_to_csv(txt_filepath, csv_filepath, sep="\t"):
        try:
            data = pd.read_csv(txt_filepath, sep=sep)
            data.to_csv(csv_filepath, index=False)
            print(f"File converted successfully and saved at {csv_filepath}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
