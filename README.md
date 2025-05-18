# Olx-Scrapper
A Python-based web scraper that extracts listings from OLX using Selenium. The script is designed to dynamically load more listings by interacting with the "Load More" button and collect desired data for further use or analysis.

##  Features

- Automatically scrolls and loads OLX listings.
- Clicks the "Load More" button until a specified number of listings are loaded.
- Extracts data such as title, price, location, and date posted.
- Saves output as a CSV file.
- Error handling for page load, element click interception, and timeout issues.

##  Requirements

- Python 3.7+
- Google Chrome installed
- ChromeDriver (compatible with your Chrome version)

##  Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/olx-scraper.git
   cd olx-scraper
   ```
2. **Install required Python packages
   ```bash
   pip install -r requirements.txt
   ```

##  Usage

   ```bash
   python olx.py
   ```
   You can configure:
   - target_count – how many listings to scrape
   - OLX URL (modify inside the script)
     
   Scraped data will be saved in a CSV file (output.csv by default).


## 📂 Output Sample

| Title                                                     | Price          | Details                     | Location               | Posted Time | Link                                                                                                                            |
|-----------------------------------------------------------|----------------|-----------------------------|------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------|
| `107 Gaj home with covered car parking near by main market` | `₹ 45,00,000.00` | `2 Bds - 1 Ba - 900 ft²`     | `JAWAHAR COLONY, FARIDABAD` | `APR 26`    | [View Listing](https://www.olx.in/item/for-sale-houses-apartments-c1725-2-bhk-houses-villas-900-sq-ft-in-jawahar-colony-faridabad-iid-1789276286) |
| `2BHK Flat at shivane with covered car parking Brand new condition` | `₹ 37,99,000.00` | `2 BHK - 2 Bathroom - 1100 sqft` | `SHIVANE, PUNE`          | `3 DAYS AGO` | [View Listing](https://www.olx.in/item/for-sale-houses-apartments-c1725-2-bhk-apartments-1100-sq-ft-in-shivane-pune-iid-1803879123)                |





