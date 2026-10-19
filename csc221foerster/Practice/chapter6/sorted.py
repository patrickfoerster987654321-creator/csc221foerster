i = input("Please enter a text file: ")

file = open(i, 'r')
d = {}
line = file.readline()
while line != "":
    d[line] = 1
    line = file.readline()

sorted_list = sorted(d)
output_name = "sorted" + i 
file2 = open(output_name, "w")
for item in sorted_list:
    file2.write(f"{item}")



