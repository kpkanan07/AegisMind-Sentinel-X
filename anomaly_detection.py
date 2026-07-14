def detect_anomaly(data):
    
    score=0


    failed_login=data.get(
        "failed_login",
        0
    )

    requests=data.get(
        "requests",
        0
    )


    suspicious_ports=data.get(
        "ports",
        0
    )


    if failed_login > 10:
        score +=30


    if requests >300:
        score +=30


    if suspicious_ports >20:
        score +=40


    return min(score,100)
