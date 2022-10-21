import requests
import jsonpath
from json import jsonify
from flask import Flask, request, jsonify

def test_app(client):
    assert client.get('http://127.0.0.1:5000/user').status_code == 200

@api.route('/ping')
def ping():
    return jsonify(ping='pong')

def test_api_ping(client):
    res = client.get(url_for('api.ping'))
    assert res.json == {'ping': 'pong'}