#list = "C:\Users\incar\Desktop\Python\labs\lab72.py"

list = input(" Enter the file path: ")
list = list.split('\\')

for i in list[:-1]:
        print(i)

print(f"Name of file - {list[-1].split('.')[0]}, file extension - .{list[-1].split('.')[1]}")