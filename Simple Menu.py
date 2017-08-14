menu = {'Pepperoni':1.75,'Extra Cheese':1.75,'Plain':1.50,'Sicilian':2.00}
def print_menu(menu):
    i = 1
    for val in menu:
        print str(i)+' '+val+' '+str(menu[val])
        i+=1
def get_orders():
    orders = []
    value = "0"
    while(value != "-1"):
        value=raw_input("What would you like to order? Enter -1 to conclude order. Select a number: ")
        if(value != "-1"):
            orders.append(int(value)-1)
    return orders
def print_orders(orders):
    keys = list(menu.keys())
    for val in orders:
        print "Order: "+str(menu[keys[val]])
def compute_total(orders, menu):
    keys=list(menu.keys())
    total = 0
    for i in orders:
        total += menu[keys[i]]
    return total
print_menu(menu)
orders=get_orders()
print_orders(orders)
print compute_total(orders, menu)