import requests
import json

# Dados da imagem a serem enviados
image_data = [[0, 1, 2, ...]]  # Substitua pelos dados reais da imagem

# Remova ou substitua '...' por valores reais, dependendo dos seus dados
image_data_fixed = [[0, 1, 2, 3, 4, 5]]  

# URL da sua API local
url = "http://127.0.0.1:5000/"

# Enviar solicitação POST
response = requests.post(url, json={"image": image_data_fixed})

# Obter a resposta
result = response.json()
print(result)
