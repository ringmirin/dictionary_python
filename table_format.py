####write a pytho program to print dictionary in a table format
dict1 = {'NAME': ['John', 'Tim', 'Steve'],
         'AGE': [21, 20, 21],
         'COURSE': ['Data Structures', 'Machine Learning', 'OOPS with Java']}

for each_row in zip(*([i] + (j)
                      for i, j in dict1.items())):
    print(*each_row," ")



dict1 = {1:["John", 21, 'CS'],
          2: ["Tim", 20, 'EE'],
          3: ["Steve", 21, 'Civil'],
         }

# Print the names of the columns.
print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

# print each data item.
for key, value in dict1.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course))


