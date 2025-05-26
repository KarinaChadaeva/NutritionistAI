import recipes
import sys
import pandas as pd


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        raw_input = " ".join(sys.argv[1:])
        ingredients = [ing.strip().lower() for ing in raw_input.split(',')]

        features = pd.read_csv('data/features.csv')
        all_ingredients = [col.strip().lower() for col in features.columns]

        feature_vector = [1 if ing in ingredients else 0 for ing in all_ingredients]

        X_input = pd.DataFrame([feature_vector], columns=all_ingredients)
        f = recipes.Forecast(X_input)
        f.forecast_rating()
        f.print_forecast()

        n = recipes.Nutrients(ingredients)
        n.calculate_daily_values()
        n.print_nutrients()

        r = recipes.Recipes(ingredients)
        r.choose_recipes()
        r.print_recipes()
    else:
        print("Please provide a list of coma-separated ingredients")
        sys.exit(1)