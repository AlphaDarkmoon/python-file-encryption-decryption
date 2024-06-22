from cryptography.fernet import Fernet, InvalidToken

def decrypt_file(file_name, key):
    try:
        # Initialize the cipher suite with the provided key
        cipher_suite = Fernet(key)
    except ValueError:
        print("Error: The provided key is invalid.")
        return

    try:
        # Read the encrypted file
        with open(file_name, 'rb') as file:
            encrypted_data = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return
    except IOError:
        print(f"Error: An error occurred while reading the file '{file_name}'.")
        return

    try:
        # Decrypt the file data
        decrypted_data = cipher_suite.decrypt(encrypted_data)
    except InvalidToken:
        print("Error: The provided key is incorrect or the data is corrupted.")
        return
    except Exception as e:
        print(f"An unexpected error occurred during decryption: {e}")
        return

    try:
        # Save the decrypted data to a new file
        with open('decrypted_file.txt', 'wb') as file:
            file.write(decrypted_data)
        print(f"File '{file_name}' decrypted successfully to 'decrypted_file.txt'.")
    except IOError:
        print("Error: An error occurred while writing the decrypted file.")

if __name__ == "__main__":
    file_name = input("Enter file name (with extension): ")
    key = input("Enter Key: ")
    decrypt_file(file_name, key)

