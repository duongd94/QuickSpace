# Python program to find all 
# rectangles filled with 0 
from copy import copy, deepcopy
import array


def findend(i,j,a,output,index): 
	x = len(a) 
	y = len(a[0]) 

	# flag to check column edge case, 
	# initializing with 0 
	flagc = 0

	# flag to check row edge case, 
	# initializing with 0 
	flagr = 0

	for m in range(i,x): 

		# loop breaks where first 1 encounters 
		if a[m][j] == 1: 
			flagr = 1 # set the flag 
			break

		# pass because already processed 
		if a[m][j] == 5: 
			pass

		for n in range(j, y): 

			# loop breaks where first 1 encounters 
			if a[m][n] == 1: 
				flagc = 1 # set the flag 
				break

			# fill rectangle elements with any 
			# number so that we can exclude 
			# next time 
			a[m][n] = 5

	if flagr == 1: 
		output[index].append( m-1) 
	else: 
		# when end point touch the boundary 
		output[index].append(m) 

	if flagc == 1: 
		output[index].append(n-1) 
	else: 
		# when end point touch the boundary 
		output[index].append(n) 


def get_rectangle_coordinates(a): 
	# retrieving the column size of array 
	size_of_array = len(a) 

	# output array where we are going 
	# to store our output 
	output = [] 

	# It will be used for storing start 
	# and end location in the same index 
	index = -1

	for i in range(0,size_of_array): 
		for j in range(0, len(a[0])): 
			if a[i][j] == 0: 

				# storing initial position 
				# of rectangle 
				output.append([i, j]) 

				# will be used for the 
				# last position 
				index = index + 1		
				findend(i, j, a, output, index) 

	print (output) 
	return output


def fill_coord(M, len1, wid1):
	print("-----------------------------------------")
	curr = deepcopy(M)
	coords = get_rectangle_coordinates(M)
	poss = len(coords)
	if len1 < wid1:
		tmp = len1
		len1 = wid1
		wid1 = tmp
	print("ADDING: Len: ", len1, " Wid: ", wid1)
	for i in range(poss):
		maxLen = coords[i][2]+1 - coords[i][0]
		maxWid = coords[i][3]+1 - coords[i][1]
		isHorizontal = True
		if maxLen < maxWid:
			tmp = maxLen
			maxLen = maxWid
			maxWid = tmp
			isHorizontal = False
		print(maxLen, " - ", maxWid)
		print("\n Before storing:")
		for j in range(len(M)):
			for k in range(len(M[0])):
				print(curr[j][k], end=" ")
			print("")
		if len1 <= maxLen:
			if wid1 <= maxWid:
				print("Will fit in warehouse.")
				if isHorizontal or (maxLen >= wid1 and maxWid >= len1):
					print("facing vertically")
					for j in range(len1):
						for k in range(wid1):
							curr[j+coords[i][0]][k+coords[i][1]] = 1

					print("\n After storing:")
					for j in range(len(M)):
						for k in range(len(M[0])):
							print(curr[j][k], end=" ")
						print("")
					return curr

				else:
					print("facing horizontally")
					# TODO: need to fix this
					for j in range(len1):
						for k in range(wid1):
							curr[k+coords[i][0]][j+coords[i][1]] = 1

					for j in range(len(M)):
						for k in range(len(M[0])):
							print(curr[j][k], end=" ")
						print("")
					return curr

			else:
				print("Does not fit")
				return curr
		else:
			print("Does not fit")
			return curr
		

# driver code 
# tests = [ 

# 			[1, 1, 1, 1, 1, 1, 1], 
# 			[1, 1, 1, 1, 1, 1, 1], 
# 			[1, 1, 1, 0, 0, 1, 1], 
# 			[1, 0, 0, 0, 0, 1, 1], 
# 			[1, 0, 0, 0, 0, 1, 1], 
# 			[1, 0, 0, 0, 0, 1, 0], 
# 			[1, 1, 1, 0, 0, 1, 1], 
# 			[1, 1, 1, 1, 1, 1, 1] 

# 		] 

rows = 10
cols = 10

tests = [ [ 0 for i in range(rows) ] for j in range(cols) ]

tests = fill_coord(tests, 3, 2)
tests = fill_coord(tests, 3, 2)
tests = fill_coord(tests, 1, 1)

for i in range(20):
	tests = fill_coord(tests, 3, 2)


# get_rectangle_coordinates(tests) 
