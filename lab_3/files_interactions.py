
import json


def write_txt(file_path: str, data: str) -> None:
    """function, which can write data to .txt file

    Args:
        file_path (str): path to file, which we need to fill
        data (str): what we need to write in file
    """
    try:
        with open(file_path, 'w', encoding="UTF-8") as file:
            file.write(data)
    except Exception as e:
       print("Error occured:", e)


def read_txt(file_path: str) -> str:
    """function, which can read data from .txt file

    Args:
        file_path (str): path to file with data

    Returns:
        str: what the file contains
    """
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            return file.read().replace("\n", " \n")
    except Exception as e:
       print("Error occured:", e)


def read_json(file_path: str) -> dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print("Error occured:", e)


def write_json(file_path: str, data: dict, indent: int = 4) -> None:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=indent)
        print("Data was successfully written.")
    except Exception as e:
        print(f"Error occured: {e}")


def read_binary(file_path: str) -> bytes:
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        return data
    except Exception as e:
        print(f"Error occured: {e}")



def write_binary(file_path: str, bytes_text: bytes) -> None:
    try:
        with open(file_path, 'wb') as file:
            file.write(bytes_text)
        print("The binary data has been successfully saved to the file.")
    except Exception as e:
        print(f"Error occured: {e}")