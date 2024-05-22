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


def set_new_cypher_parameters(path: str, new_alphabet: dict | None = None, new_key: str | None = None) -> None:
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
            letter = str(letter).lower()
            while True:
                x = randint(1, len(new_alphabet.keys()))
                if x not in list(json_content['alphabet'].values()):
                    json_content['alphabet'][letter] = x
                    break
    
    if new_key:
        json_content["key"] = new_key.lower()
        numerise_letter = lambda letter: json_content['alphabet'][letter]
        json_content['key_numerised_value'] = [numerise_letter() for letter in json_content['key']]

    write_json(path, json_content)


def main() -> None:
    russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё',
                         'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                           'н', 'о', 'п', 'р', 'с', 'т', 'у',
                             'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
                               'ы', 'ь', 'э', 'ю', 'я']
    set_new_cypher_parameters("task1/key.json", russian_alphabet, "панграмма")



if __name__ == '__main__':
    main()        
