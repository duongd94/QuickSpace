import sys
import unittest
sys.path.insert(1, '../')
import items

class TestItems(unittest.TestCase):

    def test_item_add_only_if_fits(self):
        # Assume
        
        width = 10
        height = 30
        name = "testing warehouse item add"
        warehouse = items.WareHouse(height, width, name)
        itemWidths = [5, 20, 10, 25]
        itemHeight = [10, 20, 15, 5]
        itemNames = ['Paper', 'Stapler', 'Television', 'Radio']

        # Action Add Item w = 5, h = 10: Will fit
        result = warehouse.addItem(itemNames[0], itemWidths[0], itemHeight[0])
        # Assert
        self.assertTrue(result)

        # Action Add Item w = 20, h = 20: Will not fit
        result = warehouse.addItem(itemNames[1], itemWidths[1], itemHeight[1])
        # Assert
        self.assertFalse(result)

        # Action Add Item w = 10, h = 15: Will fit
        result = warehouse.addItem(itemNames[2], itemWidths[2], itemHeight[2])
        # Assert
        self.assertTrue(result)

        # Action Add Item w = 25, h = 5: Will not fit
        result = warehouse.addItem(itemNames[2], itemWidths[2], itemHeight[2])
        # Assert
        self.assertFalse(result)

    def test_usedSpace_and_remainingSpace_accuracy(self):
        #Assume
        width = 10
        height = 30
        name = "testing warehouse Remaining & Used Space"
        warehouse = items.WareHouse(height, width, name)
        itemWidths = [5, 10, 5]
        itemHeight = [10, 15, 5]
        itemNames = ['Paper', 'Stapler', 'Television', 'Radio']
        
        # Action no items are in warehouse
        usedSpaceResult = warehouse.usedSpace()
        self.assertEqual(usedSpaceResult, 0)

        remainingSpaceResult = warehouse.remainingSpace()
        self.assertEqual(remainingSpaceResult, 300)

        # Action Add Item w = 5, h = 10: Will fit
        warehouse.addItem(itemNames[0], itemWidths[0], itemHeight[0])

        usedSpaceResult = warehouse.usedSpace()
        self.assertEqual(usedSpaceResult, 50)

        remainingSpaceResult = warehouse.remainingSpace()
        self.assertEqual(remainingSpaceResult, 250)

        # Action Add Item w = 10, h = 15: Will fit
        warehouse.addItem(itemNames[1], itemWidths[1], itemHeight[1])
        usedSpaceResult = warehouse.usedSpace()
        self.assertEqual(usedSpaceResult, 200)

        remainingSpaceResult = warehouse.remainingSpace()
        self.assertEqual(remainingSpaceResult, 100)

        # Action Add Item w = 5, h = 5: Will fit
        warehouse.addItem(itemNames[2], itemWidths[2], itemHeight[2])
        usedSpaceResult = warehouse.usedSpace()
        self.assertEqual(usedSpaceResult, 225)

        remainingSpaceResult = warehouse.remainingSpace()
        self.assertEqual(remainingSpaceResult, 75)



        

        # warehouse.addItem(itemNames[i], itemWidths[i], itemHeight[0])
        # result = warehouse.totalSpace()
        
if __name__ == '__main__':
    unittest.main()