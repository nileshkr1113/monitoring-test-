Build_Result = 'FAILURE'
string1 = 'The Excel sheet was not created'
string2 = 'The Excel sheet is empty!'
string3 = 'There are currently no messaging engines in bus'
string4 = 'WebSphere Servers are not up! Please check'
string5 = 'It was not possible to contact any of the specified bootstrap servers'
string6 = 'A timeout occurred while remotely browsing destination'
string7 = 'An exception was received during the call to the method createBrowserSession'

# opening a text file
file1 = open('C:\\Users\\003EKW744\Desktop\\Script\\abc.txt', 'r')

# read file content
readfile = file1.read()

# checking condition for string found or not
if string1 in readfile:
	print(Build_Result)
elif string2 in readfile:
    print(Build_Result)
elif string3 in readfile:
    print(Build_Result)
elif string4 in readfile:
    print(Build_Result)
elif string5 in readfile:
    print(Build_Result)
elif string6 in readfile: 
    print(Build_Result)
elif string7 in readfile:
    print(Build_Result)
    
else:
	print('SUCCESS')

# closing a file
file1.close()
