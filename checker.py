import requests

url = "https://www.blackdesertonline.com/login"
email = input("Email: ")
password = input("Password: ")
print("Black Desert Online Account Checker Coded By The Jolly Roger")

def check():
    post = {"email": email, "password": password}
    login = requests.post(url, data=post)
    if login.text == "<Response [200]>":
        print("Account is Working!")
    else:
        print("Not Working")


check()
