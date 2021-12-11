# Row with max 1s

# Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

array = [[0, 1, 1, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]

count_1s = 0
min_index = -1

for index in range ( 0 , len ( array ) ) :
    temp = array [ index ] .count ( 1 )
    if temp > count_1s :
        count_1s = temp
        min_index = index

print ( min_index )