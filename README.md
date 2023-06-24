
# Transfermarkt-Scrape-22/23-season

A data scraping project focused on extracting transfer information from Transfermarkt for the 2022/2023 seasons using python and selenium. The project aims to analyze club activities in the transfer market, identifying instances of overpaid and bargain signings. By leveraging web scraping techniques, this project provides valuable insights into the financial aspects of football transfers, enabling a better understanding of clubs' spending patterns during the specified seasons.  Furthermore, the extracted data is seamlessly visualized using Tableau, a powerful data visualization tool. 

## Tableau Dashboard
Here's the link to the Tableau Dashboard for the scraped data: 
[Transfermarkt Tableau Dashboard](https://public.tableau.com/app/profile/farhan.hasin.saad/viz/TransfermarktSeason2223DataVisualization/Sheet1#1) (7 Sheets)

## CSV File (Data Example):
| Name          | Age | Position           | Player Nationality | Market Value | Club      | League         | League Country | Transfer Type | Fee   |
|---------------|-----|--------------------|--------------------|--------------|-----------|----------------|----------------|---------------|-------|
| Casemiro      | 30  | Defensive Midfield | Brazil             | 40           | Man Utd   | Premier League | England        | Permanent     | 70.65 |
| Romelu Lukaku | 29  | Centre-Forward     | Belgium            | 70           | Inter     | Serie A        | Italy          | Loan          |       |
| Jules Kounde | 23  | Centre-Back        | France             | 60           | Barcelona | LaLiga         | Spain          | Permanent     | 50    |

## Findings and Observations from the Dashboard
1. Chelsea FC of England spent the most in this transfer window almost €600m. Their most expensive player was Enzo Fernandez.
2. Premier League of England had the most business in this transfer window with 138 incomings averaging transfer fee €21.98m per player and €3.3b in total.
3. The players age has relation with their transfer fee, market value and their movement in the market. Players within the age of (21-25) have the most demand.
4. The most popular position were Center Forward with 386 total bought of this position. 2nd were Center Back.
5. In terms of nationality Latin American players were very demanding in this transfer window. Brazil had 97 players in the transfer window signing for various clubs. 
6. Europes top 5 league had two signings that stood out from the rest of them in the scatterplot. Erling Haaland (As a bargain €90m less than the market price) and Enzo Fernandez (Most overpaid with €66m paid more than the market price).



## Run Locally

1. Clone the repository

```bash
  git clone https://github.com/saadism777/Transfermarkt-Scraping
```

2. Go to the project directory

```bash
  cd Transfermarkt-Scraping
```
3. Initialize and activate Virtual Environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```

4. Install dependencies

```bash
  pip install -r requirements.txt
```
5. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads

6. Run the scrapper: 
```bash
python scraper.py --chromedriver_path <path_to_chromedriver>
```
7. The csv file named 'transfermarkt.csv' will be generated within the project directory.
