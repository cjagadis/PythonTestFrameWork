'''The function check two Json database
   If there is perfect match the test is a success
   Input: product Json, Test Json
   Return: "Data Match" if the both Json data sets match
           "Prod Shcema has more fields" if prod has more fields than dev
		   "Prod Schema has less fields" if prod has less fields than test
		   "Key Missing in Test" if test keys does not match with prod keys
		   "Data Miscmatch" - test differs from prod though number of key value pairs are same
''' 
def checkJson(prod, test):
	jsprod = prod
	jstest = test
	i = len(jsprod)
	j = len(jstest)
    
    # Check if both prod and test match
	if i > j:
		return("Prod Schema is Greater than Test Schema")
	elif i < j:
		return("Prod Schema is smaller than Prod Schema")
    
    # Check if all prod keys match with test keys
	for key in jsprod:
		if (key not in jstest):
			return("Key missing in Test")

	for key in jsprod:
		if jsprod[key] != jstest[key]:
			return("Data Mismatch")
	return("Data Match")

	
'''Read a single database Schema from a file.
   Reach the entire file and split them into rows
   From the rown extract relevant columns
   And from these columns build a Json file
   Input: Schema file name
   Output: Json file of the schema
'''
def readFileDBSchema(file):
    text = open(file, "r").read()
    metadata = {}
    myRows = text.split("\n")      #this method tells Python to split your filetest object each time it encounters a line break 
    myRowLen = len(myRows)
    i = 0
    for row in myRows:
        myColumns = row.split()   #this method will consider each of your rows one at a time.
        if i == 0:
            key=myColumns[1]
            value=myColumns[2]
            metadata[key] = value
        elif i < myRowLen-1:
            key=myColumns[0]
            value=myColumns[1]
            metadata[key] = value
        i = i+1
    return(metadata)

# Test - Data Match

dbFileName = "C:\Apps\schemaprod.txt"
metadata1 = readFileDBSchema(dbFileName)
dbFileName = "C:\Apps\schemadev.txt"
metadata2 = readFileDBSchema(dbFileName)
res = checkJson(metadata1, metadata2)
print(res)

# Test - Prod Schema has more fields
dbFileName = "C:\Apps\schemaprod.txt"
metadata1 = readFileDBSchema(dbFileName)
dbFileName = "C:\Apps\schemadevsmall.txt"
metadata2 = readFileDBSchema(dbFileName)
res = checkJson(metadata1, metadata2)
print(res)

# Test - Test Schema has more fields
dbFileName = "C:\Apps\schemaprod.txt"
metadata1 = readFileDBSchema(dbFileName)
print(metadata1)
dbFileName = "C:\Apps\schemadevlarge.txt"
metadata2 = readFileDBSchema(dbFileName)
print(metadata2)
res = checkJson(metadata1, metadata2)
print(res)


# Test - Test Schema has data value mismatch
dbFileName = "C:\Apps\schemaprod.txt"
metadata1 = readFileDBSchema(dbFileName)
print(metadata1)
dbFileName = "C:\Apps\schemadevmismatch.txt"
metadata2 = readFileDBSchema(dbFileName)
print(metadata2)
res = checkJson(metadata1, metadata2)
print(res)

# Test - Test Schema key does not match with prod key
dbFileName = "C:\Apps\schemaprod.txt"
metadata1 = readFileDBSchema(dbFileName)
print(metadata1)
dbFileName = "C:\Apps\schemakeymismatch.txt"
metadata2 = readFileDBSchema(dbFileName)
print(metadata2)
res = checkJson(metadata1, metadata2)
print(res)
