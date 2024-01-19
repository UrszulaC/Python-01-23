import csv

companies = []
sales = []

with open('output.csv', newline='') as csvfile:
    reader = csv.reader(csvfile) 
    lines = csvfile.readlines
    next(reader) 
    for line in reader: 
        companies.append(line[0]) 
    for x in line[1:]:
        sales.append([int(x.replace(",", ""))])
        #sales.append([int(x.replace(",", "")) for x in line[1:]])

    #monthly_sum = []
    #for x in zip(*sales):
        #monthly_sum += x
    monthly_tot = [sum(x) for x in zip(*sales)]  
    #print(monthly_tot)

    yearly_sum = {}
    for i in range(len(companies)):
        yearly_sum[companies[i]] = sum(sales[i])
    #print(companies)
    print("Monthly sales:", monthly_tot)
    print("Yearly sales:",)
    for company, sales in yearly_sum.items():
        print(company, sales)




