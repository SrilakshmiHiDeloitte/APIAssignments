import requests
import pytest


def test_check_status():
    response = requests.get('https://hbs-ob-stage.herokuapp.com/status')
    response_body = response.json()
    assert response.status_code == 200


def test_create_user():
    payload = {
        "name": "Srilaks",
        "phone": "+919391022222",
        "email": "visrilak@hashedin.com",
        "password": "Srilshmi",
        "otp": 111111
    }
    response = requests.post('https://hbs-ob-stage.herokuapp.com/user', json=payload)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 201


def test_get_otp():
    payload = {"phone": "+917095379695"}
    endpoint = 'https://hbs-ob-stage.herokuapp.com/get_register_otp'
    response = requests.post(url=endpoint, json=payload)
    print(response.status_code)
    response_body = response.json()
    print(response.status_code)
    assert response.status_code == 409


def test_del_user():
    payload = {
        "phone": "+919391022222",
        "otp": 111111
    }
    endpoint = 'https://hbs-ob-stage.herokuapp.com/user'
    response = requests.delete(url=endpoint, json=payload)
    print(response.json())
    assert response.status_code == 200


def test_edit_user():
    payload = {
        "name": "Srilaks",
        "phone": "+919391022222",
        "email": "visrilakhmi@hashedin.com",
        "password": "Srilakshmi",
        "otp": 111111
    }
    endpoint = 'https://hbs-ob-stage.herokuapp.com/user'
    response = requests.delete(endpoint, json=payload)
    print(response.status_code)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 200


def test_login_otp():
    payload = {
        "phone": "+919391022222"
    }
    endpoint = 'https://hbs-ob-stage.herokuapp.com/get_otp'
    response = requests.post(url=endpoint, json=payload)
    print(response.status_code)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 200


def test_authenticate():
    payload = {
        "phone": "+919391022222",
        "LoginType": "password",
        "password": "Srilakshmi"
    }
    endpoint = 'https://hbs-ob-stage.herokuapp.com/authenticate'
    response = requests.post(url=endpoint, json=payload)
    print(response.json())
    token = 'Bearer' + str(response.json()[1])
    assert response.status_code == 200

    # test_login_testing:
    endpoint = 'https://hbs-ob-stage.herokuapp.com/protected_test'
    headers = {'Authorization': token}
    print(requests.post(endpoint, data=data, headers=headers).json())
    assert requests.status_code == 200
