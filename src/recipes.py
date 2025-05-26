import joblib
import pandas as pd
from imblearn.ensemble import BalancedRandomForestClassifier


class Forecast:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.rating_class = None

    def forecast_rating(self):
        model = joblib.load('data/best_model.pkl')
        prediction = model.predict(self.ingredients)
        self.rating_class = prediction
        return self.rating_class

    def print_forecast(self):
        print("I. OUR FORECAST")
        if self.rating_class == 'great':
            print("Delicious choice! In our opinion, these ingredients work wonderfully together\n— we think it's a great recipe idea")
        elif self.rating_class == 'so-so':
            print("You might enjoy this dish, but we think it's only somewhat acceptable given\nthe ingredients you've chosen")
        else:
            print("You might find it tasty, but in our opinion, it is a bad idea to have\na dish with that list of ingredients")
    
    
class Nutrients:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.daily_values_dict = dict()

    def calculate_daily_values(self):
        nutrients = pd.read_csv('data/nutrients.csv')
        nutrients.set_index('ingredient', inplace=True)

        for ing in self.ingredients:
            if ing in nutrients.index:
                row = nutrients.loc[ing]
                self.daily_values_dict[ing] = row[row > 0].to_dict()
        return self.daily_values_dict
    
    def print_nutrients(self):
        print("\nII. NUTRITION FACTS")
        for ingr in self.ingredients:
            print(ingr.capitalize())
            values = self.daily_values_dict.get(ingr.lower(), {})
            if values:
                for nutrient, percent in values.items():
                    print(f"  {nutrient}: {percent}% of Daily Value")
    

class Recipes:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.recipes_names = []
    
    def choose_recipes(self):
        data = pd.read_csv("data/epi_r.csv")
        valid_ingredients = [ing for ing in self.ingredients if ing in data.columns]
        if not valid_ingredients:
            return []
        data['match_score'] = data[valid_ingredients].sum(axis=1)
        data = data[data['match_score'] > 0]
        top_matches = data.sort_values(by='match_score', ascending=False)
        self.recipes_names = top_matches['title'].tolist()
        return self.recipes_names
    
    def print_recipes(self):
        print("\nIII. TOP-3 SIMILAR RECIPES")
        data = pd.read_csv("data/urls_recipes.csv")
        counter = 0
        for name in self.recipes_names:
            for _, row in data.iterrows():
                if row['title'].strip() == name.strip():
                    print(f"- {name}, rating: {row['rating']}, URL: {row['url']}")
                    counter += 1
                    break
            if counter == 3:
                break