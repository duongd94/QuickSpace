# from rectpack import newPacker

# rectangles = [(10, 3,1), (4, 6,2), (3, 3,3),(7, 7,4), (10, 5,5), (3, 3,6), (2, 2, 7)]
# bins = [(30, 30)]

# packer = newPacker()

# # Add the rectangles to packing queue
# for r in rectangles:
# 	packer.add_rect(*r)

# # Add the bins where the rectangles will be placed
# for b in bins:
# 	packer.add_bin(*b)

# # Start packing
# packer.pack()

# # Full rectangle list
# all_rects = packer.rect_list()
# print(all_rects)
# for rect in all_rects:
# 	b, x, y, w, h, rid = rect
# 	# print(rect)
# tests = [ [ 0 for i in range(30) ] for j in range(30) ]
# for i in all_rects:
# 	for j in range(i[3]):# width
# 		for k in range(i[4]):# height
# 			disRow = i[2]
# 			disCol = i[1]
# 			tests[disRow+k][disCol+j] = i[5]

# for i in range(30):
# 	for j in range(30):
# 		if not tests[i][j] == 0:
# 			print(tests[i][j], end=", ")
# 		else:
# 			print(" ", end=", ")
# 	print("")
	
# # print(tests)

# rectangles = [(10, 3, 9)]

# packer.add_rect(*rectangles[0])

# packer.pack()
# all_rects = packer.rect_list()
# print("\n\n-----------------------------------------------------------------------------------------\n\n")
# print(all_rects)

# for i in all_rects:
# 	for j in range(i[3]):# width
# 		for k in range(i[4]):# height
# 			disRow = i[2]
# 			disCol = i[1]
# 			tests[disRow+k][disCol+j] = i[5]

# for i in range(30):
# 	for j in range(30):
# 		if not tests[i][j] == 0:
# 			print(tests[i][j], end=", ")
# 		else:
# 			print(" ", end=", ")
# 	print("")


# # b - Bin index
# # x - Rectangle bottom-left corner x coordinate
# # y - Rectangle bottom-left corner y coordinate
# # w - Rectangle width
# # h - Rectangle height
# # rid - User asigned rectangle id or None

# greedypacker.BINSET
BINSET = binpack.BinPack(bin_size=(4,8))
BINSET.insert((2, 4), (2, 2), (4, 5), (4, 4), (2, 2), (3, 2), heuristic='best_fit')
BINSET.print_stats()