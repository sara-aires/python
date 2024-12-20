import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Função para criptografar
def encrypt_file():
    # Nome fixo do arquivo de entrada e saída
    input_file = "teste.txt"
    output_file = "ramsoware.txt"

    # Verifica se o arquivo de entrada existe
    if not os.path.exists(input_file):
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
        return

    # Solicita a senha
    password = input("Digite a senha (até 16 caracteres): ")

    # Gera uma chave de 16 bytes a partir da senha
    key = password.encode('utf-8').ljust(16, b'\0')[:16]

    # Gera um IV aleatório
    iv = os.urandom(16)

    # Lê o conteúdo do arquivo
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Aplica o padding para garantir que o tamanho seja múltiplo de 16 bytes
    padded_plaintext = pad(plaintext, 16)

    # Criptografa o conteúdo
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_plaintext)

    # Salva o IV e os dados criptografados no arquivo de saída
    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)

    print(f"Arquivo '{input_file}' criptografado com sucesso como '{output_file}'.")

# Executa a função de criptografia
if __name__ == "__main__":
    encrypt_file()
