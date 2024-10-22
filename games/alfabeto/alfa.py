import random

alfabeto_palavras = {
    'A': 'Abacate',
    'B': 'Bola',
    'C': 'Cachorro',
    'D': 'Dado',
    'E': 'Elefante',
    'F': 'Foca',
    'G': 'Gato',
    'H': 'Hipopótamo',
    'I': 'Igreja',
    'J': 'Jacaré',
    'K': 'Kiwi',
    'L': 'Leão',
    'M': 'Macaco',
    'N': 'Navio',
    'O': 'Ovelha',
    'P': 'Pato',
    'Q': 'Queijo',
    'R': 'Rato',
    'S': 'Sapo',
    'T': 'Tigre',
    'U': 'Urso',
    'V': 'Vaca',
    'W': 'Wolverine',
    'X': 'Xaxim',
    'Y': 'Yeti',
    'Z': 'Zebra'
}

def fase_1():
    print("\n--- Fase 1: Letras do Alfabeto ---")
    letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(letras)

    for letra in letras:
        resposta = input(f"Qual palavra que começa com a letra '{letra}'? ").strip().capitalize()
        if resposta.startswith(letra):
            print("Muito bem!")
        else:
            print(f"A palavra correta deve começar com '{letra}'.")

def fase_2():
    print("\n--- Fase 2: Imagens (Exemplo) ---")
    for letra, palavra in alfabeto_palavras.items():
        resposta = input(f"Qual letra começa a palavra '{palavra}'? ").strip().upper()
        if resposta == letra:
            print("Muito bem!")
        else:
            print(f"A palavra '{palavra}' começa com a letra '{letra}'.")

def fase_3():
    print("\n--- Fase 3: Frases Curiosas ---")
    letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(letras)

    for letra in letras:
        frase = input(f"Crie uma frase usando palavras que começam com a letra '{letra}': ")
        if any(palavra.startswith(letra) for palavra in frase.split()):
            print("Ótima frase! Você usou palavras que começam com a letra!")
        else:
            print(f"Tente novamente! Sua frase deve conter palavras que começam com '{letra}'.")

def jogar():
    print("Bem-vindo ao Alfabeto Mágico!")
    fase_1()
    fase_2()
    fase_3()
    print("\nParabéns! Você completou todas as fases!")

if __name__ == "__main__":
    jogar()
