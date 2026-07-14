import numpy as np
import joblib

from sklearn.ensemble import RandomForestClassifier


X = np.array([

    [2,120,3,250],
    [5,200,8,400],
    [35,900,60,1400],
    [50,1200,80,2000],
    [10,650,45,1100],
    [1,80,2,150]

])


# 0 = Safe
# 1 = Threat

y = np.array([

    0,
    0,
    1,
    1,
    1,
    0

])


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


model.fit(X,y)


joblib.dump(
    model,
    "anomaly_model.pkl"
)


print("✅ anomaly_model.pkl created")