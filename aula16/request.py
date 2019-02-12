from decimal import Decimal
import requests

response = requests.get('https://brasil.io/api/dataset/eleicoes-brasil/bens_candidatos/data')
results = response.json()['results']
proximo = response.json()['next']

for n in range(10):
	r = requests.get(proximo)
	proximo = r.json()['next']
	results += r.json()['results']

soma = 0
for element in results:
	soma += Decimal(element['valor_bem'])

media = round(soma/len(results), 2)

print('valor total de bens: '+str(soma))
print('Média de bens: '+str(media))

