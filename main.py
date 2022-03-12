import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/Users/luiscaceres/Documents/ChromeDriver')

driver.get('https://bokapass.nemoq.se/Booking/Booking/Index/halland');

target_month = ['mar','apr']
target_day = 6


def get_times():
    driver.find_element_by_class_name('btn-primary').click()
    driver.find_element_by_id('AcceptInformationStorage').click()
    select = Select(driver.find_element_by_id('NumberOfPeople'))
    select.select_by_value('2')
    driver.find_element_by_class_name('btn-primary').click()
    driver.find_element_by_id('ServiceCategoryCustomers_0__ServiceCategoryId').click()
    driver.find_element_by_id('ServiceCategoryCustomers_1__ServiceCategoryId').click()
    driver.find_element_by_class_name('btn-primary').click()
    driver.find_element_by_name('TimeSearchFirstAvailableButton').click()

def output_dates():
    dates2 = driver.find_element_by_id('dateText')
    return(dates2.text)


def checkpasstimes():
    nextDate = output_dates().split()
    month = nextDate[1]
    day = nextDate[0]

    if month not in target_month:
        print(f'The next available date is {month}, {day}')
        driver.quit()
    else:
        if month == 'mar':
            print("Get the date!")
        else:
            if day < 6:
                print("Get the date!")
            else:
                print(f'The next available date is {month, day}')
                driver.quit()



get_times()
checkpasstimes()

time.sleep(3)
driver.quit()
