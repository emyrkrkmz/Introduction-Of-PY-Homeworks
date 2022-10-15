import csv

tag = input("Enter country tag: ")  # The country tag taken from user.
data_set = ()

average = -1
sum   = -1
maximum = -1

with open('daily-cases-covid-19.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headers = next(csv_reader)
    data_set = tuple(csv_reader)
    

# WRITE YOUR CODE IN THIS RANGE

print(headers)                        # Prints the csv headers. This line can be deleted.      
print(data_set)                       # Prints data. This line can be deleted.








# WRITE YOUR CODE IN THIS RANGE

if average != -1:
    print(f"Average number of cases for the country tagged {tag} : {average}")
    
if sum   != -1:
    print(f"Sum number of cases for the country tagged {tag} : {sum}")
    
if maximum != -1:
    print(f"Maximum number of cases for the country tagged {tag} : {maximum}")
