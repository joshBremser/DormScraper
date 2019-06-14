#Python program to scrape names/dorm rooms from mainestreet

#Used to make a firefox browser
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary		

#Used to send keypresses to the browser
from selenium.webdriver.common.keys import Keys 
import time
import sys
import os

UMS_ID = 
UMS_PASSWORD = 
SPEED_CONSTANT = .2 #Number of seconds to wait for page redirection
HEADLESS = True

#Rooms
startingurl = 'https://mainestreetcs.maine.edu/psp/CSPRD_1/EMPLOYEE/HRMS/c/RES_LIFE.RL_SS_ROOM_STAFF.GBL?Page=RL_SS_ROOM_DTL&Action=U&CAMPUS=USM&INSTITUTION=UMS06&RL_QUAD_CD=GORHAM&RL_BLDG_CD=PHILIPPI&STRM=2010'


#Setup
binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
browser = webdriver.Firefox()
f = open("information.txt","w+")

#UMS Login Page

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
for room in range(100,330):
    f.write("\n")
    if (( room % 100 ) > 30 ):
        room = room + 70
    fs = '';
    if ((room/100) == 1):
        fs += '1F_'
    elif ((room/100) == 2):
        fs += '2F_'
    elif ((room/100) == 3):
        fs += '3F_'
    if ((room % 100) < 16):
        fs += '1S'
    else:
        fs += '2S'
    browser.get(startingurl + '&RL_ROOM_CD=' + str(room) + '&RL_FLOOR_CD=' + fs)
    time.sleep(SPEED_CONSTANT)
    try:
        browser.switch_to.frame('ptifrmtgtframe')
        browser.execute_script("document.getElementById('RL_OCCUPANTS$hviewall$0').click()")
        time.sleep(SPEED_CONSTANT)
        f.write(browser.find_element_by_id('RL_ROOM_TRM_VW_DESCR').text)
        for x in range(0,5):
            personid = 'NAME1$span$' + str(x)
            element = browser.find_element_by_id(personid)
            f.write('\t' + element.text)
    except:
        print ''
    

f.close()
