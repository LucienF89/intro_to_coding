####### Notes ###############

# Printing files

# file = "file_name.txt"
# with open(file, 'r') as temp:
#     data = temp.read()  #  .read() returns all data as one string
#     print(data)

    # data_line = temp.readline()  #   .readline returns one line of the data
    # print(data_line)

    # data_list = temp.readlines()  # returns a list with each line, as a string
    # print(data_list)

    # split_data = data.split()
    # print(split_data)

# Printing files, splitting files

# def open_file(filename, option='readlines'): #if you leave the second option empty, it will be read
#     with open(filename, 'r') as f:
#         if option =='read':
#             return f.read()
#         elif option ==  'readlines':
#             return f.readlines()
#         else:
#             return None

# data = open_file('file_name.txt', 'readlines')
# for line in data:
#     print(line.split())

#readlines returns a list

#read returns a string

# Creating new files, writing on files

# def open_file(filename, option='read'):
#     return None

# with open('new_file.txt', 'a') as f:   # w replaces everything in the file, a adds to it
#     text = 'whats up! \n'
#     f.write(text)

# Writing in files

# def write_file(filename, a_string, mode): # mode equals either write or append/ w,a
#     with open(filename, mode) as f:
#         f.write(a_string)

# print(write_file('new_file.txt', "test\n", 'w'))
# print(write_file('new_file.txt', "test", 'a'))


##### Questions ########                                             

#Exercise 1
#Write a function write_file(filename, a_string, mode) 
# that takes the three parameters, as shown, and creates a new file, 
# of the name given as a parameter, and writes the string parameter to that file.  
# We’ll use this function to create the .txt files for the next 6 exercises.


#Exercise 2
#Write a function open_file(filename, mode) 
# that takes the two parameters, as shown, and opens the file, 
# of the name given as a parameter, and returns the output of the preferred mode 
# (‘read’ or ‘readlines’).  
# We’ll use this function to create the .txt files for the next 6 exercises.


# Exercise 3 (use the “FileName” file)
# Write a function, printFile(file), 
# that prints the contents of the file named “filename” to screen. 


# Exercise 4 (use “Sum Column” file)
# Write a function, sumColumn(filename), 
# that should read a file that has exactly one integer on each line 
# and return the sum of these integers. 
# Hint: You will read strings from the file, but want to sum integers.


# Exercise 5 (use “Sum All” file)
# Write a function, sumAll(filename), 
# that should read a file containing only integers 
# and return the sum of all these integers. 
# Hint: Use str.split() to split a line containing multiple integers. 


# Exercise 6 (use “Read Column” file)
# Write a function, readColumn(filename, columnNo). 
# The file named by filename should contain columns of integers separated by whitespace. 
# The function should read the column number columnNo, convert it to integers and return it as a list.


# Exercise 7 (Use zenOfPython.txt file)
# Write a function, countWord(filename, words), 
# that takes a file and a list of words as parameters, 
# counts how many times they exist in filename, 
# and writes the results to a new file, use any name you like for the file.  
# For purposes of this exercise words that are conjunctions can be considered a single word.


########### Work #########

#1

# def write_file(filename, a_string, mode):
#     with open(filename, mode) as f:
#         f.write(a_string)

# print(write_file('new_file.txt', "test", 'w'))

#2

# def open_file(filename, option='readlines'):
#     with open(filename, 'r') as f:
#         if option =='read':
#             return f.read()
#         elif option ==  'readlines':
#             return f.readlines()
#         else:
#             return None

# data = open_file('file_name.txt', 'read')
# print(data)
    

#3

# file = "file_name.txt"
# with open(file, 'r') as temp:
#     data = temp.read()
#     print(data)

#4

# def sum_column(filename):
#     total = 0
#     with open(filename, 'r') as f:
#         for line in f:
#             line = line.strip()
#             if line.isdigit():
#                 total += int(line)
#     return total

# final = sum_column('sum_column.txt')
# print(final)

#5

# def sum_all(filename):
#     total = 0
#     with open(filename, 'r') as file:
#         for line in file:
#             numbers = line.strip().split()
#             for num in numbers:
#                 if num.isdigit():
#                     total += int(num)
#     return total

# print(sum_all('sum_all.txt'))

#6. 

# def readColumn(filename, option='readlines'):
#     empty = []
#     with open(filename, 'r') as file:
#         lines = file.readlines() if option == 'readlines' else [file.read()]
#         for line in lines:
#             words = line.split()
#             for word in words:
#                 if word.isalpha():
#                     empty.append(word)
#                 elif word.isdigit():
#                     empty.append(word)
#     return empty

# print(readColumn('read_column.txt', 'readlines'))



#7.

# def count_words(filename, words):
#     counter = 0
#     with open(filename, 'r') as file:
#         for line in file:
#             line1 = line.strip().split()
#             for word in line1:
#                 if word.lower().strip('.,?!') in words:
#                     counter += 1
#     return counter

# print(count_words('zen_of_python.txt', 'is,than,there'))