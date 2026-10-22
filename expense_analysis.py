import pandas as pd

# Load the expense dataset
df = pd.read_csv("personal_expense_raw.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate key metrics
total_expenses = df["Amount_INR"].sum()
average_expense = df["Amount_INR"].mean()
highest_expense = df["Amount_INR"].max()
lowest_expense = df["Amount_INR"].min()

# Category-wise analysis
category_report = df.groupby("Category")["Amount_INR"].sum()
category_report = category_report.sort_values(ascending=False)

# Payment method analysis
payment_report = df.groupby("Payment_Method")["Amount_INR"].sum()

# Monthly analysis
df["Month"] = df["Date"].dt.to_period("M")
monthly_report = df.groupby("Month")["Amount_INR"].sum()

# Display report
print("===== PERSONAL EXPENSE ANALYSIS =====")
print(f"Total Expenses: Rs. {total_expenses:,.2f}")
print(f"Average Expense: Rs. {average_expense:,.2f}")
print(f"Highest Expense: Rs. {highest_expense:,.2f}")
print(f"Lowest Expense: Rs. {lowest_expense:,.2f}")

print("\n===== CATEGORY-WISE EXPENSES =====")
print(category_report)

print("\n===== PAYMENT METHOD ANALYSIS =====")
print(payment_report)

print("\n===== MONTHLY EXPENSES =====")
print(monthly_report)
# Save analysis report to a text file
with open("expense_report.txt", "w") as file:
    file.write("PERSONAL EXPENSE ANALYSIS REPORT\n")
    file.write("=" * 35 + "\n")
    file.write(f"Total Expenses: Rs. {total_expenses:,.2f}\n")
    file.write(f"Average Expense: Rs. {average_expense:,.2f}\n")
    file.write(f"Highest Expense: Rs. {highest_expense:,.2f}\n")
    file.write(f"Lowest Expense: Rs. {lowest_expense:,.2f}\n\n")

    file.write("CATEGORY-WISE EXPENSES\n")
    file.write(category_report.to_string() + "\n\n")

    file.write("PAYMENT METHOD ANALYSIS\n")
    file.write(payment_report.to_string() + "\n\n")

    file.write("MONTHLY EXPENSES\n")
    file.write(monthly_report.to_string() + "\n")

print("\nReport saved as expense_report.txt")
