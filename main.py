import requests
from bs4 import BeautifulSoup
import json
import getpass

baseURL = "https://schoolbox.arden.nsw.edu.au"
loginURL = baseURL + "/login/"
session = requests.Session()

def getNoti():
    notiJSON = session.get(baseURL + "/news/lists/feed").text
    notis = json.loads(notiJSON)
    finalNotiList = [f"{item["title"]}: {item["blurb"]}" for item in notis]
    return finalNotiList



if __name__ == "__main__":
    u = input("Username: ")
    p = getpass.getpass("Password: ")

    package = {
        "username" : u,
        "password": p
        }
    
    response = session.post(loginURL, data=package)
    if response.url != loginURL:
        print("Success!")
        pageData = BeautifulSoup(response.text, "html.parser")
        print(getNoti())
    else:
        print("Login failed. Please check if password is in date and credentials are correct")