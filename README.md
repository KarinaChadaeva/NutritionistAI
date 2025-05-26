# 🥦 Nutritionist AI

## Overview

**Nutritionist AI** is a Python-based prototype application that helps users make food choices based on ingredients they have. It predicts the taste of a dish, analyzes its nutritional content and recommends similar recipes from the Epicurious database.

This project combines **data science**, **machine learning**, and **web scraping** techniques into a command-line tool.

---

## Features

### ✅ Rating Prediction
- Forecasts if a dish made with selected ingredients will be **"bad"**, **"so-so"**, or **"great"**
- Based on a classification model trained on the Epicurious dataset

### ✅ Nutritional Analysis
- Displays nutritional values (% Daily Value) for each ingredient
- Extracted using a public API

### ✅ Recipe Recommendation
- Finds top 3 similar recipes from the Epicurious database
- Shows each recipe's rating and URL

---

## File Structure
```
project-root/
│
├── src/
│   ├── nutritionist.py       # Main script to run the application
│   ├── recipes.py            # Core logic: classes and methods for forecasting and recommendations
│
├── notebooks/
│   └── recipes.ipynb         # Research, model selection and evaluation
│
├── data/
│   ├── epi_r.csv             # Recipe dataset with ingredient features
│   ├── urls_recipes.csv      # Epicurious recipe titles with URLs and ratings
│   ├── nutrients.csv         # Nutrient Daily Value % per ingredient
│   ├── features.csv          # List of all binary ingredient features used for modeling
│   ├── countries.csv         # Used for cleaning initial dataset
│   └── us_states.csv         # Used for cleaning initial dataset
│
└── README.md                 # This file
```
---

## How to Use

```bash
$ python3 nutritionist.py garlic, chicken
```

Output:
```
I. OUR FORECAST
Delicious choice! In our opinion, these ingredients work wonderfully together
— we think it's a great recipe idea

II. NUTRITION FACTS
Garlic
  Calcium: 51% of Daily Value
  Carbohydrate: 12% of Daily Value
  Vitamin C: 89% of Daily Value
Chicken
  Cholesterol: 15% of Daily Value
  Protein: 43% of Daily Value
  Sodium: 8% of Daily Value

III. TOP-3 SIMILAR RECIPES
- Spicy Noodle Soup , rating: 4.4, URL: https://www.epicurious.com/search?q=Spicy+Noodle+Soup
- Braised Chicken Teriyaki , rating: 3.8, URL: https://www.epicurious.com/search?q=Braised+Chicken+Teriyaki
- Braised Chicken with Celery Root and Garlic , rating: 4.4, URL: https://www.epicurious.com/search?q=Braised+Chicken+with+Celery+Root+and+Garlic
```


## Technologies
-	Python 3
-	Pandas, Scikit-learn
-	Jupyter Notebook (for research and modeling)

Created as part of a Python + Data Science Project at School 21.
