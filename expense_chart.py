import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("personal_expense_raw.csv")

category_expenses = (
    df.groupby("Category")["Amount_INR"]
    .sum()
    .sort_values(ascending=False)
)

category_expenses.plot(kind="bar")

plt.title("Category-wise Personal Expenses")
plt.xlabel("Expense Category")
plt.ylabel("Amount (INR)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("category_expenses.png", dpi=300)
plt.show()
