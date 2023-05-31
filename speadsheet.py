import csv
import matplotlib.pyplot as plt



with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    
    #for row in spreadsheet:
    #    print(dict(row))

    the_sales = []


    for row in spreadsheet:
        all_sales= row['sales']
        print(all_sales)
        the_sales.append(int(all_sales))

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    the_months=[]
    for row in spreadsheet:
        x=row['month']
        the_months.append(x)
    print(the_months)

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    the_exp=[]
    for row in spreadsheet:
        y=row['expenditure']
        the_exp.append(int(y))
    print(the_exp)

        
print(the_sales)
total_sales=0
for x in the_sales:
    total_sales+=int(x)
    print(total_sales)

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    m_sales = []
    for row in spreadsheet:
        sales_value = row['sales']
        m_sales.append(sales_value)
    max_sales = max(m_sales)
    min_sales = min(m_sales)
print(f"Max value in sales column is: {max_sales}\nMin value in sales column is: {min_sales}")

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    expen = []
    for row in spreadsheet:
        expen_value = row['expenditure']
        expen.append(expen_value)
    max_expen = max(expen)
    min_expen = min(expen)
print(f"Max value in expenditure column is: {max_expen}\nMin value in expenditure column is: {min_expen}")


plt.bar(the_months, the_sales, color='g')
plt.title("Sales evolution")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
plt.savefig('Sales_evolution.png')
    # Plot the data using bar() method
    
plt.bar(the_months, the_exp, color='g')
plt.title("Expenditure evolution")
plt.xlabel("Month") 
plt.ylabel("Expenditure")
  
    # Show the plot
plt.show()
plt.savefig('Expenditure_evolution.png')
