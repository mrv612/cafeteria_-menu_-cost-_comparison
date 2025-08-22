# cafeteria_-menu_-cost-_comparison


📊 Cafeteria Menu Cost Comparison
This project analyzes the cost difference between food items in a college cafeteria and local market prices. By using data analysis techniques, it identifies and ranks items that are significantly overpriced, providing actionable insights for potential cost adjustments.

🌟 Features
Cost Analysis: Calculates the absolute and percentage price difference between cafeteria and market prices.

Overpriced Item Identification: Filters the dataset to highlight items that are more expensive in the cafeteria.

Data Ranking: Sorts and ranks items by their percentage price difference to show the most overpriced items first.

Actionable Insights: Provides suggestions for cost adjustments based on the analysis.

💻 How to Use
1. Requirements
Make sure you have Python installed, along with the pandas library. You can install pandas using pip:

pip install pandas

2. Run the Script
Copy the code from the cafeteria-cost-analysis.py file into your local environment.

Save the file.

Run the script from your terminal:

python cafeteria-cost-analysis.py

3. Customize the Dataset
You can easily add more items to the analysis by modifying the data dictionary in the script:

# The provided sample dataset
data = {
    'Item': ['Samosa', 'Sandwich', 'Juice', 'New_Item_Name'],
    'Cafeteria_Price': [20, 50, 30, 100],
    'Market_Price': [15, 40, 25, 80]
}

📊 Sample Output
The script generates a formatted table showing the overpriced items and their price differences.

![Table of Overpriced Items]

The script also provides a clear summary and suggestions for cost adjustments, making the results easy to understand and act upon.

![Analysis Summary]
