# import random

# class RandomizedSet(object):
#     def __init__(self):
#         self.a = set()
        

#     def insert(self, val):
#         if val in self.a:
#             return False
#         self.a.add(val)
#         return True
        

#     def remove(self, val):
#         if val in self.a:
#             self.a.remove(val)
#             return True
#         return False
        

#     def getRandom(self):
#         return random.choice(list(self.a))

import random

class RandomizedSet(object):

    def __init__(self):
        self.val = []
        self.val_index = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_index :
            return False
        self.val.append(val)
        self.val_index[val] = len(self.val) - 1
        return True
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_index :
            return False
        last_val = self.val[len(self.val) - 1]
        index_to_remove = self.val_index[val]
        self.val[index_to_remove] = last_val
        self.val_index[last_val] = index_to_remove
        self.val.pop()
        del self.val_index[val]
        return True


    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.val)