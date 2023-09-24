import math
 
purchase=int(input("Number of purchases: "))
salestax=float(input("Sales tax: "))
customers=[]
costs=[]
for i in range(purchase):
    customer=input("Customer: ")
    cost=float(input("Cost: "))
    customers.append(customer)
    costs.append(cost)

def add_tax(costs,salestax):
    return([cost*(1+salestax)for cost in costs])


withtax = add_tax(costs, salestax)

totalcost={}

for i in range(purchase):
    customer=customers[i]
    cost=withtax[i]
    if customer in totalcost:
        totalcost[customer]+=cost
    else:
        totalcost[customer]=cost
print(totalcost)






















#customer1=input("Customer: ")
#Costbt= int(input("Cost: "))
#customer2=input("Customer: ")
#Costbt2=int(input("Cost: "))
#print("Customer:{customer1})
#Costbt3=int(input("Cost: "))

#customers.append[customer1,customer2]
#costs.append[Costbt,Costbt2,Costbt3]

#def add_tax(costs,salestax):
    #for cost in costs:
        #costs=costs*salestax
    #return add_tax