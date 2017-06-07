from ParentClass import Billing

import pickle,shelve

# Main programs begins here

if __name__ == "__main__":
	print("This is Main Program")





###########   FOR QUITTING THE MAIN MENU ####################################################
def return_prog():
           print(" You requested to quit this :")
           return

def show_all():
         print(" You requested to show all the records of File")
         confirmation = input(" Press 'y' or 'Y' for confirmation :")
         if confirmation == 'Y':
                  print("Your confirmation noticed:")
         elif confirmation == 'y':
                  print("Your confirmation noticed:")
         else:
                  print("You have entered a Wrong Choice, we are going back to main program")
                  return
         file_object = open("Master_File.data","rb")
         Billy = Billing()
         Billy = pickle.load(file_object)
         Billy.display_info()
         file_object.close()





############### FOR SHOWING A PARTICLUAR RECORD  ############################################				
def show_one():
           print(" You requested to quit this :")
           return





############### FOR UPDATING A PARTICULAR RECORD ############################################
def update():
           print(" You requested to quit this :")
           return




############### FOR DELETING A PARTICLUAR RECORD #############################################
def delete():
           print(" You requested to quit this :")
           return





############### FOR DELETING ALL THE RECORDS OF DATA FILE #####################################
def delete_all():
           print(" You requested to quit this :")
           return

def add_record():

##This is add_record which will add/append a particular record in the existing Master_File of record
           try:
                      file_object = open("Record_File.dat","wb")
                      Billy = Billing()
                      Billy.get_info()
                      pickle.dump(Billy,file_object)
                      file_object.close()
           except IOError:
                      print("File Opening Error")
##Options are defined with their functions using a dictionary options

options = {	0:return_prog,
			1:add_record,
			2:show_all,
			3:show_one,
			4:update,
			5:delete,
			6:delete_all,
	    }

print("Press 1: For Adding new records")
print("Press 2: For Showing all the records")
print("Press 3: For Showing a particular record")
print("Press 4: For Updating a record ")
print("Press 5: For Deleting a record")
print("Press 0: To quit")

#User choice has been taken into "choice" variable
choice = int(input("Enter your Choice"))			
print(choice)
#here we are calling the function as per user enter value
options[choice]()
