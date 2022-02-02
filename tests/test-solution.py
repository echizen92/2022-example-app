import requests 
from bs4 import BeautifulSoup

# login test cases
    
def test_login_1():
    session = requests.session()
    login = session.post("http://localhost:9988/login", {"username": "test@user.com", "password": "password"}).text
    soup = BeautifulSoup(login, "html.parser")
    print(soup.title.string)
    fault_text = soup.title.string
    assert fault_text == "ChaimTube"

def test_login_2():
    session = requests.session()
    login = session.post("http://localhost:9988/login", {"username": "test@user.com", "password": "pass"}).text
    soup = BeautifulSoup(login, "html.parser")
    print(soup.title.string)
    fault_text = soup.title.string
    assert fault_text == "Invalid login!" 

    
def test_login_3():
    session = requests.session()
    login = session.post("http://localhost:9988/login", {"username": "root@user.com", "password": "password"}).text
    soup = BeautifulSoup(login, "html.parser")
    print(soup.title.string)
    fault_text = soup.title.string
    assert fault_text == "Invalid login!"

if __name__ == '__main__':
    test_login_1()
    test_login_2()
    test_login_3()