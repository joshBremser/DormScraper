#Python program to scrape names/dorm rooms from mainestreet

#Used to make a firefox browser
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#Used to send keypresses to the browser
from selenium.webdriver.common.keys import Keys 
#from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import os

UMS_ID = 'username' #Your Brandeis username from environment variable
UMS_PASSWORD = 'password'    #Your Brandeis password from environment variable
SPEED_CONSTANT = 1                    #Number of seconds to wait for page redirection
HEADLESS = True

def get_stuff():
    #Setup
    binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    browser = webdriver.Firefox()


    #Sage Login Page

    browser.get('https://identity.maine.edu/cas/login' )

    #Acquiring Signin Elements

    userid = browser.find_element_by_id('username')

    pwd = browser.find_element_by_id('password')

    #Signing In

    userid.send_keys(UMS_ID)

    pwd.send_keys(UMS_PASSWORD + Keys.RETURN)

    #Waiting for page to load

    time.sleep(SPEED_CONSTANT)
    browser.get('https://mycampus.maine.edu/group/usm/home/-/launcher/fire/3937066')
    time.sleep(SPEED_CONSTANT)
    browser.get('https://mainestreetcs.maine.edu/psp/CSPRD_1/EMPLOYEE/HRMS/c/RES_LIFE.RL_SS_ROOM_STAFF.GBL?Page=RL_SS_ROOM_DTL&Action=U&CAMPUS=USM&INSTITUTION=UMS06&RL_BLDG_CD=PHILIPPI&RL_FLOOR_CD=1F_1S&RL_QUAD_CD=GORHAM&RL_ROOM_CD=104&STRM=1910')

    
    return something

if __name__ == '__main__':
    print (get_stuff())
