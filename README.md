# 🛡️ AegisMind-Sentinel

## AI Powered Predictive Cyber Defense System

AegisMind-Sentinel is an AI-based cybersecurity platform that detects,
analyzes and predicts cyber threats using machine learning and threat intelligence.

## Features

- AI Threat Detection
- Anomaly Detection
- Risk Score Prediction
- Threat Reasoning Engine
- Security Dashboard
- Automated Security Recommendations

## Technology

Frontend:
React + Vite

Backend:
FastAPI + Python

AI:
Machine Learning

## Run Backend

Install:

pip install -r requirements.txt


Start:

uvicorn backend.app:app --reload


## API

POST:

/analyze-threat

Example:

{
 "ip":"192.168.1.50",
 "failed_login":20,
 "requests":500
}
