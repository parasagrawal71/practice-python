import os

print("\n")

f = open("test.txt", "r+") # r+ = read and write
print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readlines())


# f.write("Hello, world!\n")       # Write string
# f.writelines(["A\n", "B\n"])  # Write list of strings

f.close() # Release file resource

with open("test.txt", "r") as f: # file auto-closed here; Using with (Best Practice)
    data = f.read()
    print(data)

print(os.path.exists("test.txt"))
# os.remove("file.txt")
# os.rename("old.txt", "new.txt")

print("\n")