from openai_service import analyze_currency_correlation

def analyze_correlation(currencies):
    
    insights = analyze_currency_correlation(currencies)
    return insights
