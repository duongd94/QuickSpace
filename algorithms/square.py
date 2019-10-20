# Python3 code for Maximum size 
# square sub-matrix with all 1s 

def printMaxSubSquare(M): 
	R = len(M) # no. of rows in M[][] 
	C = len(M[0]) # no. of columns in M[][] 

	S = [[0 for k in range(C)] for l in range(R)] 
	# here we have set the first row and column of S[][] 

	# Construct other entries 
	for i in range(R): 
		for j in range(C): 
			if (M[i][j] == 1): 
				S[i][j] = min(S[i][j-1], S[i-1][j], 
							S[i-1][j-1]) + 1
			else: 
				S[i][j] = 0

	# for i in range(R): 
		# for j in range(C): 
			# print(S[i][j], end = " ")
		# print("")
	# print("")

	# Find the maximum entry and 
	# indices of maximum entry in S[][] 
	# max_of_s = S[0][0] 
	# max_i = 0
	# max_j = 0
	# for i in range(R): 
	# 	for j in range(C): 
	# 		if (max_of_s < S[i][j]): 
	# 			max_of_s = S[i][j] 
	# 			max_i = i 
	# 			max_j = j 

	# print("Maximum size sub-matrix is: ") 
	# for i in range(max_i, max_i - max_of_s, -1): 
	# 	for j in range(max_j, max_j - max_of_s, -1): 
	# 		print (M[i][j], end = " ") 
	# 	print("") 
	# print("")
	return S

# places the item inside the coordinates of 'coords'
	# then returns the updated matrix 'M'
def place_item(wid, len1, coords, M):
	max_x = 5
	max_y = 5
	print("length: ", len1)
	print("Width: ", wid)

	start = coords['x']
	end = coords['x']-wid
	for i in range(start, end, -1):
		for j in range(coords['y'], coords['y']- len1, -1):
			if M[i][j]:
				M[i][j] = 0
	max_x = len(M)
	max_y = len(M[0])
	for i in range(max_x):
		for j in range(max_y):
			print(M[i][j], end = " ")
		print("")
	print("")

	return M

# gets the coords for an item 
	# TODO: only works with squares for now
def getCoords(wid, len1, M):
	S = printMaxSubSquare(M)
	max1 = findMax(S)
	if max1['max'] >= (len1):
		if max1['max'] >= (wid):
			max1 = max(wid, len1)
			coords = findCoords(S, max1)
			return coords

# checks if there is enough space for the item that is being stored
	# if there is then it returns the coordinate
def findCoords(S, max_dim):
	max_x = len(S)
	max_y = len(S[0])
	
	for i in range(max_x):
		for j in range(max_y):
			if S[i][j] == max_dim:
				return {
					"x": i,
					"y": j
				}
			
# returns the max dimension possible in the matrix
	# 
def findMax(S):
	max1 = 0
	x = 0
	y = 0
	max_x = len(S)
	max_y = len(S[0])
	for i in range(max_x):
		for j in range(max_y):
			if max1 < S[i][j]:
				max1 = S[i][j]
				x = i
				y = j
	# print("")
	# print(max1, x, y)
	max1 = {
		"max": max1,
		"x": x,
		"y": y
	}
	return max1

# Driver Program 
M = [[1, 1, 1, 1, 1, 1], 
	[1, 1, 1, 1, 1, 1], 
	[1, 1, 1, 1, 1, 1], 
	[1, 1, 1, 1, 1, 1], 
	[1, 1, 1, 1, 1, 1], 
	[1, 1, 1, 1, 1, 1]] 

coords = getCoords(3, 3, M)

M = place_item(3, 3, coords, M)

coords = getCoords(2, 2, M)

M = place_item(2, 2, coords, M)


# This code is contributed by Soumen Ghosh 