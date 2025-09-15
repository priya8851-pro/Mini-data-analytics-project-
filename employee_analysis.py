import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("employees.csv")

# Total salary expense
print("Total Salary Expense:", data["Salary"].sum())

# Highest paid employee
max_emp = data.loc[data["Salary"].idxmax()]
print("Highest Paid:", max_emp["Name"], "with", max_emp["Salary"])

# Department-wise salary expense
dept_expense = data.groupby("Department")["Salary"].sum()
print("\nDepartment-wise Salary Expense:\n", dept_expense)

# Plot department-wise expense
dept_expense.plot(kind="bar", title="Department-wise Salary Expense", color="purple")
plt.ylabel("INR")
plt.show()
