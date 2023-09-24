purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))

x = purchases
y = 1

customer_names = []
item_costs = []

while y<=x:
    customer = input("Customer: ")
    cost = float(input("Cost: "))
    customer_names.append(customer)
    item_costs.append(cost)
    y=y+1

def add_tax(items_costs_list, tax):
    return [cost * (1 + tax) for cost in items_costs_list]

item_costs_with_tax = add_tax(item_costs, sales_tax)

customer_totals = {}

for customer, cost in zip(customer_names, item_costs_with_tax):
    if customer in customer_totals:
        customer_totals[customer] += cost
    else:
        customer_totals[customer] = cost

print(customer_totals)