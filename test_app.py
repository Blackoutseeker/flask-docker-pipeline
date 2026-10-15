import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_status_code_e_retorno(client):
    resposta = client.get('/api/status')
    dados = resposta.get_json()

    assert resposta.status_code == 200
    assert dados['status'] == "operacional"
    assert dados['servico'] == "FastOrder-Web"


def test_home_mensagem(client):
    resposta = client.get('/')
    dados = resposta.get_json()
    assert dados['mensagem'] == "Bem-vindo ao API FastOrder!"


def test_soma(client):
    resposta = client.get('/api/soma?a=10&b=5')
    dados = resposta.get_json()
    assert resposta.status_code == 200
    assert dados['resultado'] == 15


def test_soma_parametros_invalidos(client):
    # Testando com uma string em vez de um número para forçar o erro de conversão
    resposta = client.get('/api/soma?a=texto&b=5')
    dados = resposta.get_json()

    assert resposta.status_code == 400
    assert dados['erro'] == "Parâmetros inválidos."
