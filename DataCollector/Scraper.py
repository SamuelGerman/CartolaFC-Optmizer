from selenium import webdriver
from selenium.webdriver.common.by import By

class Scraper:
    BRASILEIRAO_URL = "https://www.sofascore.com/tournament/football/brazil/brasileirao-serie-a/325#id:58766"
    clubs_urls = []
    driver = webdriver.Chrome()
    
    @staticmethod
    def getBrasileiraoClubsURLs():
        Scraper.driver.get("https://www.sofascore.com/tournament/football/brazil/brasileirao-serie-a/325#id:58766")
        elements = Scraper.driver.find_elements(By.XPATH, '//a[@data-testid="standings_row"]')
        for element in elements:
            Scraper.clubs_urls.append(element.get_attribute("href"))
        






#driver.get(SOFASCORE_URL)



