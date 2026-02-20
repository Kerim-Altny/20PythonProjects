import requests
from bs4 import BeautifulSoup
import csv

def scrape_steam_topsellers():
    url = 'https://store.steampowered.com/search/?filter=topsellers'


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    print("🌐 Connecting to Steam servers...")
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Error: Could not reach the server. Status Code: {response.status_code}")
        return
    
    soup= BeautifulSoup(response.text, 'html.parser')
    games_data = []
    game_rows= soup.find_all('a', class_='search_result_row')
    print(f"🎮 Found {len(game_rows)} games on the page, extracting data...")
    
    for game in game_rows:
        title = game.find('span', class_='title').text.strip()
        release_date = game.find('div', class_='search_released responsive_secondrow').text.strip()
        price_elem = game.find('div', class_='discount_final_price')
        if not price_elem:
            price_elem = game.find('div', class_='search_price')
        
        price = price_elem.text.strip() if price_elem else 'Free'
        
        link = game.get('href', '')
        
        games_data.append([title, release_date, price, link])

        csv_filename = 'steam_top_sellers.csv'
        print(f"💾 Compiling data and saving to '{csv_filename}'...")

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Release Date', 'Price', 'Link'])  
            writer.writerows(games_data)
            
            print(f"✅ Process complete! Your file '{csv_filename}' is ready to be opened.")

if __name__ == '__main__':
    scrape_steam_topsellers()