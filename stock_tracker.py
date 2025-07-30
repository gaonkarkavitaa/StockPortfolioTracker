import datetime
import matplotlib.pyplot as plt

# Step 1: Hardcoded stock prices (Current Market Prices)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 320,
    "AMZN": 130
}

# Step 2: Purchase prices (Optional for profit calculation)
purchase_prices = {
    "AAPL": 150,
    "TSLA": 230,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 120
}

# Step 3: Welcome message
print("📈 Welcome to the Stock Portfolio Tracker!")

portfolio = {}
total_value = 0

# Step 4: User input loop
while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc.) or type 'done' to finish: ").upper().strip()
    if stock == "DONE":
        break
    if not stock:
        print("⚠️ Please enter a stock symbol.")
        continue
    if stock not in stock_prices:
        print("❌ Stock not found.")
        continue
    try:
        qty = int(input(f"Enter quantity for {stock}: "))
        if qty <= 0:
            raise ValueError
    except ValueError:
        print("⚠ Please enter a valid quantity (> 0).")
        continue
    portfolio[stock] = qty

# Step 5: Sort by value (descending)
sorted_portfolio = sorted(portfolio.items(), key=lambda x: stock_prices[x[0]] * x[1], reverse=True)

# Step 6: Display and export CSV
print("\n📊 Portfolio Summary:")
print("---------------------")

with open("portfolio.csv", "w", encoding="utf-8") as file:
    file.write(f"Portfolio Report - {datetime.datetime.now()}\n")
    file.write("Stock,Quantity,Current Price,Total Value,Profit\n")

    for stock, qty in sorted_portfolio:
        current_price = stock_prices[stock]
        buy_price = purchase_prices[stock]
        value = qty * current_price
        invested = qty * buy_price
        profit = value - invested
        total_value += value
        print(f"{stock}: {qty} × ₹{current_price} = ₹{value} | Profit: ₹{profit}")
        file.write(f"{stock},{qty},{current_price},{value},{profit}\n")

    print(f"\n💰 Total Investment: ₹{total_value}")
    file.write(f"Total Investment,,,₹{total_value},\n")

# Step 7: Export TXT version
with open("portfolio.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write("📊 Your Portfolio Summary\n")
    txt_file.write("----------------------------\n")
    for stock, qty in sorted_portfolio:
        current_price = stock_prices[stock]
        value = qty * current_price
        txt_file.write(f"{stock}: {qty} × ₹{current_price} = ₹{value}\n")
    txt_file.write(f"\n💰 Total Investment: ₹{total_value}\n")

# Step 8: Create Pie Chart
labels = []
sizes = []

for stock, qty in sorted_portfolio:
    value = qty * stock_prices[stock]
    labels.append(stock)
    sizes.append(value)

# Plot
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Stock Portfolio Distribution')

plt.axis('equal')
plt.tight_layout()
plt.savefig("portfolio_pie_chart.png")
plt.show()
# Step 9: Investment Grade Badge
if total_value < 5000:
    grade = "🟡 Beginner Investor"
elif total_value < 20000:
    grade = "🔵 Smart Investor"
else:
    grade = "🟢 Pro Investor"

print(f"🏅 Investment Grade: {grade}")
