# PPP Price Comparison Analysis

This project analyzes the price differences of commonly purchased items in India, adjusting for purchasing power parity (PPP). It fetches live exchange rates from the [Exchange Rate API](https://www.exchangerate-api.com/) and compares the prices in India (INR) to their equivalent values in USD and PPP-adjusted USD.

## Features:
- Fetches live exchange rate (USD to INR).
- Compares the price of items in INR to USD using current exchange rates.
- Adjusts the price based on PPP to reflect the relative purchasing power in India.
- Generates a CSV report and graphs for price comparisons.

## Requirements:
- Python 3.x
- Libraries:
  - `requests`
  - `pandas`
  - `matplotlib`

## Installation:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ppp-analysis.git
    ```
2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Obtain an API key from [Exchange Rate API](https://www.exchangerate-api.com/) and replace it in the `api_key` variable in `ppp_analysis.py`.

## Usage:
Run the program using the following command:

```bash
python ppp_analysis.py
