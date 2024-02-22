from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

file1 = 'Base Text - Matrix Representation I - v2.txt'
file2 = 'Base Text - Matrix Representation II - v2.txt'

with open(file1, 'r', encoding='utf-8') as arquivo:
    texto1 = arquivo.read()

with open(file2, 'r', encoding='utf-8') as arquivo:
    texto2 = arquivo.read()

# Vetorizando os textos
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform([texto1, texto2])

# Calculando a similaridade de cosseno
similaridade = cosine_similarity(tfidf[0:1], tfidf[1:2])

print(f"A similaridade entre os textos é de: {similaridade[0][0]*100:.2f}%")