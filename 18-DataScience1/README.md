# 🚀 Space Missions Analysis

> **Note:** This project was completed with the assistance of AI (Google Gemini).

<p align="center">
  <img src="https://i.imgur.com/9hLRsjZ.jpg" alt="Space Missions" width="500">
</p>

## 📋 Overview

A comprehensive data science project that analyzes **all space missions since the beginning of the Space Race in 1957**. The dataset was scraped from [nextspaceflight.com](https://nextspaceflight.com/launches/past/?page=1) and covers thousands of launches across multiple decades, organisations, and countries.

## 📊 Analysis Sections

| # | Section | Description |
|---|---------|-------------|
| 1 | **Preliminary Data Exploration** | Shape, columns, data types, NaN values, and duplicates |
| 2 | **Data Cleaning** | Removing junk columns, type conversions (Price → numeric, Date → datetime) |
| 3 | **Descriptive Statistics** | Summary statistics for numeric and categorical features |
| 4 | **Launches per Company** | Horizontal bar chart of top 20 organisations by launch count |
| 5 | **Active vs Retired Rockets** | Donut chart comparing active and decommissioned rockets |
| 6 | **Distribution of Mission Status** | Pie chart showing Success, Failure, Partial Failure, Prelaunch Failure |
| 7 | **Launch Price Distribution** | Histogram with box plot marginal for price in USD millions |
| 8 | **Launches by Country (Choropleth)** | World map colored by number of launches per country |
| 9 | **Failures by Country (Choropleth)** | World map colored by number of mission failures |
| 10 | **Sunburst Chart** | Hierarchical chart: Country → Organisation → Mission Status |
| 11 | **Total Spending by Organisation** | Bar chart + scatter plot (launches vs spending) |
| 12 | **Cost per Launch** | Average cost per launch by organisation + box plot distribution |
| 13 | **Launches per Year** | Time series of annual launch counts |
| 14 | **Month-on-Month Launches** | Monthly time series with 12-month rolling average |
| 15 | **Most Popular Launch Months** | Bar chart of launches by calendar month |
| 16 | **Launch Price Over Time** | Average price trend line chart |
| 17 | **Top 10 Organisations Over Time** | Stacked area chart showing dominance shifts |
| 18 | **Cold War Space Race** | USA vs USSR annual launch comparison (up to 1991) |
| 19 | **USA vs USSR Pie Chart** | Total Cold War era launches comparison |
| 20 | **Cumulative Launches (Superpowers)** | Cumulative launch count: USA vs USSR |
| 21 | **Mission Failures Year-on-Year** | Failure count trends for both superpowers |
| 22 | **Failure Percentage Over Time** | Failure rate trends (superpowers + overall) |
| 23 | **Leading Country per Year** | Which country had the most launches each year |
| 24 | **Leading Organisation per Year** | Which organisation dominated each year + decade summaries |

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Plotly Express** — Interactive charts (bar, pie, choropleth, sunburst, area)
- **Matplotlib** — Static plots (time series with rolling average)
- **Seaborn** — Statistical visualizations
- **iso3166** — Country name to ISO Alpha-3 code conversion

## 📁 Project Structure

```
18-DataScience1/
├── Space_Missions_Analysis_(start).ipynb   # Main analysis notebook
├── mission_launches.csv                     # Dataset
└── README.md                                # This file
```

## 📦 Installation

```bash
# Install required packages
pip install pandas numpy plotly matplotlib seaborn iso3166
```

## ▶️ How to Run

1. Open the notebook in **Jupyter Notebook**, **JupyterLab**, or **Google Colab**
2. Run all cells sequentially from top to bottom
3. Interactive Plotly charts will render inline

```bash
# Launch Jupyter
jupyter notebook Space_Missions_Analysis_(start).ipynb
```

## 📈 Dataset

| Column | Description |
|--------|-------------|
| `Organisation` | Company/agency that conducted the launch |
| `Location` | Launch site location |
| `Date` | Date and time of the launch (UTC) |
| `Detail` | Rocket name/model |
| `Rocket_Status` | Active or Retired |
| `Price` | Launch cost in USD millions (many missing values) |
| `Mission_Status` | Success, Failure, Partial Failure, or Prelaunch Failure |

- **Rows:** 4,324 missions
- **Time Span:** 1957 – 2020
- **Price Data Available:** ~964 out of 4,324 missions

## 🔑 Key Findings

- 🏆 **RVSN USSR** has the most launches historically
- 📉 Mission failure rates have **decreased significantly** over the decades
- 💰 Launch prices vary wildly — from under $10M to over $400M
- 🇷🇺 The **USSR/Russia** dominated the space race during the Cold War era
- 🚀 **SpaceX** emerged as the dominant organisation in 2018–2020
- 📅 **December** and **June** tend to be the most popular months for launches

## 📝 License

This project is for educational and analytical purposes.
