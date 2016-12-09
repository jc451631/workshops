__author__ = 'jc451631'
numofitems = 1
while numofitems > 0:
    numofitems = int(input("please enter the no. of items:"))
    costperitem = float(input("shipping cost of each items:"))
    shippingcosttotal = numofitems * costperitem ;
    if shippingcosttotal > 100:
        shippingcosttotal = shippingcosttotal - (shippingcosttotal * 0.1)
    print("the total cost for delivering your product is",shippingcosttotal)
