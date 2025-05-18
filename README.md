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

| Title                       | Price        | Details | Location                 | Posted Time | Link                                                                                                                   |
|-----------------------------|--------------|---------|--------------------------|-------------|------------------------------------------------------------------------------------------------------------------------|
| `Car Cover and Power Steering pump` | `₹ 5,500.00`  |         | `PARDHASARDI NAGAR, MANDAPETA` | `TODAY`      | [View Listing](https://www.olx.in/item/spare-parts-c1585-other-spare-parts-in-pardhasardi-nagar-mandapeta-iid-1807070098) |
| `new car cover`              | `₹ 2,000.00` |         | `KISHANPURA, WARANGAL`   | `TODAY`      | [View Listing](https://www.olx.in/item/spare-parts-c1585-other-spare-parts-in-kishanpura-warangal-iid-1807295554)        |




