from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import csv
import os
import time

# Configuration
URL = "https://www.olx.in/items/q-car-cover"
OUTPUT_DIR = "scraped_data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "items.csv")

# CSS Selectors
LISTING_SELECTOR = "li[data-aut-id='itemBox3']"
TITLE_SELECTOR   = "div.fTZT3 span[data-aut-id='itemTitle']"
PRICE_SELECTOR   = "div.fTZT3 span[data-aut-id='itemPrice']"
DETAILS_SELECTOR = "div.fTZT3 span[data-aut-id='itemDetails']"
LOCATION_SELECTOR = "div._3rmDx span._2VQu4"
TIME_SELECTOR = "div._3rmDx span._2jcGx span"

def wait_for_element(parent, by, selector, timeout=5):
    ignored = (NoSuchElementException, StaleElementReferenceException)
    return WebDriverWait(parent, timeout, ignored_exceptions=ignored) \
        .until(EC.presence_of_element_located((by, selector)))

def safe_get_text(element, by, selector):
    try:
        return element.find_element(by, selector).text.strip()
    except NoSuchElementException:
        return ""

def load_until_target(driver, target_count):
    from selenium.webdriver.common.action_chains import ActionChains

    while True:
        listings = driver.find_elements(By.CSS_SELECTOR, LISTING_SELECTOR)
        if len(listings) >= target_count:
            break

        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-aut-id='btnLoadMore']"))
            )

            # Scroll into view
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", load_more_button)
            time.sleep(0.5)  # Let page settle

            # Ensure the button is clickable
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-aut-id='btnLoadMore']"))
            )

            # Click using JavaScript to avoid interception
            driver.execute_script("arguments[0].click();", load_more_button)
            time.sleep(2)

        except TimeoutException:
            print("Timeout while waiting for Load More button.")
            break
        except Exception as e:
            print(f"Exception during load more: {e}")
            break

def main():
    target_count = int(input("Enter number of listings to scrape: "))

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get(URL)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-aut-id='itemsList1']"))
        )

        load_until_target(driver, target_count)

        listings = driver.find_elements(By.CSS_SELECTOR, LISTING_SELECTOR)
        total = len(listings)
        print(f"Ready to scrape {min(target_count, total)} items")

        data = []
        for i in range(min(target_count, total)):
            for attempt in range(3):
                try:
                    listings = driver.find_elements(By.CSS_SELECTOR, LISTING_SELECTOR)
                    listing = listings[i]

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block: 'center'});", listing
                    )
                    time.sleep(0.3)

                    title = wait_for_element(listing, By.CSS_SELECTOR, TITLE_SELECTOR).text
                    price = wait_for_element(listing, By.CSS_SELECTOR, PRICE_SELECTOR).text
                    details = safe_get_text(listing, By.CSS_SELECTOR, DETAILS_SELECTOR)
                    location = safe_get_text(listing, By.CSS_SELECTOR, LOCATION_SELECTOR)
                    posted_time = safe_get_text(listing, By.CSS_SELECTOR, TIME_SELECTOR)
                    link = listing.find_element(By.TAG_NAME, "a").get_attribute("href")

                    data.append([title, price, details, location, posted_time, link])
                    print(f"{i+1}: {title} | {price} | {details} | {location} | {posted_time} | {link}")
                    break

                except (StaleElementReferenceException, TimeoutException) as e:
                    print(f"Retry {attempt+1} for item {i+1} due to: {e}")
                    time.sleep(0.5)
                except Exception as e:
                    print(f"Skipped item {i+1} due to unexpected error: {e}")
                    break

        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Price', 'Details', 'Location', 'Posted Time', 'Link'])
            writer.writerows(data)

        print(f"Saved {len(data)}/{target_count} listings to {OUTPUT_FILE}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
