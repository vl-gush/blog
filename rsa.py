import argparse
import binascii
import os

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

"""
У скрипта есть два режима работы.
1. Шифрование исходного сообщения:
    python rsa.py --action=encrypt --message="Test new message"
2. Дешифрование сообщения:
    python rsa.py --action=decrypt --message=ТоЧтоВывелоНаПечатьПредыдущаяКоманда
"""
parser = argparse.ArgumentParser(description="Encrypt commands")
parser.add_argument("--action", type=str, choices=("encrypt", "decrypt"), help="Action to run")
parser.add_argument("--message", type=str, required=True, help="Message")


if __name__ == "__main__":
    if not os.path.exists("id_rsa"):
        # Генерируем новый ключ
        key_pair = RSA.generate(2048)
        open("id_rsa", "w").write(key_pair.export_key().decode())
    else:
        # Или переиспользуем старый
        f = open("id_rsa", "r")
        key_pair = RSA.importKey(f.read())

    args = parser.parse_args()
    cipher = PKCS1_OAEP.new(key_pair)
    if args.action == "encrypt":
        # Переводим строку в байты
        message = args.message.encode()
        # Шифруем сообщение
        encrypted = cipher.encrypt(message)
        # Переводим сообщение в HEX кодировку
        hex_string = binascii.hexlify(encrypted)
        # Переводим байты в строку и печатаем
        print(hex_string.decode())
    else:
        # Переводим сообщение из HEX кодировки
        message = binascii.unhexlify(args.message)
        # Дешифруем сообщение
        decrypted = cipher.decrypt(message)
        # Переводим байты в строку и печатаем
        print(decrypted.decode())
