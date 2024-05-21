import json
from random import randint


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


def main() -> None:
    russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё',
                         'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                           'н', 'о', 'п', 'р', 'с', 'т', 'у',
                             'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
                               'ы', 'ь', 'э', 'ю', 'я']
    json_content = dict()
    json_content["alphabet"] = dict()

    for letter in russian_alphabet:
        while True:
            x = randint(1,33)
            if x not in list(json_content['alphabet'].values()):
                json_content['alphabet'][letter] = x
                break
    
    json_content["key"] = "панграмма"
    numerise_letter = lambda letter: json_content['alphabet'][letter]
    json_content['key_numerised_value'] = [numerise_letter(letter) for letter in json_content['key']]
    write_json("task1/key.json",json_content)


if __name__ == '__main__':
    main()        