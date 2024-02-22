import string
import numpy as np

file1 = 'Base Text - Matrix Representation I - v2.txt'
file2 = 'Base Text - Matrix Representation II - v2.txt'

def TextComparison(filename):
    vetor_dados = []
    vetor_somente_valores = []

    with open(filename, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        # Remove pontuações do texto
        conteudo_sem_pontuacao = conteudo.translate(str.maketrans('', '', string.punctuation))
        palavras = conteudo_sem_pontuacao.split()

########################################################################################################################
    NumeroDeCaracterers = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '>5': 0}

    # Itera sobre cada palavra na lista
    for palavra in palavras:
        tamanho = len(palavra)  # Calcula o comprimento da palavra
        if tamanho > 5:
            NumeroDeCaracterers['>5'] += 1
        else:
            # Atualiza a contagem para o comprimento correspondente
            NumeroDeCaracterers[str(tamanho)] += 1

    # Adicionando dados de contagem de comprimento
    for chave, valor in NumeroDeCaracterers.items():
        vetor_dados.append({'tipo': 'comprimento', 'chave': chave, 'valor': valor})
        vetor_somente_valores.append(valor)

########################################################################################################################
    LetrasAlfabeto = {chr(i): 0 for i in range(97, 123)}  # 97 a 122 são os códigos ASCII para 'a' a 'z'

    for palavra in palavras:
        primeira_letra = palavra[0].lower()  # Converte a primeira letra para minúscula para uniformidade
        if primeira_letra in LetrasAlfabeto:
            LetrasAlfabeto[primeira_letra] += 1

    # Adicionando dados de contagem de letras
    for chave, valor in LetrasAlfabeto.items():
        vetor_dados.append({'tipo': 'letra', 'chave': chave, 'valor': valor})
        vetor_somente_valores.append(valor)

########################################################################################################################

    vetor_dados = np.array(vetor_dados)
    vetor_somente_valores = np.array(vetor_somente_valores)

    return vetor_dados, vetor_somente_valores

vetor_dados1, vetor_somente_valores1 = TextComparison(file1)
vetor_dados2, vetor_somente_valores2 = TextComparison(file2)

similaridade_cosseno = np.dot(vetor_somente_valores1, vetor_somente_valores2) / (np.linalg.norm(vetor_somente_valores1) * np.linalg.norm(vetor_somente_valores2))

print(f"A similaridade entre os textos é de: {similaridade_cosseno*100:.2f}%")


