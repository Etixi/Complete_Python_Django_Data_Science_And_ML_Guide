print()
print("Example - Converting Dictionary to Another Dictionary" + "\n" +
      "========================================"
      )
print()

stocks = {
    'GOOGL': 1500,
    'AMZN': 3000,
    'AAPL': 300
}

doubled_stocks = {k: v * 2 for k, v in stocks.items() if v>=500}
print(doubled_stocks)