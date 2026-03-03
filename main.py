import requests

loginUrl = "https://schoolbox.arden.nsw.edu.au/login/"

session = requests.Session()

session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

if __name__ == "__main__":
    u = input("Username: ")
    p = input("Password: ")

    package = {
        "username" : u,
        "password" : p
    }

response = session.post(loginUrl, data=package)

if response.status_code == 200 and "Dashboard" in response.text:
    print("Success! We are in.")
else:
    print("Login failed. Check if there was a CSRF token required.")