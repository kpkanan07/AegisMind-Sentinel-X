def generate_reasoning(data,risk):
    
    reasons=[]


    if data.get("failed_login",0)>10:

        reasons.append(
            "Multiple failed login attempts detected"
        )


    if data.get("requests",0)>300:

        reasons.append(
            "Abnormal traffic volume detected"
        )


    if data.get("ports",0)>20:

        reasons.append(
            "Possible port scanning behavior detected"
        )


    if not reasons:

        reasons.append(
            "Normal activity pattern detected"
        )


    return {

        "risk":risk,

        "explanation":reasons,

        "recommendation":[

            "Enable multi factor authentication",

            "Monitor suspicious IP activity",

            "Review security logs"

        ]

    }