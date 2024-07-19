import requests
import pytest


URL =  'https://api.pokemonbattle.ru/v2'
TOKEN = '35077fd41d298a0399303a038c4207ba'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = "4200"



def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200


def test_name():
        response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
        assert response_get.json()["data"][0]["trainer_name"] == "Денис"