from datetime import date
import random


class WareHouse:
    def __init__(self, length, width, total_space, used_space, remain_space):
        self.list = {}
        self.length = length
        self.width = width
        self.total_space = total_space
        self.used_space = used_space
        self.remain_space = remain_space
        self.item = Item()

    def get_total_space(self):
        self.total_space = self.width * self.length
        return self.total_space

    def get_used_space(self):
        for i in self.list:
            self.used_space += self.list[i].item.get_items_size()

    def get_remaining_space(self):
        self.remain_space = self.total_space.get_total_space() - self.get_used_space()
        return self.remain_space


class Item:
    def __init__(self, item_num, item_name, item_type, item_width,
                 item_length, item_size, amount, date_in, date_out, price, owner_name):
        self.item_num = item_num
        self.item_name = item_name
        self.item_type = item_type
        self.item_width = item_width
        self.item_length = item_length
        self.amount = amount
        self.date_in = date_in
        self.date_out = date_out
        self.price = price
        self.owner_name = owner_name
        self.today = date.today()
        self.item_size = item_size

    def item_to_add(self):
        self.item_num = random.randint(1, 10001)  # need to be format to 5digits
        self.item_name = input()
        self.item_type = input()
        self.item_width = int(input())
        self.item_length = int(input())
        self.amount = input()
        self.date_in = self.today.strftime("%m/%d/%Y")
        self.date_out = input()
        self.price = input()
        self.owner_name = input()

    def get_items_size(self):
        self.item_size = self.item_width * self.item_length
        return self.item_size
