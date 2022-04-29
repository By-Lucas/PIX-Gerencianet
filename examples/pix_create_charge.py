from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'txid': 'fc9a4366ff3d4964b5dbc6c91a8722d3'
}

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '07490113512',
        'nome': 'Lucas da Silva dos Santos'
    },
    'valor': {
        'original': '0.50'
    },
    'chave': '71cdf9ba-c695-4e3c-b010-abb521a3f1be',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response =  gn.pix_create_charge(params=params,body=body)
print(response)
