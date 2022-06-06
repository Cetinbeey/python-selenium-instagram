from cgitb import text
import time
from  selenium import webdriver 
from selenium.webdriver.common.keys import Keys
# from instagraminfo import username,password
username=""
password=""



class instagram:
    def __init__(self,username,password):
        self.username=username
        self.passwrod=password
        self.browser=webdriver.Safari()
        
    def singIn(self):
        login=self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        usernameInput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        

        passwordInput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.passwrod)
        passwordInput.send_keys(Keys.ENTER)
        
        
        
        # wiews=self.browser.find_element_by_xpath("//*[@id='loginForm']/div[1]/div[2]/div/div")
        # wiews.click()
        # time.sleep(2)     -->> şifre göster/gizle butonu etkileşimi 
        # wiews.click()
        
        
        
    
insta=instagram(username,password)
insta.singIn()










