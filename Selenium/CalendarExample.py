from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto import keyboard
import time
import os
import datetime


class calenderClass():
    def CalenderOperation(self):
        driver = None
        try:
            userInputDate = input("Enter the travel date in DD-MM-YYYY format \n")

            if calenderClass().DateValidation(userInputDate) != 0:
                # DateValidation() returns 3 variables and is assigned to respective variables
                EnteredYear, EnteredMonth, EnteredDate = calenderClass().DateValidation(userInputDate)

                # this is because in html code of expedia, the month is always Actual month -1
                # i.e if month of sept is 9 then in html code it will be written as 8.
                NewMonth = EnteredMonth - 1

            driver = webdriver.Firefox(executable_path=os.getcwd() + "//drivers//geckodriver.exe")
            driver.get("https://www.expedia.co.in/")
            driver.maximize_window()
            time.sleep(1)

            # destination Field
            InputDestination = driver.find_element(By.NAME, "destination")
            InputDestination.send_keys("Goa, India")
            keyboard.send_keys("{TAB}")  # Keyboard action using pywinAuto module.
            time.sleep(2)

            # Clicking on check-in date
            CheckInField = driver.find_element(By.ID, "hotel-checkin-hp-hotel")
            CheckInField.click()

            # Selecting the check-in date
            CheckInDateXpath = "//div[@class= 'datepicker-cal-month']//*[contains(@data-year, '" + str(
                EnteredYear) + "') and  contains(@data-month,'" + str(NewMonth) + "') and contains(@data-day, '" + str(
                EnteredDate) + "')]"
            CheckInDate = driver.find_element(By.XPATH, CheckInDateXpath)
            CheckInDate.click()
            driver.get_screenshot_as_file(os.getcwd()+"/ScreenShots/CalendarExample.png")
            time.sleep(4)

        except Exception as e:
            print(str(e))

        finally:
            if driver is not None:
                driver.close()


    def DateValidation(self, traveldate):

        dateSplit = traveldate.split("-")
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
            raise Exception("Entered date is not valid. Date should be greater than or equal to current date")
            return 0


obj = calenderClass()
obj.CalenderOperation()
# obj.DateValidation()
