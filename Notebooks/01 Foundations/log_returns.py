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
