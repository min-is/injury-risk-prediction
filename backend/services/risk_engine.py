import joblib
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

class InjuryRiskModel:
    def __init__(self):
        self.model = GradientBoostingClassifier(
            n_estimators=200,
            max_depth=5,
            learning_rate=0.1,
            random_state=42
        )
    
    def load_data(self):
        pass
    
    def train(self):
        X, y = self.load_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        self.model.fit(X_train, y_train)
        joblib.dump(self.model, 'model.pkl')
    
    def predict(self, features):
        processed = self._process_features(features)
        return float(self.model.predict_proba([processed])[0][1])
    
    def _process_features(self, data):
        acwr = data['weekly_load'] / data['4wk_avg_load']
        return np.array([
            acwr,
            data['asymmetry_score'],
            data['sleep_quality'],
            data['stress_level']
        ])