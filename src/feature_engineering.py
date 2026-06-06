

class FeatureEngine:
     def __init__(self, numerical_cols, cat_cols):
          self.numerical_cols = numerical_cols
          self.cat_cols = cat_cols

    def 










from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def feature_engine(X_train, X_test, numerical_cols, cat_col):
    

    numerical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_pipeline, numerical_cols),
            ('cat', categorical_pipeline, cat_col)
        ]
    )

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    return X_train_processed, X_test_processed