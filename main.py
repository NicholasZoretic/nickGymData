#import requests
#from bs4 import BeautifulSoup
from selenium import webdriver
import time

def getData():
    URL = "https://recwell.wisc.edu/nick/"
    path = r'C:\\Users\nickr\\Documents\\geckodriver-v0.29.1-win64\\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=path)
    driver.get(URL) 
    #page = requests.get(URL, timeout=(5, 10))
    time.sleep(3)
    #soup = BeautifulSoup(page.content, "html.parser")
    tracker_elements = driver.find_elements_by_class_name('tracker-count-wrapper')
    values = [element.text[:-5] for element in tracker_elements[:4]]
    #trackers = soup.find_all("span", class_="tracker-current-count pending")
    driver.close()
    return values
def main():
    #time.sleep(10)
    print(getData())

if __name__ == "__main__":
    main()
