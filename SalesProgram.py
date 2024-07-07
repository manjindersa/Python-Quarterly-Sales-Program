print("\nThe Quarterly Sales Program\n")

# Initialize a list to store sales for each quarter
sales = []

# Get sales for each quarter from the user
for i in range(1, 5):
    while True:
        try:
            sale = float(input(f"Enter sales for Q{i}: "))
            sales.append(sale)
            break
        except ValueError:
            print("Please enter a valid number.")

# Calculate the total, average, lowest, and highest sales
total_sales = sum(sales)
average_sales = total_sales / 4
lowest_sales = min(sales)
highest_sales = max(sales)

# Print the results, rounding to 2 decimal places
print(f"\nTotal: \t\t\t{total_sales:.2f}")
print(f"Average Quarter:\t{average_sales:.2f}")
print(f"Lowest Quarter:\t\t{lowest_sales:.2f}")
print(f"Highest Quarter:\t{highest_sales:.2f}")
print()