from cryptography.fernet import Fernet

def encrypt_file(file_name):
    try:
        # Generate a key for encryption
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)

        # Save the key to a file (important to save for decryption)
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
        
        try:
            # Read the file to encrypt
            with open(file_name, 'rb') as file:
                file_data = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
            return
        except IOError:
            print(f"Error: An error occurred while reading the file '{file_name}'.")
            return
        
        # Encrypt the file data
        encrypted_data = cipher_suite.encrypt(file_data)

        new_file_name = file_name + '.enc'
        try:
            # Save the encrypted data to a new file
            with open(new_file_name, 'wb') as file:
                file.write(encrypted_data)
            print(f"File '{file_name}' encrypted successfully to '{new_file_name}'.")
        except IOError:
            print(f"Error: An error occurred while writing the encrypted file '{new_file_name}'.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_name = input("Enter file name (with extension): ")
    encrypt_file(file_name)

