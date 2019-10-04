
from DEMO.sevices import *
from DEMO.model import Product

prodList = []
class serviceImpl(productServices):

    def add_Product(self,prod):
        # if type(prod) == Product:
        #     print(prod)
        #     print('Product Added Successfully...!')
        # else:
        #     return 'Invalid Product.. cant proceed...!'

        if prod and type(prod) == Product:
            if self.get_Product(prod.prodId):
                print('Duplicate..')
            else:
                prodList.append(prod)
                print('Added..')
                return prodList
                # print(prodList)

    def update_Product(self, prod):
       if prod and type(prod) == Product:
           dbprod = self.get_Product(prod.prodId)
           if dbprod:
                dbprod.prodName = prod.prodName
                dbprod.prodCat = prod.prodCat
                dbprod.prodQty = prod.prodQty
                print('Product Updated Successfully...!')

    def delete_Product(self,pid):
        pass

    def get_Product(self,pid):
        for prod in prodList:
            if prod.prodId == pid:
                return prod
        # return 'product not exist.. so cant proceed...!'

    def get_all_Products(self):
        return prodList
