from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import argparse
import pandas as pd

# path parser for the chrome driver
parser = argparse.ArgumentParser()
parser.add_argument('--chromedriver_path', type=str, help="Check where the Chromedriver is in your PC and share the path")
args = parser.parse_args()
webdriver_path = "D:\chromedriver.exe"
# webdriver_path = args.chromedriver_path

# columns for the csv file
columns = ["Name", "Age", "Position", "Player Nationality","Market Value", "Club", "League", "League Country","Transfer Type","Fee"]

# Loading chromedriver
chromeOptions = Options()
chromeOptions.headless = False
driver = webdriver.Chrome(webdriver_path, options=chromeOptions)
wait = WebDriverWait(driver, 10)

# Function to scrape the data
def main(): 
    accept_cookie = True
    player_data = []
    for page_id in range(1,81):
        url = f"https://www.transfermarkt.com/transfers/saisontransfers/statistik/top/ajax/yw0/saison_id/2022/transferfenster/alle/land_id//ausrichtung//spielerposition_id//altersklasse//leihe//plus/0/galerie/0/page/{page_id}"
        driver.get(url)
        # Handle the cookie for the first load. [clicks accept button]
        if accept_cookie:
            print("Waiting for cookie.....")
            time.sleep(5)
            # Switch to the iframe
            iframe_id = "sp_message_iframe_764226"  
            driver.switch_to.frame(iframe_id)
            cookie_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.sp_choice_type_11')))
            #cookie_popup = driver.find_element(By.CSS_SELECTOR,'.sp_choice_type_11')
            cookie_popup.click()
            print("Cookie Accepted!")
            accept_cookie = False
        
        # Scrape the data
        rankings = driver.find_element(By.ID,'yw0')
        rows = rankings.find_elements(By.CSS_SELECTOR, '.odd, .even')
        # Printing scrape status [pages traversed]
        print(f"Page: {page_id} Done.")
        
        # Creating and populating the csv file
        for index,row in enumerate(rows):
            player_data.append(get_player_details(row))
        df = pd.DataFrame(data=player_data, columns=columns)
        df.to_csv("transfermarkt.csv", index=False)
    driver.close()

# Function to get the player details
def get_player_details(row):
    details = row.text.split('\n')
    contents = {}
    contents["Name"] = details[1].encode('utf-8').decode('utf-8')
    contents["Position"] = details[2]  
    contents["Age"] = int(details[3].split(' ')[0])
    market_value = details[3].split(' ')[1]
    contents["Market Value"] = extract_numerical_value(market_value)
    contents["Club"] = details[4].encode('utf-8').decode('utf-8')
    contents["League"] = details[5].encode('utf-8').decode('utf-8')
    fee = details[6]
    contents["Fee"] = numerical_value_and_transfer_category(fee,contents)
    country_flags = row.find_elements(By.CSS_SELECTOR, 'img.flaggenrahmen')
    nationality = country_flags[0].get_attribute('title')
    contents["Player Nationality"] = nationality
    contents["League Country"] = country_flags[-1].get_attribute('title')
    return contents

# Function to extract the numerical value
def extract_numerical_value(value):
    numerical_part = ''.join(filter(str.isdigit, value))
    if numerical_part:
        return float(numerical_part)/100
    else:
        return None  # or assign a default value, e.g., 0

# Function to extract the numerical value and transfer category
def numerical_value_and_transfer_category(value,contents):
    numerical_part = ''.join(filter(str.isdigit, value))
    value = value.lower()
    if numerical_part:
        contents["Transfer Type"] = "Permanent"
        return float(numerical_part)/100
    else:
        if 'loan' in value:
            contents["Transfer Type"] = "Loan"
            return None
        elif value == 'free transfer':
            contents["Transfer Type"] = "Free"
            return None
        else:
            contents["Transfer Type"] = "Unknown"
            return None

if __name__ == "__main__":
    main()