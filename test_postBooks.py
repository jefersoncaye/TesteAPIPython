from httpx import post
import json
url_base = 'https://fakerestapi.azurewebsites.net/api/v1/Books'

def test_adicionarUmNovoLivro():
    arquivo_json = open('payloads/add-book.json', 'r')
    arquivo_json = json.load(arquivo_json)
    request = post(url_base, json=arquivo_json)
    assert request.status_code == 200, 'Código de resposta Diferente de 200'
    assert request.json()['title'] == 'Livro Post'
    assert request.json()['description'] == 'Testando POST'
    assert request.json()['excerpt'] == 'Aqui temos uma descricao longa para testar o POST de uma API aleatoria'
