import ast
import matplotlib.pyplot as plt
import pandas as pd

with open('/home/mario/Downloads/dados/dados_brasil.csv', 'r') as file:
	lines = file.readlines()

	for line in lines:
		if "Aumento do PIB (% anual)" in line:
			pib_list = list(ast.literal_eval(line)[4:])
		elif "Country Code" in line:
			years = list(ast.literal_eval(line)[4:])

	for index, value in enumerate(pib_list):
		if value == '':
			pib_list[index] = None
		else:
			pib_list[index] = float(value)

	for index, value in enumerate(years):
		years[index] = int(value)

	df = pd.DataFrame(data=pib_list, index=years)
	df.plot()
	# plt.show()
	plt.savefig('variacao_pib_brasil.svg')