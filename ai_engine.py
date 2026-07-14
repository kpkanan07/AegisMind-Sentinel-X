from backend.anomaly_detection import detect_anomaly
from backend.threat_reasoning import generate_reasoning



def analyze_threat(data):


    risk_score = detect_anomaly(data)


    reasoning = generate_reasoning(
        data,
        risk_score
    )


    if risk_score >=70:

        level="HIGH"


    elif risk_score >=40:

        level="MEDIUM"


    else:

        level="LOW"



    return {


        "risk_score":risk_score,

        "threat_level":level,

        "reasoning":reasoning


    }