# 🐍 20 Python Projects

> **Note:** Some of these projects were completed with the assistance of AI.

A collection of **19 Python projects** built while following the [100 Days of Code™: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu on Udemy. These projects cover a wide range of topics — from GUI applications and games to web development, automation, APIs, and data science.

---

## 📂 Projects Overview

| # | Project | Tech Stack | Description |
|---|---------|------------|-------------|
| 01 | [Morse Code Converter](./01-MorseCodeProject) | Python | Text to Morse code converter via the command line |
| 02 | [Portfolio Website](./02-PortfolioWebsiteProject) | Flask, HTML | A personal portfolio website built with Flask and Jinja templates |
| 03 | [Tic Tac Toe](./03-TicTacToe) | Python, Turtle | Classic Tic Tac Toe game with ASCII art |
| 04 | [Image Watermark](./04-ImageWatermark) | Python, Tkinter | Desktop app to add watermarks to images |
| 05 | [Typing Speed Test](./05-TypingSpeed) | Python, Tkinter | Measure your typing speed (WPM) with a GUI application |
| 06 | [Breakout Game](./06-BreakoutGame) | Python, Turtle | Classic Breakout arcade game with paddle, ball, and bricks |
| 07 | [Cafe & Wifi](./07-Cafe%26Wifi) | Flask, SQLite, HTML/CSS | Web app to browse and add cafes with wifi and power socket ratings |
| 08 | [Todo List](./08-TodoList) | Flask, SQLite, HTML/CSS | A simple web-based to-do list application |
| 09 | [Disappearing Text](./09-DisappearingText) | Python, Tkinter | A writing app where your text disappears if you stop typing |
| 10 | [PDF to Audiobook](./10-PdfToAudiobook) | Python, gTTS | Converts PDF files into MP3 audiobooks using text-to-speech |
| 11 | [Image Colour Palette](./11-ImageColourPalette) | Flask, OpenCV/PIL | Upload an image and extract its dominant colour palette |
| 12 | [Web Scraping](./12-WebScraping) | BeautifulSoup, Pandas | Scrapes Steam top sellers and exports results to CSV |
| 13 | [Auto Dinosaur Game](./13-AutoDinosaurGame) | Python, Selenium/PyAutoGUI | Automates Chrome's offline dinosaur game |
| 14 | [Space Invaders](./14-SpaceInvaders) | Python, Turtle | Space Invaders arcade game with player, aliens, and bullets |
| 15 | [Riot Games API](./15-RiotGamesAPI) | Flask, Riot API | Web app that fetches and displays League of Legends player stats |
| 16 | [Online Shop](./16-OnlineShop) | FastAPI, SQLAlchemy, HTML/CSS | Full-stack e-commerce application with cart and product management |
| 17 | [Automation](./17-Automation) | Python, Requests | Twitch VOD scraper — fetches past broadcasts for any streamer |
| 18 | [Data Science 1 — Space Missions](./18-DataScience1) | Pandas, Plotly, Matplotlib | Analysis of all space missions since 1957 with interactive visualisations |
| 19 | [Data Science 2 — Fatal Force](./19-DataScience2) | Pandas, Plotly, Matplotlib | Analysis of fatal police shootings in the US with demographic data |

---

## 🛠️ Tech Stack

The projects collectively use the following technologies:

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3 |
| **Web Frameworks** | Flask, FastAPI |
| **Databases** | SQLite, SQLAlchemy |
| **Frontend** | HTML5, CSS3, Jinja2 |
| **GUI** | Tkinter, Turtle |
| **Data Science** | Pandas, NumPy, Plotly, Matplotlib, Seaborn |
| **Web Scraping** | BeautifulSoup, Selenium, Requests |
| **APIs** | Riot Games API, Twitch API |
| **Other** | gTTS, OpenCV, PIL, iso3166 |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/20PythonProjects.git
cd 20PythonProjects

# Create a virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies for a specific project (if it has a requirements.txt)
cd 16-OnlineShop
pip install -r requirements.txt
```

### Running a Project

Each project is self-contained in its own folder. Navigate to the project directory and run:

```bash
# For CLI / GUI projects
python main.py

# For Flask projects
python main.py
# Then open http://localhost:5000

# For Jupyter notebooks (Data Science projects)
jupyter notebook
```

---

## 📁 Repository Structure

```
20PythonProjects/
├── 01-MorseCodeProject/         # CLI app
├── 02-PortfolioWebsiteProject/  # Flask web app
├── 03-TicTacToe/                # Terminal game
├── 04-ImageWatermark/           # Tkinter GUI
├── 05-TypingSpeed/              # Tkinter GUI
├── 06-BreakoutGame/             # Turtle game
├── 07-Cafe&Wifi/                # Flask + SQLite
├── 08-TodoList/                 # Flask + SQLite
├── 09-DisappearingText/         # Tkinter GUI
├── 10-PdfToAudiobook/           # Script + gTTS
├── 11-ImageColourPalette/       # Flask web app
├── 12-WebScraping/              # BeautifulSoup
├── 13-AutoDinosaurGame/         # Automation
├── 14-SpaceInvaders/            # Turtle game
├── 15-RiotGamesAPI/             # Flask + API
├── 16-OnlineShop/               # FastAPI full-stack
├── 17-Automation/               # Twitch scraper
├── 18-DataScience1/             # Jupyter notebook
├── 19-DataScience2/             # Jupyter notebook
└── README.md
```

---

## 📝 License

This repository is for educational purposes. Projects are based on exercises from the **100 Days of Code™** Python Bootcamp by Dr. Angela Yu.
