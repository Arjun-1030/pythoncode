import os,shutil
# #file handling->open file,close file,read file,write and maintain file.
path=r"C:\Users\Dell\Desktop\tranning\text.txt"
# my_file=open(path)
# print(my_file)
# print(my_file.read())#to read the file.
# print(my_file.writable())#to check whether to write in file or not.
# my_file.close()

# my_another_file=open("text.txt","w+")
# print(my_another_file.readable())
# print(my_another_file.writable()) 
# print(my_another_file.read())
# my_another_file.write("Ram\n")
# print(my_another_file.seek(1))#indexing garera kata dekhi padne
# print(my_another_file.read())

my_next_file=open('next.txt','a+')
print(my_next_file.writable())
print(my_next_file.readable())
my_next_file.write("Hello world\n")
print(my_next_file.seek(0))
print(my_next_file.read())
list1=['\nram\n','\nshyam\n','\nhari\n']
print(my_next_file.writelines(list1))
print(my_next_file.seek(0))
print(my_next_file.readline())
print(my_next_file.readlines())

shutil.copy('next.txt','arjun.txt')


