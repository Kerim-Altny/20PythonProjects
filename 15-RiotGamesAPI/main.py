from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import requests
import os 
from dotenv import load_dotenv 

load_dotenv()

app = FastAPI(title="Riot Games Statistics Platform")
templates = Jinja2Templates(directory="templates")

API_KEY = os.getenv("RIOT_API_KEY")



@app.get("/", response_class=HTMLResponse)
def home_page(request: Request, error: str = None):
    """Landing page when the user visits the site"""
    return templates.TemplateResponse("index.html", {"request": request, "error": error})



@app.get("/player/{region}/{game_name}/{tag_line}")
def get_player_puuid_and_redirect(region: str, game_name: str, tag_line: str):
    print(f"🔍 Searching for account {game_name}#{tag_line}...")
    
    
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {"X-Riot-Token": API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        puuid = data["puuid"]
        print(f"✅ Account found! PUUID: {puuid[:15]}... Redirecting!")
        target_url = f"/profile/{region}/{puuid}"
        return RedirectResponse(url=target_url)
    else:
        return RedirectResponse(url="/?error=not_found")



@app.get("/profile/{region}/{puuid}", response_class=HTMLResponse)
def get_profile_and_matches(request: Request, region: str, puuid: str):
    """
    Fetches both summoner information and stats for the last 5 matches.
    """
    headers = {"X-Riot-Token": API_KEY}
    
   
    summoner_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    sum_response = requests.get(summoner_url, headers=headers)
    
    if sum_response.status_code != 200:
        raise HTTPException(status_code=sum_response.status_code, detail="Could not fetch summoner info.")
        
    sum_data = sum_response.json()
    level = sum_data.get("summonerLevel", "Unknown")
    icon_id = sum_data.get("profileIconId", 1)

   
    continent_server = "europe" 
    match_ids_url = f"https://{continent_server}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=5"
    match_ids_response = requests.get(match_ids_url, headers=headers)
    
    match_list = []
    
    
    if match_ids_response.status_code == 200:
        match_ids = match_ids_response.json()
        
     
        for match_id in match_ids:
            match_detail_url = f"https://{continent_server}.api.riotgames.com/lol/match/v5/matches/{match_id}"
            match_detail_response = requests.get(match_detail_url, headers=headers)
            
            if match_detail_response.status_code == 200:
                match_data = match_detail_response.json()
                
               
                for participant in match_data["info"]["participants"]:
                    if participant["puuid"] == puuid:
                        match_list.append({
                            "game_mode": match_data["info"]["gameMode"],
                            "champion": participant["championName"],
                            "kda": f"{participant['kills']} / {participant['deaths']} / {participant['assists']}",
                            "result": "Victory" if participant["win"] else "Defeat",
                            "damage": participant["totalDamageDealtToChampions"]
                        })
                        break 

 
    return templates.TemplateResponse(
        request=request, 
        name="profile.html", 
        context={
            "level": level,
            "icon_id": icon_id,
            "matches": match_list
        }
    )