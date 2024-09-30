import argparse
import symmetric
import assymetric
from files_interactions import *


def menu():
    parser = argparse.ArgumentParser()
    settings = read_json("settings.json")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', action='store_true', help='Generate symmetric and asymmetric keys')
    group.add_argument('-enc', '--encryption', action='store_true', help='Encrypt a file using symmetric key')
    group.add_argument('-dec', '--decryption', action='store_true', help='Decrypt a file using symmetric key')
    group.add_argument('-enc_sym', '--encrypt_symmetric_key', action='store_true', help='Encrypt sym key using asym encryption')
    group.add_argument('-dec_sym', '--decrypt_symmetric_key', action='store_true', help='Decrypt sym key using asym decryption')

    args = parser.parse_args()

    if args.generation:
        key_length = 128
        print(f"Your key length: {key_length}\n Algorithm: SM4\n")
        
        assym_keys = assymetric.generate_keys()
        assymetric.serialize_private_key(assym_keys["private_key"], settings["private_key_path"])
        assymetric.serialize_public_key(assym_keys["public_key"], settings["public_key_path"])
        key_serialization = symmetric.generate_key(key_length)
        symmetric.serialize_key(key_serialization, settings["symmetric_key_path"])

    elif args.encryption:
        symmetric_key = symmetric.deserialize_key(settings["symmetric_key_path"])
        symmetric.encrypt(symmetric_key, settings["initial_file_path"], settings["encrypted_file_path"])

    elif args.decryption:
        symmetric_key = symmetric.deserialize_key(settings["symmetric_key_path"])
        symmetric.decrypt(symmetric_key, settings["encrypted_file_path"], settings["decrypted_file_path"])

    elif args.encrypt_symmetric_key:
        symmetric_key = symmetric.deserialize_key(settings["symmetric_key_path"])
        public_key = assymetric.deserialize_public_key(settings["public_key_path"])
        
        encrypted_symmetric_key = assymetric.encrypt(public_key, symmetric_key)
        write_binary(settings["encrypted_key_path"], encrypted_symmetric_key)

    elif args.decrypt_symmetric_key:
        private_key = assymetric.deserialize_private_key(settings["private_key_path"])
        encrypted_symmetric_key = read_binary(settings["encrypted_key_path"])
        
        decrypted_symmetric_key = assymetric.decrypt(private_key, encrypted_symmetric_key)
        write_binary(settings["decrypted_key_path"], decrypted_symmetric_key)

if __name__ == "__main__":
    menu()
