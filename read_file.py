employee_file = open("readfile.txt","r") # r = read, r+ = read + write, w = write, a = append

#print(employee_file.readable()) #Can the file be read?
#print(employee_file.read()) #Reads whole file

#print(employee_file.readline()) #Reads current line and sets next line for read

#print(employee_file.readlines()) #An array of all lines in the file

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
