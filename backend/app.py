from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

HF_TOKEN = os.getenv('HF_TOKEN')  # Set your Hugging Face API token as environment variable
HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_text(prompt, max_length=200):
    if not HF_TOKEN:
        # Mock response for testing without token
        if "Qualitative" in prompt:
            return "Mock qualitative analysis: Apple Inc. has strong brand recognition and innovative product lineup. Recent news includes new iPhone releases and expansion into services. Management under Tim Cook has focused on privacy and sustainability."
        elif "Quantitative" in prompt:
            return "Mock quantitative analysis: Apple reported $394.3 billion in revenue for FY2023, up 2.8% YoY. Net income was $97.0 billion with a P/E ratio of 28.5. Debt-to-equity ratio stands at 1.5."
        elif "Valuation" in prompt:
            return "Mock valuation analysis: Using DCF model with 10% discount rate, intrinsic value is approximately $180 per share. Current market price of $192 suggests slight overvaluation. Comparables show P/E of 25-30x for tech peers."
        else:
            return "Mock overview: Apple is a leading technology company with strong financials and market position."
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": max_length,
            "temperature": 0.7,
            "do_sample": True
        }
    }
    response = requests.post(HF_API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and result:
            return result[0].get('generated_text', '').replace(prompt, '').strip()
    return "Unable to generate response at this time."

@app.route('/analyze', methods=['POST'])
def analyze_stock():
    data = request.get_json()
    ticker = data.get('ticker', '').upper()
    qualitative = data.get('qualitative', False)
    quantitative = data.get('quantitative', False)
    valuation = data.get('valuation', False)

    results = {}

    if qualitative:
        prompt = f"Qualitative analysis for {ticker} stock: company news, management quality, industry position."
        results['qualitative'] = generate_text(prompt)

    if quantitative:
        prompt = f"Quantitative analysis for {ticker} stock: financial ratios, revenue growth, profit margins."
        results['quantitative'] = generate_text(prompt)

    if valuation:
        prompt = f"Valuation analysis for {ticker} stock: intrinsic value, P/E ratio, DCF model."
        results['valuation'] = generate_text(prompt)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

