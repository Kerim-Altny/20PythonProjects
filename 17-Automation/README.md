# Kick VOD Scraper 🎥

A lightweight Python automation tool that uses Selenium to extract Video on Demand (VOD) data from Kick.com. 

## Features
* **Dynamic Content Handling:** Automatically scrolls the page to trigger lazy-loaded VOD elements.
* **Anti-Bot Evasion:** Configured with specific Chrome options to bypass basic automated software detections.
* **Clean Data Extraction:** Parses dynamic web elements to extract video titles, durations, and valid URLs into a structured JSON file.
* **CLI Integration:** Dynamically accepts the target streamer's username via command-line arguments (`sys.argv`).

## Prerequisites
* Python 3.x
* Google Chrome
* Selenium WebDriver

## Installation & Usage

1. Install the required dependency:
   ```bash
   pip install selenium
2. Run the scraper by passing the target streamer's username as an argument:

   ```Bash
   python vod_scraper.py <streamer_username>

Example:

   ```Bash
   python vod_scraper.py xqc