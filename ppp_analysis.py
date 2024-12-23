import requests
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch exchange rates
def fetch_exchange_rate(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        exchange_rate = data["conversion_rates"]["INR"]
        return exchange_rate
    else:
        print("Error: Unable to fetch exchange rate.")
        exit()

# Function to analyze and compare prices
def analyze_prices(india_prices, exchange_rate):
    # Create a DataFrame for analysis
    df = pd.DataFrame(india_prices, columns=["Item", "Price_INR"])
    df["Price_USD"] = df["Price_INR"] / exchange_rate

    # Example PPP Adjustment Factor (you can refine this value based on research)
    ppp_factor = 0.23  # Assumes 1 INR in India has the purchasing power of $0.23 in the US
    df["PPP_Adjusted_USD"] = df["Price_INR"] * ppp_factor

    # Save data to CSV
    df.to_csv("price_comparison.csv", index=False)

    # Generate graphs
    plt.figure(figsize=(10, 6))
    plt.bar(df["Item"], df["Price_USD"], color="blue", label="Price in USD (Converted)")
    plt.bar(df["Item"], df["PPP_Adjusted_USD"], color="orange", alpha=0.7, label="PPP-Adjusted USD Price")
    plt.xlabel("Items")
    plt.ylabel("Price (USD)")
    plt.title("Price Comparison: Market vs. PPP Adjusted")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("price_comparison_graphs.png")
    plt.show()

# Main function
def main():
    api_key = "6c2e0ebe8f6bb946339dd7e8"  # Replace with your API key

    # Step 1: Fetch exchange rate
    exchange_rate = fetch_exchange_rate(api_key)
    print(f"Live Exchange Rate (1 USD to INR): {exchange_rate}")

    # Step 2: Define price list for analysis (in INR)
    india_prices = [
        ["Milk (1 liter)", 60],
        ["Eggs (12)", 80],
        ["Chicken (1 kg)", 200],
        ["Rice (1 kg)", 50],
        ["Gasoline (1 liter)", 110],
    ]

    # Step 3: Analyze and compare prices
    analyze_prices(india_prices, exchange_rate)

if __name__ == "__main__":
    main()
