# 🔫 Fatal Police Shootings — Data Analysis

> **Note:** This project was completed with the assistance of AI (Google Gemini).

<p align="center">
  <img src="https://i.imgur.com/sX3K62b.png" alt="Fatal Force" width="500">
</p>

## 📋 Overview

A comprehensive data science project analysing **fatal police shootings in the United States** since January 2015, using data compiled by [The Washington Post](https://www.washingtonpost.com/graphics/investigations/police-shootings-database/). The analysis is supplemented with US Census data on poverty rates, high school graduation rates, median household income, and racial demographics.

## 📊 Analysis Sections

| # | Section | Description |
|---|---------|-------------|
| 1 | **Preliminary Data Exploration** | Shape, columns, data types, NaN values for all 5 datasets |
| 2 | **Data Cleaning** | Type conversions, NaN handling, date parsing |
| 3 | **Poverty Rate by State** | Bar chart ranking states by poverty rate |
| 4 | **High School Graduation Rate** | Bar chart of HS graduation rates in ascending order |
| 5 | **Poverty vs HS Graduation** | Dual y-axis chart, jointplot (KDE), and linear regression |
| 6 | **Racial Makeup by State** | Stacked bar chart of racial demographics per state |
| 7 | **Donut Chart — Killed by Race** | Pie/donut chart of fatalities by race |
| 8 | **Deaths: Men vs Women** | Bar chart comparing gender distribution |
| 9 | **Age & Manner of Death** | Box plot and violin plot by gender |
| 10 | **Were People Armed?** | Top weapons, armed vs unarmed pie chart |
| 11 | **Age Distribution** | Histogram, KDE, and per-race age distributions |
| 12 | **Race of People Killed** | Bar chart of total deaths by race |
| 13 | **Mental Illness** | Percentage and pie chart of mental illness signs |
| 14 | **Top 10 Most Dangerous Cities** | Bar chart of cities with most killings |
| 15 | **Rate of Death by Race (Top Cities)** | Stacked bar chart — racial breakdown in top 10 cities |
| 16 | **Choropleth Maps** | US state maps for killings and poverty rate comparison |
| 17 | **Killings Over Time** | Yearly bar chart, monthly trend with rolling average, race over time |

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Plotly Express** — Interactive charts (bar, pie, choropleth)
- **Matplotlib** — Static plots (dual axis, time series)
- **Seaborn** — Statistical visualisations (KDE, regression, violin plots)

## 📁 Project Structure

```
19-DataScience2/
├── Fatal_Force_(start).ipynb              # Main analysis notebook
├── Deaths_by_Police_US.csv                # Police killings dataset
├── Median_Household_Income_2015.csv       # Census: median household income
├── Pct_People_Below_Poverty_Level.csv     # Census: poverty rates
├── Pct_Over_25_Completed_High_School.csv  # Census: HS graduation rates
├── Share_of_Race_By_City.csv              # Census: racial demographics
└── README.md                              # This file
```

## 📈 Datasets

| Dataset | Rows | Description |
|---------|------|-------------|
| Deaths by Police | 2,535 | Every fatal shooting by police since Jan 2015 |
| Poverty Level | 29,329 | Poverty rate by city |
| High School Graduation | 29,329 | HS completion rate by city |
| Median Income | 29,322 | Median household income by city |
| Race by City | 29,268 | Racial demographic share by city |

## 🔑 Key Findings

- 👤 **95.8%** of people killed by police are **male**
- 🔫 **55%** of those killed were carrying a **gun**
- 🧠 **~25%** showed signs of **mental illness**
- 🏙️ **Los Angeles** and **Phoenix** are among the cities with the most killings
- 📉 There is a **negative correlation** between poverty rates and high school graduation rates
- 🧑‍🤝‍🧑 **White** individuals make up the largest absolute number, but minority groups are disproportionately represented

## 📝 License

This project is for educational and analytical purposes.
