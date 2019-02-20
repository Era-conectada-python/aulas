import requests


url_pacientes = 'http://localhost:8000/pacientes/'
data = {
    "nome": "Bozo",
    "idade": "2006-10-01 00:00:00",
    "telefone": "asds",
    "profissao": "presida",
    "email": "bozo@psl.com"
}

response = requests.get(url_pacientes)
print(response.status_code, response.json()[0]['nome'])

for x in range(300):
    response_post = requests.post(url_pacientes,
                                  data=data,
                                  auth=('mario', '96384270mario'))

    print(response_post.status_code)