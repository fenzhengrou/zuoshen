import random


class Generator:
    def __init__(self, max_length, max_value):
        self.max_length = max_length
        self.max_value = max_value
        self.arr = []
        self.arr_cpy = []

    def cpy_arr(self, arr):
        if len(arr) == 0:
            return []
        self.arr_cpy = [0] * len(arr)
        for i in range(len(arr)):
            self.arr_cpy[i] = arr[i]
        return self.arr_cpy

    def random_generator(self):
        # self.max_length = int((self.max_length+1)*random.random())
        len = random.randint(0,self.max_length) + 1
        self.arr = [0]*len
        for i in range(len):
            value = random.randint(0, self.max_value) - random.randint(0, self.max_value)
            # value = int((self.max_value+1) * random.random() - (self.max_value+1) * random.random())
            self.arr[i] = value

        return self.arr


# g = Generator(1000,100)
# lst = g.random_generator()
# cpy = g.cpy_arr(lst)
# print(1)