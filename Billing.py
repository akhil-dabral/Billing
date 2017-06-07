from Parent_Class_File import Billing
import pickle,shelve
# Main programs begins here

Billy = Billing("212943","SkullCandy-2010223","SkullCandy",1300)
Billy.get_info()
Billy.display_info()

#Lets start making a data file where we'll store all of our class objects
file_object = open("Source_File.dat","wb")
pickle.dump(Billy,file_object)
file_object.close()



#Now we are gonna print these values in console too
file_object = open("Source_File.dat","rb")
BILL = Billing("000000","00000","00000",000)
BILL = pickle.load(file_object)
BILL.display_info()



if __name__ == "__main__":
    print("This is Main Program")
