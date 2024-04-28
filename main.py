import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv"
df = pd.read_csv(url)

print(df.head())

mean_salary = df['salary'].mean()
median_salary = df['salary'].median()
std_dev_salary = df['salary'].std()
min_salary = df['salary'].min()
max_salary = df['salary'].max()

print(f"Mean Salary: {mean_salary}")
print(f"Median Salary: {median_salary}")
print(f"Standard Deviation of Salary: {std_dev_salary}")
print(f"Minimum Salary: {min_salary}")
print(f"Maximum Salary: {max_salary}")