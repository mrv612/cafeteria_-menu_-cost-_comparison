import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/cafeteria_prices.csv")

# Calculate price difference & % difference
df["Price_Diff"] = df["Cafeteria_Price"] - df["Market_Price"]
df["%_Difference"] = (df["Price_Diff"] / df["Market_Price"]) * 100

# Filter overpriced items
overpriced = df[df["Price_Diff"] > 0].sort_values("%_Difference", ascending=False)

# Save results
overpriced.to_csv("../results/overpriced_items.csv", index=False)

# Visualization
plt.bar(overpriced["Item"], overpriced["%_Difference"])
plt.title("Overpriced Cafeteria Items (% Difference)")
plt.ylabel("% Over Market Price")
plt.xlabel("Item")
plt.savefig("../results/price_gap_chart.png")
plt.show()

print("Overpriced Items:\n", overpriced)
