from pathlib import Path
import csv
import os
import json
import xml.etree.ElementTree as ET

class ParZer:

   def checkFormat(filePath):
        ext = os.path.splitext(filePath)[-1].lower()
        return ext

   def openFile(filePath, mode):
       with open(filePath, mode) as file:
         formatType = ParZer.checkFormat(filePath)
         print(formatType)
         if(formatType == ".txt"):
                data = file.read()
                print("data:", data)
                parsed_data = data.split(", ")
                print("parsed data:", parsed_data)
                print("item at index 2:", parsed_data[2])
         elif formatType == "csv":
                csv_reader = csv.reader(file)
                headers = next(csv_reader)
                for row in csv_reader:
                    row[1] = int(row[1])
                    print(row)
         elif formatType == ".json":
                 data = file.read()
                 parsed_data = json.loads(data)
                 print("apples quantity:", parsed_data["apples"])
         elif formatType == ".xml":
              tree = ET.parse(filePath)
              root = tree.getroot()
              items_over_6 = []             
              for item in root.findall("grocery_item"):
                  name = item.find("name").text
                  price = item.find("price").text
                  if( float(price) > 6.00 ):
                      items_over_6.append(name)     
                  print(name, price)
              print("items with price higher than 6.00:", items_over_6)    


ParZer.openFile("C:/XXX/XXXX/XXXX/PYTHONFORAUTOMATION/AutomatingDataManipulationAndValidation/XML/groceries.xml", "r") 


