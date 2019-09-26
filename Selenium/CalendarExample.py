from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto import keyboard
import time
import os
import datetime


class calenderClass():
    def Calenderoperation(self):
        try:
            userinputDate = input("Enter the travel date in DD-MM-YYYY format \n")
            if calenderClass().DateValidation(userinputDate) != 0:
                # DateValidation returns 3 variables and is assigned to respective variables
                EnteredYear, EnteredMonth, EnteredDate = calenderClass().DateValidation(userinputDate)
                print(EnteredYear)
                print(EnteredMonth)
                print(EnteredDate)

            driver = webdriver.Firefox(executable_path=os.getcwd()+"//drivers//geckodriver.exe")
            driver.get("https://www.expedia.co.in/")
            time.sleep(1)
            # destination Field
            InputDestination = driver.find_element(By.NAME, "destination")
            InputDestination.send_keys("Goa, India")
            keyboard.send_keys("{TAB}")
            time.sleep(2)
            CheckIn = driver.find_element(By.ID, "hotel-checkin-hp-hotel")
            CheckIn.click()
            time.sleep(1)




        except Exception as e:
            print(str(e))


    def DateValidation(self, travelDate):

        dateSplit = travelDate.split("-")
        timeFormat = time.localtime()

        # Current date Split
        Year = timeFormat[0]
        month = timeFormat[1]
        date = timeFormat[2]

        # user data Split
        EnteredYear = int(dateSplit[2])
        EnteredMonth = int(dateSplit[1])
        EnteredDate = int(dateSplit[0])

        currentDate = datetime.datetime(Year, month, date)
        UserDate = datetime.datetime(EnteredYear, EnteredMonth, EnteredDate)
        if UserDate >= currentDate:
            return EnteredYear, EnteredMonth, EnteredDate
        else:
            raise Exception("Entered date is not valid")
            return 0




obj = calenderClass()
obj.Calenderoperation()
#obj.DateValidation()