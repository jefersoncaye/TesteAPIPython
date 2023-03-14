from httpx import put
import json
url_base = 'https://fakerestapi.azurewebsites.net/api/v1/Books'


def test_alterandoUmLivro():
    arquivo_json = open('payloads/put-book.json', 'r')
    arquivo_json = json.load(arquivo_json)
    request = put(f'{url_base}/{arquivo_json["id"]}', json=arquivo_json)
    assert request.status_code == 200
    assert request.json()['title'] == 'Livro Post Alterado'
    assert request.json()['description'] == 'Testando PUT'
    assert request.json()['excerpt'] == 'Aqui temos uma descricao longa para testar o PUT de uma API aleatoria'