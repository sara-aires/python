import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Função para descriptografar
def decrypt_file():
    # Nome fixo do arquivo de entrada
    input_file = "ramsoware.txt"  # Arquivo criptografado

    # Verifica se o arquivo de entrada existe
    if not os.path.exists(input_file):
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
        return

    # Solicita a senha
    password = input("Digite a senha (até 16 caracteres): ")

    # Gera uma chave de 16 bytes a partir da senha
    key = password.encode('utf-8').ljust(16, b'\0')[:16]

    # Lê o IV e os dados criptografados do arquivo
    with open(input_file, 'rb') as f:
        data = f.read()
    
    iv = data[:16]  # IV está nos primeiros 16 bytes
    ciphertext = data[16:]  # O restante são os dados criptografados

    # Descriptografa o conteúdo
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)

    # Remove o padding
    plaintext = unpad(decrypted_data, 16)

    # Exibe o conteúdo descriptografado no console (sem salvar em arquivo)
    print("Conteúdo Descriptografado:")
    print(plaintext.decode('utf-8'))  # Exibe a mensagem em texto

# Executa a função de descriptografia
if __name__ == "__main__":
    decrypt_file()
