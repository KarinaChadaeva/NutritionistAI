# 🥦 Nutritionist AI

## Overview

**Nutritionist AI** is a Python-based prototype application that helps users make healthier and tastier food choices based on ingredients they have. It predicts the quality of a potential dish, analyzes its nutritional content, and recommends similar recipes from the Epicurious database.

This project combines **data science**, **machine learning**, and **web scraping** techniques into a user-friendly command-line tool.

---

## Features

### ✅ Rating Prediction
- Forecasts if a dish made with selected ingredients will be **"bad"**, **"so-so"**, or **"great"**.
- Based on a classification model trained on the Epicurious dataset.

### ✅ Nutritional Analysis
- Displays nutritional values (% Daily Value) for each ingredient.
- Extracted using a public API and normalized for comparison.

### ✅ Recipe Recommendation
- Finds top 3 similar recipes from the Epicurious database.
- Shows each recipe's rating and a direct URL for full instructions.

---

## File Structure
project-root/
│
├── src/
│   ├── nutritionist.py       # Main script to run the application
│   ├── recipes.py            # Core logic: classes and methods for forecasting and recommendations
│
├── notebooks/
│   └── recipes.ipynb         # Research, EDA, model selection and evaluation
│
├── data/
│   ├── epi_r.csv             # Recipe dataset with ingredient features
│   ├── urls_recipes.csv      # Epicurious recipe titles with URLs and ratings
│   ├── nutrients.csv         # Nutrient Daily Value % per ingredient
│   ├── features.csv          # List of all binary ingredient features used for modeling
│   ├── countries.csv         # Used for cleaning initial dataset
│   └── us_states.csv         # Used for cleaning initial dataset
│
├── models/
│   └── best_model.pkl        # Final trained classification model used for rating prediction
│
└── README.md                 # This file

---

## How to Use

```bash
$ python3 nutritionist.py garlic, chicken

Output:



## Technologies Used
	•	Python 3
	•	Pandas, Scikit-learn
	•	BeautifulSoup (for web scraping)
	•	Jupyter Notebook (for research and modeling)

Created as part of a Python + Data Science Rush Project at School 21.
