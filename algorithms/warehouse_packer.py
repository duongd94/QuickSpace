import rectpack
import rectpack.packer as packer
from copy import copy, deepcopy

class warehousePacker:
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.p = packer.newPacker(mode=packer.PackingMode.Online, 
				bin_algo=packer.PackingBin.BFF)
		self.p.add_bin(self.width, self.height)

	def addItem(self, width, height, barcode):
		print("trying to add item width: ", width, ", height: ", height, ", Barcode: ", barcode)
		fits = self.p.add_rect(width, height, barcode)
		if not fits:
			return False
		else:
			return True

	def itemLocation(self, barcode):
		for item in self.p.rect_list():
			if barcode in item:
				return item
		return False
	
	def displayMatrix(self):
		all_rects = self.p.rect_list()
		tests = [ [ 0 for i in range(self.width) ] for j in range(self.height) ]
		for i in all_rects:
			for j in range(i[3]):# width
				for k in range(i[4]):# height
					disRow = i[2]
					disCol = i[1]
					tests[disRow+k][disCol+j] = i[5]
					# tests[disCol+j][disRow+k] = 1
		for i in range(self.height):
			for j in range(self.width):
				if not tests[i][j] == 0:
					print(tests[i][j], end=", ")
				else:
					print(" ", end=", ")
			print("")



# make a warehouse, warehousePacker(width, height)
x = warehousePacker(50, 30)

# addItem(width, height, barcode)
# fits
print("Was the item placed?: ", x.addItem(3, 5, 'd'))
print("Was the item placed?: ", x.addItem(3, 50, 2))
print("Was the item placed?: ", x.addItem(2, 5, 3))
print("Was the item placed?: ", x.addItem(2, 5, 4))
# does not fit 
print("Was the item placed?: ", x.addItem(30, 50, 9))

# list of all items
print("List of all items: ",x.p.rect_list())

# itemLocation(barcode)
# gives the location of the item given the barcode
# returns (ignore, initial_x, initial_y, height, width)
print("location of item with barcode '2': ", x.itemLocation(2))

# displays the current
x.displayMatrix()