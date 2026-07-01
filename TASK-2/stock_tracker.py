# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock_name = input("\nEnter Stock Symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter Quantity: "))

    portfolio[stock_name] = quantity

# Calculate investment value
print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_value += investment

    print(
        f"{stock} | Quantity: {quantity} | "
        f"Price: ${price} | Value: ${investment}"
    )

print("\nTotal Investment Value: $", total_value)

# Save report to text file
with open("portfolio_summary.txt", "w") as file:
    file.write("===== STOCK PORTFOLIO SUMMARY =====\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Value: ${investment}\n"
        )

    file.write(f"\nTotal Investment Value: ${total_value}")

print("\nPortfolio saved to portfolio_summary.txt")