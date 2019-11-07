


class Node:

    def __init__(self, width, height, barcode=None):
        self.left = None
        self.right = None
        self.occupied = False
        self.width =  width
        self.height = height
        self.barcode = barcode
        self.x = None
        self.y = None

class warehouseTree:
    def __init__(self, width, height):
        self.root = Node(width, height)
        self.height = height
        self.width = width

    # TODO: 1. in order to add item, traverse binary tree in postorder.
    #       2. trying to find the very first node that is not occupied.
    #       3. once a node that is not occupied shows up, check to see 
    #            if the dimensions are appropriate
    #       3a. If size is not appropriate then repeat 2-3
    #       3b. If size is appropriate, then begin adding item
                # a. Node width and height are replaced by current item width and height
                # b. Then we split the excess space into 2 separate child nodes.
                #       The right child node should be width = original.width - new.width.... height = new.height
                #       The left child node should be width = original.width.... height = original.height - new.height
    def addItem(self, width, height, barcode):
        # print("addint item...")
        #width=int(width)
        #height=int(height)
        tempAndCoords = self.findSpace(width, height, self.root, 0, 0)
        if not tempAndCoords:
            return False
        temp = tempAndCoords['node']
        originalWidth = temp.width
        originalHeight = temp.height
        # check to see if width and height are appropriate
        # if we get here, it means that the item should fit
        #   so if width or height does not match, then we need to rotate item
        #   which is what the else statement does
        if originalWidth >= width and originalHeight >= height:
            temp.width = width
            temp.height = height
        else:
            temp.width = height
            temp.height = width
        
        # make right and left child nodes, and make temp point to them
        #   only if they have legitimate space available
        
        #print("ow type",str(type(originalWidth)) ,"tempwidth ",str(type(temp.width)))
        rightChild = Node((originalWidth)-(temp.width), (temp.height))
        if rightChild.height > 0 and rightChild.width > 0:
            temp.right = rightChild

        leftChild = Node((originalWidth), (originalHeight)-(temp.height))
        if leftChild.height > 0 and leftChild.width > 0:
            temp.left = leftChild

        # add item barcode which means that item is now occupied so set occupied status to true
        temp.barcode = barcode
        temp.occupied = True
        coords = tempAndCoords['coords']
        temp.x = coords[0]
        temp.y = coords[1]
        return True
        


    def findSpace(self, width, height, temp, x, y):
        # print("finding space...")
        rightResult = False
        leftResult = False
        if (not temp.right == None) and (temp.occupied):
            rightResult = self.findSpace(width, height, temp.right, x+temp.width, y)
        if (not temp.left == None) and (temp.occupied):
            leftResult = self.findSpace(width, height, temp.left, x, y+temp.height)
        
        if (not temp.occupied) and self.fits(width, height, temp):
            tempAndCoords = {
                'node': temp,
                'coords': (x, y)
            }
            return tempAndCoords
        if rightResult:
            if not rightResult['node'].occupied and self.fits(width, height, rightResult['node']):
                return rightResult
        if leftResult:
            if not leftResult['node'].occupied and self.fits(width, height, leftResult['node']):
                return leftResult
        return False

    def fits(self, width, height, temp):
        if width <= temp.width and height <= temp.height:
            return True
        elif width <= temp.height and height <= temp.width:
            return True
        return False

    def itemLoc(self, barcode):
        return self.findCoords(barcode, self.root, 0, 0)

    def findCoords(self, barcode, temp, x, y):
        rightFound = False
        leftFound = False
        if temp.barcode == barcode:
            return (temp.x,temp.y,temp.width+temp.x, temp.height+temp.y,   temp.barcode)
        if temp.right:
            rightFound = self.findCoords(barcode, temp.right, x+temp.width, y)
        if temp.left:
            leftFound = self.findCoords(barcode, temp.left, x, y+temp.height)
        if rightFound:
            return rightFound
        if leftFound:
            return leftFound
        return False

    def rectList(self, rect_list=[], temp=None):
        # tests = [ [ 0 for i in range(self.width) ] for j in range(self.height) ]
        if not temp:
            temp = self.root
        if temp.right:
            # print(temp.barcode)
            self.rectList(rect_list, temp.right)
        if temp.left:
            self.rectList(rect_list, temp.left)
        if temp.occupied:
            rect_list.append((temp.x, temp.y, temp.width, temp.height, temp.barcode))
            return rect_list

    def printWarehouseMatrix(self):
        rect_list = self.rectList()

        tests = [ [ 0 for i in range(self.width) ] for j in range(self.height) ]
        for i in rect_list:
            for j in range(i[2]):# width
                for k in range(i[3]):# height
                    disRow = i[1]
                    disCol = i[0]
                    tests[disRow+k][disCol+j] = i[4]
                    # tests[disCol+j][disRow+k] = 1
        for i in range(self.height):
            for j in range(self.width):
                if not tests[i][j] == 0:
                    print(tests[i][j], end=", ")
                else:
                    print(" ", end=", ")
            print("")

    def printNodes(self):
        self.printPostorder(self.root)
    def printPostorder(self, root): 
        if root: 
            # First recur on left child 
            if root.left:
                self.printPostorder(root.left) 
            # the recur on right child
            if root.right:
                self.printPostorder(root.right) 
            # now print the data of node 
            print(root.barcode," w= ", root.width," h= ", root.height)
        else:
            print(" w= ", root.width," h= ", root.height)


# x = warehouseTree(25, 50)
# x.addItem(10, 20, 1)
# x.printNodes()
# x.addItem(5, 5, 2)
# # x.addItem(5, 5, 3)
# x.addItem(5, 5, 4)
# x.addItem(20, 200, 9)
# # x.addItem(20, 30, 5)
# x.addItem(30, 5, 6)
# # x.addItem(15, 15, 7)
# x.printNodes()

# print(x.itemLoc(1))
# print(x.itemLoc(2))
# print(x.itemLoc(3))
# print(x.itemLoc(4))
# print(x.itemLoc(9))
# print("-------------------------")
# x.printWarehouseMatrix()
# # print(g)