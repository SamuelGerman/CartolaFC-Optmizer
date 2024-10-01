from DataCollector.CartolaAPI import CartolaAPI
from DataCollector.Scraper import Scraper

Scraper = Scraper()
Scraper.getBrasileiraoClubsURLs()
print (Scraper.clubs_urls)