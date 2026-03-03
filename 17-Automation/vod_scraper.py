import json
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_browser():
    """Configures and returns a Chrome browser instance with basic anti-bot measures."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    return webdriver.Chrome(options=options)


def scroll_page(driver, scrolls=4):
    """Scrolls down the page to trigger lazy-loaded video items."""
    print(f"[*] Scrolling the page {scrolls} times to load older VODs...")
    for _ in range(scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


def scrape_kick_vods(streamer_username):
    """Main function to scrape VODs and save them to a JSON file."""
    print(f"[*] Starting scraper for: {streamer_username}")

    driver = setup_browser()
    url = f"https://kick.com/{streamer_username}/videos"

    try:
        driver.get(url)
        time.sleep(5)

        scroll_page(driver, scrolls=4)

        print("[*] Extracting video elements...")

        video_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/videos/']")

        vod_dict={}

        for link in video_links:
            href = link.get_attribute("href")
            text = link.text.strip()

            if not href or not text:
                continue

            if href not in vod_dict:
                vod_dict[href] = {"url": href, "title": "Unknown Title", "duration": "N/A"}

            lines = text.split('\n')

            if len(lines) >= 2 or (":" in lines[0] and len(lines[0]) <= 8):
                vod_dict[href]["duration"] = lines[0]
            else:
                vod_dict[href]["title"] = text

        vod_list = []
        for idx, data in enumerate(vod_dict.values()):
            data["id"] = idx + 1
            vod_list.append(data)


        filename = f"{streamer_username}_vods.json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(vod_list, file, indent=4, ensure_ascii=False)

        print(f"[+] Success! Saved {len(vod_list)} unique VODs to {filename}")

    except Exception as e:
        print(f"[!] An error occurred during scraping: {e}")

    finally:
        print("[*] Closing the browser...")
        driver.quit()


if __name__ == "__main__":

    target_streamer = sys.argv[1]
    scrape_kick_vods(target_streamer)