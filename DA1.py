import math
list_float = [12.8, 2.3, 2.5, 10.6, 0.0, 11.8, 11.3, 5.8, 4.7, 10.8, 17.3, 0.0, 5.9]

# Display the list in descending order
list_float.sort(reverse = True)
print(list_float)
print("Descending order:")
for float in list_float:
    print(float)

# Calculate average

numbers = len(list_float)
total = sum(list_float)

average = total/len(list_float)
average = round(average, 2)

# Max and min
maximum = round(max(list_float),2)
minimum = round(min(list_float),2)

# Median
median = list_float[(int(len(list_float)/2))]

# Printing all the values
print(f'Average: {average} \nMaximum: {maximum} \nMinimum: {minimum} \nMedian: {median}')