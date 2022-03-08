import requests
import pytest
import pandas as pd
from openpyxl.workbook import Workbook
from requests.auth import HTTPBasicAuth


# Registering the user
def test_register_user():
    payload = {
        "name": "Srilakshmi Vinnakota",
        "email": "srilakshmivinn@gmail.com",
        "password": "HiDeloitte12345",
        "age": 24
    }
    response = requests.post('https://api-nodejs-todolist.herokuapp.com/user/register', json=payload)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 201


# Logging in
def test_user_login():
    for key, value in y.items():
        if key == 'token':
            token = value
    payload = {
        "email": "srilakshmivinn@gmail.com",
        "password": "HiDeloitte12345"
    }
    response = requests.post('https://api-nodejs-todolist.herokuapp.com/user/login', json=payload)
    response_body = response.json()
    print(response.json())
    assert response.status_code == 200


def test_user_login_task():
    payload = {
        "email": "srilakshmivinn@gmail.com",
        "password": "HiDeloitte12345"
    }
    response = requests.post('https://api-nodejs-todolist.herokuapp.com/user/login', json=payload)
    return response.json()


global y
y = test_user_login_task()


# Validating User
def test_validate_user():
    for key, value in y.items():
        if key == 'token':
            token = value
    endpoint = 'https://api-nodejs-todolist.herokuapp.com/user/me'
    response = requests.get(endpoint,
                            auth=HTTPBasicAuth('srilakshmivinn@gmail.com', 'HiDeloitte12345'))
    Bearer = 'Bearer ' + str(token)
    headers = {
        'Authorization': Bearer}
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200


# Deleting the User
def test_del_user():
    for key, value in y.items():
        if key == 'token':
            token = value
    payload = {
        "email": "srilakshmivinn@gmail.com",
        "password": "HiDeloitte12345"
    }
    endpoint = 'https://api-nodejs-todolist.herokuapp.com/user/me'
    response = requests.get(endpoint,
                            auth=HTTPBasicAuth('srilakshmivinn@gmail.com', 'HiDeloitte12345'))
    Bearer = 'Bearer ' + str(token)
    print(Bearer)
    headers = {
        'Authorization': Bearer}
    response = requests.delete(url=endpoint, headers=headers)
    print(response.json())
    assert response.status_code == 200


# Adding 20 Tasks
def test_add_task():
    print(y)
    print(type(y))
    payload = open('Main_Assignment/testdata.txt', 'r')
    print(payload)
    for key, value in y.items():
        if key == 'token':
            token = value
    endpoint = 'https://api-nodejs-todolist.herokuapp.com/task'
    response = requests.get(endpoint,
                            auth=HTTPBasicAuth('srilakshmivinn@gmail.com', 'HiDeloitte12345'))
    Bearer = 'Bearer ' + str(token)
    print(Bearer)
    headers = {
        'Authorization': Bearer}
    for key1 in payload.keys():
        for value1 in payload.values():
            response2 = requests.post(endpoint, json={key1: value1}, headers=headers)
            print(response.status_code)
            print(response2.json())
            assert response2.status_code == 201
    if response2.status_code == 201:
        df = pd.DataFrame(payload, index=[0])
        df.to_excel('C:\\Users\\visrilakshmi\\PycharmProjects\\pythonProject2\\venv\\Scripts\\task.xlsx')


# Task by Pagination
@pytest.mark.parametrize('skip, end', [(2, 20), (5, 20), (10, 20)])
def test_get_pages(skip, end):
    y = test_user_login_task()
    print(y)
    for key, value in y.items():
        if key == 'token':
            token = value
    payload = {
        "email": "srilakshmivinn@gmail.com",
        "LoginType": "password",
        "password": "HiDeloitte12345"
    }
    endpoint = 'https://api-nodejs-todolist.herokuapp.com/task?'
    response = requests.get(endpoint,
                            auth=HTTPBasicAuth('srilakshmivinn@gmail.com', 'HiDeloitte12345'))
    endpoint = endpoint + 'limit=' + str(skip) + '&skip=' + str(end)
    print(endpoint)
    Bearer = 'Bearer ' + str(token)
    print(Bearer)
    headers = {
        'Authorization': Bearer}
    headers = {'Authorization': Bearer}
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    assert response.status_code == 200


# Getting all the data to an Excel file
def test_get_tasklist_toexcl():
    for key, value in y.items():
        if key == 'token':
            token = value
    endpoint = 'https://api-nodejs-todolist.herokuapp.com/task'
    Bearer = 'Bearer ' + str(token)
    print(Bearer)
    headers = {
        'Authorization': Bearer}
    response = requests.get(endpoint,
                            auth=HTTPBasicAuth('srilakshmivinn@gmail.com', 'HiDeloitte12345'))

    response2 = requests.get(endpoint, headers=headers)
    k = response2.json()
    # print(response2.json())
    # print(response2.content)
    for key, value in k.items():
        if key == 'data':
            for i in value:
                print(i)
                for j, m in i.items():
                    if j == 'description':
                        df = pd.DataFrame(i, index=[0])
                        print(df)
                        df.to_excel(
                            'Main_Assignment/Tasklist.xlsx')
    assert response.status_code == 200
