# This is just a small Product Data Storage Software where we create a interface for Barcode scanner too
class Billing:
    __Product_ID = None
    __Product_Name = None
    __Product_Company = None
    __Product_Price = 0

    "This is gonna be a Parent class for all type of Billing Info that we are gonna need here"

    def __init__(self, Product_ID, Product_Name, Product_Company,Product_Price):
        self.__Product_ID = Product_ID
        self.__Product_Name = Product_Name
        self.__Product_Company = Product_Company
        self.__Product_Price = Product_Price

    # This function will take input from user:
    def get_info(self):
             try:
                      self.__Product_ID = input("Enter the value of Product Id:\t")
                      self.__Product_Name = input("Enter the Name of Product:\t")
                      self.__Product_Company = input("Enter the Name of Product Company:\t")
                      self.__Product_Price = input("Enter the Price of Product:\t")
                  except(ValueError,TypeError):
                           print("Invalid entry")
         

    # This will show Class content
    def display_info(self):
        print("The value of Product ID is:\t"+self.__Product_ID)
        print("The value of Product Name is:\t"+self.__Product_Name)
        print("The value of Product Company is:\t" + self.__Product_Company)
        print("The value of Product Price is:\t"+self.__Product_ID)


