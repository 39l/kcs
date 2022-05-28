from bs4 import BeautifulSoup
import requests
import argparse
import pandas as pd
import tabulate
import os
import time
import keyboard


#parser = argparse.ArgumentParser()
#parser.parse_args()
#parser.add_argument("r", help='') 
#args = parser.parse_args()	
os.system('clear')
def s():
    print('############\n## Search ##\n##  Help  ##\n##  Quit  ##\n############\t\t\n')
    x = input('> ')
    if x == 's':
        os.system('clear')
        search()
    elif x == 'h':
        os.system('clear')
    elif x == 'q':
        os.system('clear')
        quit()


def search():
    print(' ############ \n ## Search ## \n ############\n')
    s = input(' > ')
    for page in range(1, 99):
        page = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw='+ s + '&_sop=20&_pgn=' + str(page))
        #pageA = requests.get('https://seattle.craigslist.org/search/sss?query=' + sRCH)


        soup = BeautifulSoup(page.text, 'html.parser')
        name = soup.find_all('span', class_='BOLD') 
        price = soup.find_all('span', class_='s-item__price')
        year = soup.find_all('span', class_='s-item__dynamic s-item__dynamicAttributes1')
        mileage = soup.find_all('span', class_='s-item__dynamic s-item__dynamicAttributes2')
        #seller = soup.find_all('span', class_='s-item__seller-info-text')


        df = pd.DataFrame(list(zip(name,price,year,mileage)))
        print(df)

        


def menu():
    print(' ############ \n ## Search ## \n ##  Help  ## \n ##  Quit  ## \n ############\t\t\n')
    x = input(' > ')
    if x == 's':
        os.system('clear')
        search()
    elif x == 'h':
        os.system('clear')
    elif x == 'q':
        os.system('clear')
        quit()
        
menu()

        