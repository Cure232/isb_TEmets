from tests import *


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
       print("Произошла ошибка:", e)


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
       print("Произошла ошибка:", e)


def main() -> None:
    cpp_bit_string = read_txt("resources/cpp_sequence.txt")
    java_bit_string = read_txt("resources/java_sequence.txt")

    result = "cpp:\n"
    cpp_fbt = frequency_bit_test(cpp_bit_string)
    result += f"frequency_bit_test: {cpp_fbt}\n"
    cpp_cbt = consecutive_bits_test(cpp_bit_string)
    result += f"consecutive_bits_test: {cpp_cbt}\n\n"
    
    result += "java:\n"
    java_fbt = frequency_bit_test(java_bit_string)
    result += f"frequency_bit_test: {java_fbt}\n"
    java_cbt = consecutive_bits_test(java_bit_string)
    result += f"consecutive_bits_test: {java_cbt}\n"

    print(result)


if __name__ == '__main__':
    main() 