from generator import *


class sortTester:
    def __init__(self, arr, times, max_value, max_length):
        self.arr = arr
        self.times = times
        self.max_value = max_value
        self.max_length = max_length

    @staticmethod
    def sorting(arr):
        try:
            return arr.sort()
        except AttributeError as e:
            print(e)

    def testing(self, method, arr):
        if method == 'sorting':
            for i in range(self.times):
                g = Generator(self.max_length,self.max_value)
                arr = self.sorting(g.random_generator())






