
from abc import ABC,abstractmethod

class productServices(ABC):

    @abstractmethod
    def add_Product(self, prod):
      pass


    @abstractmethod
    def update_Product(self, prod):
      pass

    @abstractmethod
    def delete_Product(self, pid):
      pass

    @abstractmethod
    def get_Product(self, pid):
      pass

    @abstractmethod
    def get_all_Products(self):
      pass
