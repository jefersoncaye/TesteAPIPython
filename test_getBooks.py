from httpx import get

url_base = 'https://fakerestapi.azurewebsites.net/api/v1/Books'


def test_buscarTodosLivros():
    request = get(url_base)
    assert request.status_code == 200, 'Código de resposta Diferente de 200'
    assert request.json() != [], 'Retorno foi Vazio'
    assert request.json()[0]['title'] == 'Book 1', 'Primeiro retorno Não é Igual a "Book 1"'

