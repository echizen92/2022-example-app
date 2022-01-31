import requests
import pytest

# login test cases
    
def test_login_1():
    session = requests.session()
    login = session.post("http://localhost:9988/login", {"username": "test@user.com", "password": "password"}).text
    print ("Successful login")
    #assert fault_text == "Successful login"

def test_login_2():
    session = requests.session()
    login = session.post("http://localhost:9988/login", {"username": "test@user.com", "password": "pass"}).text
    fault_text = login 
    assert fault_text == "Wrong password"
    
def test_login_3():
    session = requests.session()
    login = session.post("http://localhost:9988/login", {"username": "root@user.com", "password": "password"}).text
    fault_text = login
    assert fault_text == "Wrong username"

if __name__ == '__main__':
    test_login_1()
    test_login_2()
    test_login_3()

