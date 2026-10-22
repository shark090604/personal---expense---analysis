import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("personal_expense_raw.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_expenses = df.groupby("Month")["Amount_INR"].sum()

monthly_expenses.plot(kind="line", marker="o")

plt.title("Monthly Personal Expenses")
plt.xlabel("Month")
plt.ylabel("Amount (INR)")
plt.grid(True)
plt.tight_layout()

plt.savefig("monthly_expenses.png", dpi=300)
