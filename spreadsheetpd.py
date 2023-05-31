import pandas
import numpy as np
import matplotlib.pyplot as plt

df = pandas.read_csv('sales.csv')
print (df)

print('total sum is ')
print(sum(df['sales']))

sales=[]
for row in df['sales']:
    print(row)
    sales.append(row)

print(sales)

total_sales=0
for x in sales:
    total_sales+=int(x)
    print(total_sales)

X = list(df.iloc[:, 1])
Y = list(df.iloc[:, 2])
  
# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Sales evolution")
plt.xlabel("Month")
plt.ylabel("Sales")
  
# Show the plot
plt.show()

W = list(df.iloc[:, 1])
Z = list(df.iloc[:, 3])
print(Z)
print(W)
# Plot the data using bar() method
plt.bar(W, Z, color='g')
plt.title("Expenditure evolution")
plt.xlabel("Month")
plt.ylabel("Expenditure")
  
# Show the plot
plt.show()

