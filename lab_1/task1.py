import json

from random import randint


def read_json(file_path: str) -> dict:
    """function, which can get dict from .json file

    Returns:
        dict[str:str]: dictionary with pair (key - value)
    """
    try:
        with open(file_path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except Exception as e:
       print("Произошла ошибка:", e)


def write_json(file_path: str, content: dict) -> None:
    """function, that writes data to .json file

    Args:
        file_path (str): path to file, that we want to fill
        content (dict): what we want to write in file
    """
    try:
        with open(file_path, 'w', encoding="UTF-8") as file:
            json.dump(content, file, ensure_ascii=False, indent=4)
    except Exception as e:
       print("Произошла ошибка:", e)


def set_new_cypher_parameters(path: str, new_alphabet: list[str] | None = None, new_key: str | None = None) -> None:
    """function that sets new alphabet and/or key
       to existing .json key file or creates new one with given data

    Args:
        path (str): path to .json file or new file path.
        new_alphabet (dict | None, optional): preferred new alphabet. Defaults to None.
        new_key (str | None, optional): preferred new key. Defaults to None.
    """
    json_content = dict()
    try:
        json_content = read_json(path)
    except Exception as e:
        print(e, "\nФайл не найден, будет создан новый.")

    if new_alphabet:
        json_content["alphabet"] = dict()
        for letter in new_alphabet:
            letter = letter.lower()
            while True:
                x = randint(1, len(new_alphabet))
                if x not in list(json_content['alphabet'].values()):
                    json_content['alphabet'][letter] = x
                    break
    
    if new_key:
        json_content["key"] = new_key.lower()
        numerise_letter = lambda letter: json_content['alphabet'][letter]
        json_content['key_numerised_value'] = [numerise_letter(letter) for letter in json_content['key']]

    write_json(path, json_content)


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


def cypher_text(text: str, json_key_content: dict) -> str:
    """cyphers text: every letter is assigned to unique number,
       so new letter number equals sum of
       original number plus original number of a set keyword

    Args:
        text (str): text to cypher
        json_key_content (dict): json that contains alphabet where
        each letter has assigned number and a keyword
        

    Returns:
        str: cyphered text
    """
    result = str()
    alphabet = json_key_content['alphabet']
    alphabet_reverse = {alphabet[letter]:letter for letter in alphabet} 
    numerised_keyword = json_key_content["key_numerised_value"]
    nk_index = 0 #numerised keyword index

    for symbol in text:
        upcase_needed = False
        if symbol != symbol.lower():
            symbol = symbol.lower()
            upcase_needed = True

        if symbol in alphabet:
            num = alphabet[symbol]
            num += numerised_keyword[nk_index]
            if num > len(alphabet):
                num -= len(alphabet)
            decyphered_symbol = str(alphabet_reverse[num])

            if upcase_needed:
                decyphered_symbol = decyphered_symbol.upper()

            result += decyphered_symbol
            nk_index += 1
            if nk_index >= len(numerised_keyword): 
                nk_index = 0
        else:
            result += symbol
    
    return result


def decypher_text(text: str, json_key_content: dict) -> str:
    """decyphers text: every letter is assigned to unique number,
       so old letter number equals that number minus original number of a set keyword

    Args:
        text (str): text to cypher
        json_key_content (dict): json that contains alphabet where
        each letter has assigned number and a keyword
        

    Returns:
        str: cyphered text
    """
    result = ""
    alphabet = json_key_content['alphabet']
    alphabet_reverse = {alphabet[letter]:letter for letter in alphabet} 
    numerised_keyword = json_key_content["key_numerised_value"]
    nk_index = 0 #numerised keyword index

    for symbol in text:
        upcase_needed = False
        if symbol != symbol.lower():
            symbol = symbol.lower()
            upcase_needed = True

        if symbol in alphabet:
            num = alphabet[symbol]
            num -= numerised_keyword[nk_index]
            if num <= 0:
                num += len(alphabet)
            decyphered_symbol = str(alphabet_reverse[num])

            if upcase_needed:
                decyphered_symbol = decyphered_symbol.upper()
                
            result += decyphered_symbol
            nk_index += 1
            if nk_index >= len(numerised_keyword): 
                nk_index = 0
        else:
            result += symbol
    
    return result


def main() -> None:
    paths = read_json("lab_1/paths.json")
    task1_paths = paths["task1"]

    russian_alphabet = dict(read_json(task1_paths["key"])["alphabet"]).keys()
    set_new_cypher_parameters(task1_paths["key"], new_alphabet=russian_alphabet, new_key="панграмма")
    
    write_txt(task1_paths["result"], cypher_text(read_txt(task1_paths["message"]), read_json(task1_paths["key"])))
    write_txt(task1_paths["result_decypher"], decypher_text(read_txt(task1_paths["result"]), read_json(task1_paths["key"])))


if __name__ == '__main__':
    main()   
