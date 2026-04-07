import json
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

def run_analysis():
    # 1. Load and process salaries
    try:
        with open('data/sample_salaries.json', 'r') as f:
            salaries = json.load(f)
        
        engine = StatEngine(salaries)
        print(f"Mean Salary: {engine.get_mean():.2f}")
        print(f"Median Salary: {engine.get_median():.2f}")
        print(f"Outliers: {engine.get_outliers(threshold=2)}")
    except FileNotFoundError:
        print("Error: data/sample_salaries.json not found. Please create it.")
        return

    # 2. Run Monte Carlo Simulations
    print("\n--- Monte Carlo: Server Crashes (Target: 4.5%) ---")
    for days in [30, 365, 10000]:
        simulated = simulate_crashes(days)
        print(f"Days: {days:5} | Result: {simulated:.4f}")

if __name__ == "__main__":
    run_analysis()