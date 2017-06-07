# Here we are gonna create a simple OutPut.txt text file and write some data into it

file_object = open("Write_to_text.txt","w")
# We need to make sure that it is opened in correct mode i.e. Write mode "w"

file_object.write("Line 1\n")
file_object.write("This is Line 2\n")
file_object.write("Last line number 3\n")

list1 = { "This is First Line of List1",
          "This is second line of List2",
          "this is third line of List3"  }
file_object.writelines(list1)