import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Passo 1:Ler o Dataset
df = pd.read_excel('Defective_Equipment (rev 2024-02-21) - Transposta.xlsx')
print(df.head())

# Garanta que 'ID' não seja incluído na transformação do PCA
X = df.drop('Seq', axis=1).select_dtypes(include=[np.number])
labels = df['Seq'].values
print(labels)

# Passo 2: Normalizar os dados
scaler = StandardScaler()
scaled_data = scaler.fit_transform(X)

# Passo 3: Aplicar PCA
pca = PCA(n_components=1)
pca_results = pca.fit_transform(scaled_data)

# Criar índices para o eixo x
indices = np.arange(len(pca_results))
y = [0] * len(pca_results)

# Visualizar a variância explicada
print(f'Variância explicada: {pca.explained_variance_ratio_}')

plt.figure(figsize=(12, 8))
plt.scatter(pca_results, y, alpha=0.5)  # Plotagem dos pontos

# Adicionar rótulos
deslocamento_x = 0.02
deslocamento_y = 0.001

# Opcional: Adicionar rótulos
for i, label in enumerate(labels):
    plt.text(pca_results[i]+deslocamento_x, y[i] + deslocamento_y, ' '+str(label), rotation=45, ha='left', va='bottom', fontsize=9)

plt.title('Visualização do Primeiro Componente Principal')
plt.gca().get_yaxis().set_visible(False)
plt.gca().get_xaxis().set_visible(False)
plt.axhline(0, color='red', linestyle='--')
plt.show()