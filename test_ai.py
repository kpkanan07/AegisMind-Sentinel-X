import joblib
import numpy as np


model = joblib.load(
    "models/anomaly_model.pkl"
)


test_data = np.array([

    [
        40,
        1000,
        70,
        1800
    ]

])


prediction = model.predict(test_data)

confidence = model.predict_proba(test_data)


if prediction[0] == 1:

    print("🚨 Threat Detected")

else:

    print("✅ Normal Activity")


print(
    "Confidence:",
    round(max(confidence[0])*100,2),
    "%"
)