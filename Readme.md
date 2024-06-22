# File Encryption and Decryption

This repository contains two Python scripts for encrypting and decrypting files using the cryptography library.
Prerequisites

Before running the scripts, make sure you have the cryptography library installed. You can install it using pip:

```
pip install cryptography
```

## Encryption Script

The encryption script generates a key, encrypts a specified file, and saves the encrypted data and key.
Script: encrypt_file.py
Usage

```
    python encrypt_file.py
```

Enter the name of the file you want to encrypt (with extension).

### Explanation

    The script generates a key for encryption and saves it to a file called key.key.
    It reads the specified file, encrypts its contents, and saves the encrypted data to a new file with a .enc extension.
    If the file is not found or an error occurs during reading or writing, appropriate error messages are displayed.

## Decryption Script

The decryption script reads the key, decrypts a specified encrypted file, and saves the decrypted data.
Script: decrypt_file.py
Usage


    python decrypt_file.py

    Enter the name of the encrypted file (with extension).

    Enter the key for decryption.

### Explanation

The script reads the key provided by the user.

It reads the specified encrypted file and attempts to decrypt its contents.

If the file is not found, the key is invalid, or an error occurs during decryption or writing, appropriate error messages are displayed.

The decrypted data is saved to a file named decrypted_file.txt.
