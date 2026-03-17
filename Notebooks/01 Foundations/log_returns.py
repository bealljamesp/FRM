import numpy as np
import pandas as pd

# 1. Setup a dummy Price series (like your SQL Price History)
prices = pd.Series([100.0, 102.0, 101.0, 105.0, 104.0])

# 2. Arithmetic Return (Simple)
# (Price_t - Price_t-1) / Price_t-1
simple_rets = prices.pct_change()

# 3. Log Return (The Quant Standard)
# ln(Price_t / Price_t-1) which is also ln(Price_t) - ln(Price_t-1)
log_rets = np.log(prices / prices.shift(1))

# Output
results = pd.DataFrame(
    {"Price": prices, "Simple_Ret": simple_rets, "Log_Ret": log_rets}
)

print(results)

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# 1. Clean the data
clean_returns = log_rets.dropna()

# 2. Setup the Plot
plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(
    clean_returns, bins=10, color="skyblue", edgecolor="black"
)

# 3. Precision Labeling (Adding % values on top of bars)
for count, patch in zip(counts, patches):
    if count > 0:
        # Get the center of the bin to find the return value
        bin_center = patch.get_x() + patch.get_width() / 2
        # Format the count (frequency) and the return value (%)
        plt.text(
            bin_center,
            count + 0.05,
            f"{bin_center:.2%}",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
        )

# 4. Force X-Axis to use Decimals (4 decimal places)
plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter("%.4f"))

# 5. Add Mean and Median for Risk Analysis
plt.axvline(
    clean_returns.mean(),
    color="red",
    linestyle="dashed",
    label=f"Mean: {clean_returns.mean():.4f}",
)
plt.axvline(
    clean_returns.median(),
    color="green",
    linestyle="dotted",
    label=f"Median: {clean_returns.median():.4f}",
)

plt.title("Log Returns Distribution with Precision Labels", fontsize=14)
plt.xlabel("Return Value (Decimal)", fontsize=12)
plt.ylabel("Frequency (Days)", fontsize=12)
plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.show()
