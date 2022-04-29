from gerencianet import Gerencianet
from credentials import CREDENTIALS
import base64

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 1,
  "calendario": {
    "expiracao": 3600
  },
  "devedor": {
    "cpf": "0749011wdawd3512",
    "nome": "Lucas da Silva dos Santos"
  },
  "valor": {
    "original": "0.02"
  },
  "chave": "71cdf9ba-c695-4e3c-b010-abb521a3f1be",
  "solicitacaoPagador": "Informe o número ou identificador do pedido."

}

response =  gn.pix_generate_QRCode(params=params)
print(response)

#Generate QRCode Image
if('imagemQrcode' in response):
    with open("qrCodeImage.png", "wb") as fh:
        fh.write(base64.b64decode(response['imagemQrcode'].replace('data:image/png;base64,', '')))