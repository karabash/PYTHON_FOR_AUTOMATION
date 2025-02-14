from MyParser import parser
import csv

from MyParser as  myParser
class CSVParser(MyParser):
    def __init__(self, filepath, mode):
        self.__filepath = filepath
        self.__mode = mode
        
    def parser(self):    
        csv_reader = csv.reader(self.__filepath, self.__mode)
        headers = next(csv_reader)
        for row in csv_reader:
             row[1] = int(row[1])
             print(row)


    

csvReader =  CSVParser("C:/Users/p901ujk/Desktop/PYTHONFORAUTOMATION/AutomatingDataManipulationAndValidation/CSVgroceries.csv", "r")
