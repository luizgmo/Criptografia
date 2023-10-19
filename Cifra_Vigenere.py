def cifra_de_vigenere(frase, chave, criptografar=True):
    resultado = ""
    chave = chave.lower()
    chave_index = 0

    for letra in frase:
        if letra.isalpha():
            maiuscula = letra.isupper()
            letra = letra.lower()
            codigo = ord(letra)
            deslocamento = ord(chave[chave_index % len(chave)]) - 97        
            if criptografar:                                                
                codigo_cifrado = ((codigo - 97 + deslocamento) % 26) + 97   #97: Início do alfabeto minúsculo(a)
            else:                                                           #26: Tamanho do alfabeto
                codigo_cifrado = ((codigo - 97 - deslocamento) % 26) + 97  
            if maiuscula:
                letra_cifrada = chr(codigo_cifrado).upper()
            else:
                letra_cifrada = chr(codigo_cifrado)
            resultado += letra_cifrada
            chave_index += 1
        else:
            resultado += letra
    return resultado

def main():
    while True:
        print("")
        print("CIFRA DE VIGENÉRE")
        opcao = input("Escolha uma opção:\n1 - Criptografar\n2 - Descriptografar\n3 - Sair\nOpção: ")

        if opcao == '1':
            frase = input("Digite a frase que deseja criptografar: ")
            chave = input("Digite a chave: ")
            frase_criptografada = cifra_de_vigenere(frase, chave)
            print("")
            print("Frase criptografada:", frase_criptografada)

            with open("resultado_criptografia_vigenere.txt", "a") as arquivo:
                arquivo.write(f"Frase criptografada (chave={chave}): {frase_criptografada}\n")
                
        elif opcao == '2':
            frase = input("Digite a frase que deseja descriptografar: ")
            chave = input("Digite a chave: ")
            frase_descriptografada = cifra_de_vigenere(frase, chave, criptografar=False)
            print("")
            print("Frase descriptografada:", frase_descriptografada)

            with open("resultado_criptografia_vigenere.txt", "a") as arquivo:
                arquivo.write(f"Frase descriptografada (chave={chave}): {frase_descriptografada}\n")
                
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    with open("resultado_criptografia_vigenere.txt", "w") as arquivo:
        arquivo.write("Resultados da Criptografia de Vigenère\n\n")
    main()
