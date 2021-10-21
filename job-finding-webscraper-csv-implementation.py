from typing import final
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Finds the path to my Chromedriver, we will interact with this a lot
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#The console throws a lot of stuff at us so this will give it time to throw us the stuff
#Then we clear it so that the user can see their options
time.sleep(3)
clear = lambda: os.system("cls")
clear()

#Allows the user to input what type of job they are searching for
searchTerm = input("What job would you like to search for? ")
#searchTerm = "graduate software developer"

#Create empty arrays of each of the types of data we want to collect about the job so we can append to them later
jobTitles = []
jobEmployers = []
jobLinks = []

def indeedCollection():
    #Go to this website
    driver.get("https://uk.indeed.com/?from=gnav-jobsearch--jasx")

    #Find the text box and enter the type of job the user entered earlier
    search = driver.find_element_by_id("text-input-what")
    search.send_keys(searchTerm)
    search.send_keys(Keys.RETURN)

    #Try to locate the id mentioned below, if it is not found within 10 seconds then close the program
    try:
        jobCards = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mosaic-provider-jobcards"))
        )

        #Formatting to make the terminal easier on the eyes
        jobTitles.append(" ----- ")
        jobEmployers.append(" ----- ")
        jobLinks.append(" ----- ")
        jobTitles.append("Indeed")
        jobEmployers.append("Indeed")
        jobLinks.append("Indeed")

        #Collects all of the job titles on the page
        elements = jobCards.find_elements_by_tag_name("span")
        for x in elements:
            val = x.get_attribute("title")
            #Make sure that the empty values aren't shown
            if not len(val.strip()) == 0:
                jobTitles.append(val)

        #Collects all of the employers for the jobs
        elements = jobCards.find_elements_by_class_name("companyName")
        for x in elements:
            val = x.text
            jobEmployers.append(val)

        #Collects all of the job links
        elements = jobCards.find_elements_by_class_name("tapItem")
        for x in elements:
            val = x.get_attribute("href")
            jobLinks.append(val)

    #After everything has been done close the program
    finally:
        #driver.quit()
        pass

def govCollection():
    #Go to this website
    driver.get("https://findajob.dwp.gov.uk/")

    #Find the text box and enter the type of job the user entered earlier
    search = driver.find_element_by_id("what")
    search.send_keys(searchTerm)
    search.send_keys(Keys.RETURN)

    try:
        jobCards = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main"))
        )

        #Formatting to make the terminal easier on the eyes
        jobTitles.append(" ----- ")
        jobEmployers.append(" ----- ")
        jobLinks.append(" ----- ")
        jobTitles.append("Gov")
        jobEmployers.append("Gov")
        jobLinks.append("Gov")

        #Collects all of the job titles on the page
        elements = jobCards.find_elements_by_class_name("search-result")
        for x in elements:
            val = x.find_element_by_tag_name("a").text
            jobTitles.append(val)

        #Collects all of the employers for the jobs
        elements = jobCards.find_elements_by_class_name("search-result")
        for x in elements:
            val = x.find_element_by_tag_name("strong").text
            jobEmployers.append(val)

        #Collects all of the job links
        elements = jobCards.find_elements_by_class_name("search-result")
        for x in elements:
            val = x.find_element_by_tag_name("a").get_attribute("href")
            jobLinks.append(val)

    finally:
        #quit()
        pass

def reedCollection():
    #Go to this website
    driver.get("https://www.reed.co.uk/")

    #Find the text box and enter the type of job the user entered earlier
    search = driver.find_element_by_id("main-keywords")
    search.send_keys(searchTerm)
    search.send_keys(Keys.RETURN)

    #Try to locate the id mentioned below, if it is not found within 10 seconds then close the program
    try:
        jobCards = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "server-results"))
        )

        #Formatting to make the terminal easier on the eyes
        jobTitles.append(" ----- ")
        jobEmployers.append(" ----- ")
        jobLinks.append(" ----- ")
        jobTitles.append("reed")
        jobEmployers.append("reed")
        jobLinks.append("reed")

        #Collects all of the job titles on the page
        elements = jobCards.find_elements_by_class_name("title")
        for x in elements:
            val = x.text
            jobTitles.append(val)

        #Collects all of the employers for the jobs
        elements = jobCards.find_elements_by_class_name("gtmJobListingPostedBy")
        for x in elements:
            val = x.text
            jobEmployers.append(val)

        #Collects all of the job links
        elements = jobCards.find_elements_by_class_name("job-block-link")
        for x in elements:
            val = x.get_attribute("href")
            jobLinks.append(val)

    #After everything has been done close the program
    finally:
        #driver.quit()
        pass

def printValues():
    #Clears the terminal
    clear()

    #Prints all of the job titles, employers and links respectively
    for i in range(len(jobTitles)):
        print("")
        print("jobTitles: " + jobTitles[i])
        print("jobEmployer: " + jobEmployers[i])
        print("jobLink: " + jobLinks[i])


#Maybe implement an option to input which websites you would like to use
indeedCollection()
govCollection()
reedCollection()

printValues()
driver.quit()