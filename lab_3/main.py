import symmetric
import argparse
from files_interactions import *


def menu():
    parser = argparse.ArgumentParser()
    settings = read_json("settings.json")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', action='store_true', help='Generate symmetric and asymmetric keys')
    group.add_argument('-enc', '--encryption', action='store_true', help='Encrypt a file using symmetric key')
    group.add_argument('-dec', '--decryption', action='store_true', help='Decrypt a file using symmetric key')
    group.add_argument('-enc_sym', '--encryption_symmetric', action='store_true', help='Encrypt sym key using asym encryption')
    group.add_argument('-dec_sym', '--decryption_symmetric', action='store_true', help='Decrypt sym key using asym decryption')

    args = parser.parse_args()

    if args.generation:
        key_length = int(input("Enter the key length in bits, in the range [128, 192, 256]: "))
        print(f"Your key length: {key_length} ")
        
        key_serialization = symmetric.generate_key(key_length)
        symmetric.key_serialization(key_serialization, settings["symmetric_key_path"])

    elif args.encryption:
        symmetric_key = symmetric.key_deserialization(settings["symmetric_key_path"])
        symmetric.encrypt(symmetric_key, settings["initial_file_path"], settings["encrypted_file_path"])

    elif args.decryption:
        symmetric_key = symmetric.key_deserialization(settings["symmetric_key_path"])
        symmetric.decrypt(symmetric_key, settings["encrypted_file_path"], settings["decrypted_file_path"])


if __name__ == "__main__":
    menu()
