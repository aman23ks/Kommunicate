import requests
import json

def test_complete_chat():
  url = 'http://127.0.0.1:5000/complete_chat'
  data = {'partial_text': 'What is the capital of France?'}
  response = requests.post(url, json=data)
  assert response.status_code == 200
  response_json = json.loads(response.text)
  assert 'completed_text' in response_json
  assert len(response_json['completed_text']) > 0 

