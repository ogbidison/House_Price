from sklearn.model_selection import cross_val_score, cross_val_predict, KFold, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

class Inference():
    

def predictions_model (models, parameter_grid, X_train, X_test, y_train, y_test):
    results = {}

    for model_name, model in models.items():
        print(f"\n Training {model_name}...")

        params = parameter_grid.get(model_name, {})

        grid = GridSearchCV(
            estimator=model,
            param_grid= params,
            scoring='neg_mean_squared_error',
            cv=5,
            n_jobs=-1,
            verbose=1
        )

        grid.fit(X_train, y_train)

        best_model = grid.best_estimator_

        pred = best_model.predict (X_test)

        mae = mean_absolute_error(y_test, pred)

        mse = mean_squared_error(y_test, pred)

        r2 = r2_score(y_test, pred)

        results[model_name] = {
            "best_params": grid.best_params_,
            "best_score": grid.best_score_,
            "mae": mae,
            "mse": mse,
            "r2score": r2,
            "best_model": best_model
        }
        print(f"✔ {model_name} done.")

    return results, best_model
