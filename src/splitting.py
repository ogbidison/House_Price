from sklearn.model_selection import train_test_split

class split:

    def __init__(self, test_size, random_state):
        self.test_size = test_size,
        self.random_state = random_state

    def prep_df (df, target_col):

        features = df.drop(columns=[target_col])
        target = df[target_col]
        #missing = features[miss]
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=self.test_size, random_state=self.random_state)
    return X_train, X_test, y_train, y_test
   