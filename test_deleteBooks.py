from httpx import delete, post
import json

url_base = 'https://fakerestapi.azurewebsites.net/api/v1/Books'


def test_adicionandoEDeletenadoUmLivro():
    arquivo_json = open('payloads/add-book.json', 'r')
    arquivo_json = json.load(arquivo_json)
    post(url_base, json=arquivo_json)
    request = delete(f'{url_base}/{arquivo_json["id"]}')
    assert request.status_code == 200

