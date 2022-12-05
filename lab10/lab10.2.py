import os

files = os.getcwd()

for i in os.walk(files):
    if "input.txt" in i[-1]:
        print(f"true in - {i[0]}")