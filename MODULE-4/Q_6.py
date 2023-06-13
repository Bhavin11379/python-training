#6) Write a Python program to read a file line by line and store it into a list


def file_read(fname):
        with open (fname, "r") as myfile:
         data=myfile.readlines()
         print(data)
file_read('test.txt')