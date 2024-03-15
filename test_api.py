from unittest.mock import patch
from flask import Flask
from main import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as c:
        yield c

def test_complete_chat_valid_input(client):
    mock_openai = patch('openai.Completion.create')
    with mock_openai as m:
        m.return_value = {'choices': [{'text': 'Sample generated response'}]}

    data = {'partial_text': 'Hello, how are you?'}
    response = client.post('/complete_chat', json=data)

    assert response.status_code == 200
    assert response.json['completed_text'] == 'Sample generated response'

def test_complete_chat_empty_input(client):
    data = {'partial_text': ''}
    response = client.post('/complete_chat', json=data)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid input. \'partial_text\' field is empty.'

def test_complete_chat_invalid_json(client):
    response = client.post('/complete_chat', data='invalid json')

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid input. Request data is not valid JSON.'

def test_complete_chat_missing_field(client):
    data = {'other_field': 'value'}
    response = client.post('/complete_chat', json=data)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid input. \'partial_text\' field is missing.'

def test_internal_server_error(client):
    with patch('openai.Completion.create') as mock_openai:
        mock_openai.side_effect = Exception('Unexpected error')

        data = {'partial_text': 'Any text'}
        response = client.post('/complete_chat', json=data)

        assert response.status_code == 500
        assert response.json['error'] == 'An unexpected error occurred.'
