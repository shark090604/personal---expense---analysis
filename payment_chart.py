import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("personal_expense_raw.csv")

payment_expenses = (
    df.groupby("Payment_Method")["Amount_INR"]
    .sum()
    .sort_values(ascending=False)
)

payment_expenses.plot(kind="bar")

plt.title("Expenses by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Amount (INR)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("payment_expenses.png", dpi=300)
