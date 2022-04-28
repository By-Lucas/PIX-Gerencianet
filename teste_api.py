#Desenvolvido pela Consultoria Técnica da Gerencianet

import requests
import base64, json

credentials = {
    "client_id": "Client_Id_493944299db401abb42a0251b0e28cf0eda2a507",
    "client_secret": "Client_Secret_22e044074c3c82f4bf95400756f323ed7608907c",
}

certificado = 'examples\certificado.pem'  # A variável certificado é o diretório em que seu certificado em formato .pem deve ser inserido

auth = base64.b64encode(
    (f"{credentials['client_id']}:{credentials['client_secret']}"
     ).encode()).decode()

url = "https://api-pix-h.gerencianet.com.br/oauth/token"  #Para ambiente de Desenvolvimento

payload="{\r\n    \"grant_type\": \"client_credentials\"\r\n}"
headers = {
    'Authorization': f"Basic {auth}",
    'Content-Type': 'application/json'
}

response = requests.request("POST",
                            url,
                            headers=headers,
                            data=payload,
                            cert=certificado)

#print(json.loads(response.text))
if 'access_token' in response.text:
    data = response.json()
    print(data['access_token'])
