import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    return sha256_hash

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    data = input("Digite a chave a ser criptografada: ")
    sha256_hash = calculate_sha256_hash(data)
    
    save_to_file("save.txt", sha256_hash)
    print("Hash criptografado salvo no arquivo 'save.txt'.")

if __name__ == "__main__":
    main()