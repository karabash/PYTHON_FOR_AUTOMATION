#checks only, who have passed the drive test
sorted_data =[]
def sort_passed  (path_of_file, prefix):
 with open(path_of_file) as file:
  for line in file:
       str_split = line.split()
       if (str_split[2].upper() == "p".upper()):
           sorted_data.append(line)
  return sorted_data.sort()

def printer():
    sort_passed("C:/xxxxxx/xxxxxx/Desktop/PYTHON_FOR_AUTOMATION/inputFile.txt", "r")
    print(*sorted_data)  

printer()

#------------------------- reading all lines from inputFile.txt----------------------------------
'''inputFile = open("C:/xxxxx/xxxxx/Desktop/PYTHON_FOR_AUTOMATION/inputFile.txt", "r")
print(inputFile.read())
inputFile.close()'''



