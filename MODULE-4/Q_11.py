#11) Write a Python program to write a list to a file. 

names = ['nikhil', 'nik', 'shiva']

with open(r'E:/demos/files_demos/account/sales.txt', 'w') as fp:
    for item in names:
        
        fp.write("%s\n" % item)
    print('Done')