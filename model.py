
'''sample check git code'''

class Product:
    def __init__(self, pid, pnm, pcat, pqty):
        self.prodId = pid
        self.prodName = pnm
        self.prodCat = pcat
        self.prodQty = pqty

    def __str__(self):
        return f'''
            ProductId = {self.prodId},
            ProductName = {self.prodName},
            ProductCat = {self.prodCat},
            ProductQty = {self.prodQty},
          '''
    def __repr__(self):
        return str(self)

