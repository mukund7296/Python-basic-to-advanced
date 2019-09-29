# Python File IO - Python File Handling - Example Program

c = open("myfile.txt", 'w')

print("File created, successfully..!!");
print("writing some content inside the file....\n");

c.write("this is python file io tutorial\n");
c.write("this is python file io example\n");
c.write("this is python file handling tutorial\n");
c.write("this is python file handling example\n");

c.close()

print("File successfully closed..!!"); 