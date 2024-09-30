from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def generate_keys() -> dict:

    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    return {
        "private_key": keys, 
        "public_key": keys.public_key()
    }


def serialize_public_key(public_key: bytes, public_path: str) -> None:
  
    try:
        with open(public_path, 'wb') as public_out:
            public_out.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
    except Exception as e:
       print("Error occured:", e)


def serialize_private_key(private_key, private_path: str) -> None:

    try:
        with open(private_path, 'wb') as private_out:
            private_out.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
                ))
    except Exception as e:
       print("Error occured:", e)


def deserialize_public_key(public_path: str) -> str:

    try:
        with open(public_path, 'rb') as pem_in:
            public_bytes = pem_in.read()
        public_key = load_pem_public_key(public_bytes)
        return public_key
    except Exception as e:
       print("Error occured:", e)


def deserialize_private_key(private_path: str) -> str:
    try:
        with open(private_path, 'rb') as pem_in:
            private_bytes = pem_in.read()
        private_key = load_pem_private_key(private_bytes, password=None)
        return private_key
    except Exception as e:
       print("Error occured:", e)


def encrypt(public_key: str, symmetric_key: bytes) -> bytes:
    encrypted_symmetric_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None)
        )
    return encrypted_symmetric_key


def decrypt(private_key: str, symmetric_key: bytes) -> bytes:
    decrypted_symmetric_key = private_key.decrypt(
        symmetric_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None)
        )
    return decrypted_symmetric_key