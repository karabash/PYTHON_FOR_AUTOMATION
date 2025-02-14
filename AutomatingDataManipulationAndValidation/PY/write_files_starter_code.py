fail_list = []
pass_list = []
def sort_File(path_of_file):
# open inputFile.txt with the intention of reading it
    readPrefix = "r"
    with open(path_of_file, readPrefix) as inputFile:
         for line in inputFile:
             line_split = line.split() 
             if(line_split[2].upper() == "P"):
                 pass_list.append(line)
             else:              
                 fail_list.append(line)
             
def writeFile(file_Name_Pass, file_Name_Fail):               
    writePrefix = "w"      
    format_type = ".txt"
# open passFile.txt with the intention of writing it
    passFile = open ( (file_Name_Pass+format_type), writePrefix)
    pass_list.sort()
    passFile.writelines(pass_list)     
    passFile.close() 

# open failFile.txt with the intention of writing it
    failFile = open( (file_Name_Fail+format_type), writePrefix)
    fail_list.sort()
    failFile.writelines(fail_list)
    failFile.close()

# main method
def runner():
    sort_File("C:/xxxxxx/xxxxx/Desktop/PYTHON_FOR_AUTOMATION/inputFile.txt")
    writeFile("passFile", "failFile")

runner()