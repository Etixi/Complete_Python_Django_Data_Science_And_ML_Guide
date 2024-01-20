print()
print("Example - Data Manipulation Using the Ternary Operator" + "\n" +
      "==========================================================")
print()

def process_data(data):
    processed_data = data if data is not None else []
    # process data...
    return processed_data

received_data = None
data = process_data(received_data)
print(data)