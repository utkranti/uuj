from DEMO.model import Product
from DEMO.serviceImpl import *

if __name__ == '__main__':
    p1 = Product(pid = 101, pnm = 'Mobile', pcat = 'Personal', pqty = 12)
    # print(p1)
    p2 = Product(pid = 102, pnm = 'Laptop', pcat = 'Personal', pqty = 2)
    p3 = Product(pid = 103, pnm = 'Fridge', pcat = 'Personal', pqty = 2)
    p4 = Product(pid = 104, pnm = 'TV', pcat = 'Personal', pqty = 2)
    p5 = Product(pid = 105, pnm = '', pcat = 'Personal', pqty = 2)

    ser = serviceImpl()
    # ser.add_Product(p2)
    print(ser.add_Product(p2))
    print(ser.get_Product(102))
    # ser.update_Product(p2)
    # print(ser.get_all_Products())