


class Node:

    def __init__(self, width, height, barcode=None):
        self.left = None
        self.right = None
        self.occupied = False
        self.width =  width
        self.height = height
        self.barcode = barcode

class warehouseTree:
    def __init__(self, width, height):
        self.root = Node(width, height)

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
        print("addint item...")
        temp = self.findSpace(width, height, self.root)
        if not temp:
            return False
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
        rightChild = Node(originalWidth-temp.width, temp.height)
        if rightChild.height > 0 and rightChild.width > 0:
            temp.right = rightChild

        leftChild = Node(originalWidth, originalHeight-temp.height)
        if leftChild.height > 0 and leftChild.width > 0:
            temp.left = leftChild

        # add item barcode which means that item is now occupied so set occupied status to true
        temp.barcode = barcode
        temp.occupied = True
        return True
        


    def findSpace(self, width, height, temp):
        print("finding space...")
        rightResult = False
        leftResult = False
        if (not temp.right == None) and (temp.occupied):
            rightResult = self.findSpace(width, height, temp.right)
        if (not temp.left == None) and (temp.occupied):
            leftResult = self.findSpace(width, height, temp.left)
        
        if (not temp.occupied) and self.fits(width, height, temp):
            return temp
        if rightResult:
            if not rightResult.occupied and self.fits(width, height, rightResult):
                return rightResult
        if leftResult:
            if not leftResult.occupied and self.fits(width, height, leftResult):
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
            return (x, y)
        if temp.right:
            rightFound = self.findCoords(barcode, temp.right, x+temp.width, y)
        if temp.left:
            leftFound = self.findCoords(barcode, temp.left, x, y+temp.height)
        if rightFound:
            return rightFound
        if leftFound:
            return leftFound
        return False



    def printWarehouse(self):
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


x = warehouseTree(25, 50)
x.addItem(10, 20, 1)
x.printWarehouse()
x.addItem(5, 5, 2)
x.addItem(5, 5, 3)
x.addItem(5, 5, 4)
x.addItem(20, 200, 9)
x.printWarehouse()

print(x.itemLoc(3))
print(x.itemLoc(1))
print(x.itemLoc(4))
print(x.itemLoc(9))
