print()
print("Example - Making Selections with the While Loop" + "\n" +
      "================================================="
      )
print()

selected_option = 10

while selected_option not in range(1, 4):
    print("Menu:")
    print("1. Start the game")
    print("2. Load saved game")
    print("3. Quit")
    selected_option = int(input("Please enter your choice (1-3): "))

if selected_option == 1:
    print("Starting the game...")

if selected_option == 2:
    print("Loading the game...")

if selected_option == 3:
    print("Quitting...")