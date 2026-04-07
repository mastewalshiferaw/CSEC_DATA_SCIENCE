# Statistical Engineering & Simulation

## Project Overview
A custom-built Python statistical engine designed to process numerical datasets and perform Monte Carlo simulations to validate the Law of Large Numbers (LLN).

## Mathematical Logic
- **Variance:** Implemented with a toggle for Population ($\sigma^2$) and Sample ($s^2$). Sample variance utilizes **Bessel's Correction ($n-1$)** to reduce bias in small datasets.
- **Median:** Dynamically handles parity:
    - *Odd:* Returns the middle element.
    - *Even:* Returns the mean of the two central elements.
- **Outlier Detection:** Uses Z-score logic: $|x - \mu| > (threshold \times \sigma)$.

## Setup Instructions
1. **Clone the repo:** `git clone https://github.com/your-username/statistical_engine`
2. **Install:** Ensure you have Python 3.x installed.
3. **Run Simulation:** `python main.py`
4. **Run Tests:** `python -m unittest discover tests`

## Acceptance Criteria Checklist
- [x] **Empty Arrays:** Handled via custom `ValueError`.
- [x] **Data Cleaning:** Strict type checking for `int` and `float`.
- [x] **Variance:** Supports both Population and Sample logic.
- [x] **Modes:** Returns a list for multimodal distributions.
- [x] **Test Suite:** Comprehensive `unittest` coverage for edge cases.

## Law of Large Numbers Interpretation
The simulation proves that while small-sample data (e.g., 30 days) is subject to extreme volatility and "luck," large-scale data (10,000 days) converges to the theoretical probability. Relying on short-term data for financial planning is a primary cause of startup failure.