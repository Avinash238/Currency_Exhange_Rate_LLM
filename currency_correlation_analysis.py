from openai_service import analyze_currency_correlation

def analyze_correlation(currencies):
    # Call OpenAI service to analyze currency correlation
    insights = analyze_currency_correlation(currencies)
    return insights
