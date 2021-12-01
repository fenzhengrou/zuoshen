"""
完全二叉树：
在子节点添加新节点时保证前面的节点都不为空
index为i时
左孩子为 i*2 + 1
右孩子为 i*2 + 2
父节点为 (i-1)/2
堆是一种特殊的完全二叉树，分为大根堆和小根堆
大根堆：
每一个子二叉树的根节点都是该二叉树中所有节点的最大值
可以用来求某任意长度数组中的前几个最大值
小根堆：
每一个子二叉树的根节点都是该二叉树中所有节点的最小值
堆排序：
将一个无序数组堆化（大根堆或小根堆）
假设按照大根堆规则排序，先将数组堆化，然后取出二叉树根节点（最大值），然后堆化，再取出根节点（第二大）
以此类推，全部取出后则实现了数组的从大到小排序
"""

from P3 import *
from generator import *

class Heap:
    def __init__(self, arr):
        self.arr = arr
        # pass

    def heap_sort(self):
        """
        时间复杂度 O(NlogN)
        空间复杂度 O(1)
        :param self.arr:
        :return:
        """
        if (not self.arr) or (len(self.arr) < 2):
            return

        # 将数字插入堆中
        # for i in range(len(self.arr)):
        #     self.heap_insert(i)
            # self.heap_sort()
        # 较快一些的方法：从下往上堆化， 时间复杂度为O(N)
        for i in range(len(self.arr)-1, -1, -1):
            self.heapify(i, len(self.arr))

        heapSize = len(self.arr)
        swap(self.arr, 0, heapSize - 1)
        heapSize -= 1
        while heapSize:
            self.heapify(0, heapSize)
            swap(self.arr, 0, heapSize - 1)
            heapSize -= 1

    def heap_insert(self, idx):
        # 如果下标为idx的节点值比其父节点的值大，则将其交换，继续向上比较
        # 不比其父节点的值大时，退出循环
        while self.arr[idx] > self.arr[int((idx - 1) / 2)]:
            swap(self.arr, idx, int((idx - 1) / 2))
            idx = int((idx - 1) / 2)

    def heapify(self, idx, heap_size):
        """
        堆化，从某个idx向下出发，将整个二叉树变成堆的过程
        :param self.arr:
        :param idx:
        :param heap_size:
        :return:
        """
        left = idx*2 + 1  # 左孩子下标
        while left < heap_size:  # 当left < heap_size时说明左孩子下标没有越界，即根节点idx存在一个左孩子

            # 将下标为idx的根节点的左孩子与右孩子进行比较，得到拥有较大值的孩子下标
            largest = left + 1 if left+1 < heap_size and self.arr[left + 1] > self.arr[left] else left

            # 如果较大的孩子值比根节点大，则largest不变，以便后续将其与根节点进行交换，
            # 反之，largest = idx,代表根节点已经是该子二叉树中最大的值了，不需要再进行堆化。后续退出循环
            largest = largest if self.arr[largest] > self.arr[idx] else idx

            if largest == idx:
                break

            # 如果没有退出循环，则将较大的孩子节点与根节点进行交换
            swap(self.arr, largest, idx)

            # 然后根节点的下标变为上一步中较大的孩子节点的下标，继续堆化
            idx = largest

            # left变为新根节点下标的左孩子下标
            left = idx * 2 + 1


def heap_main():
    arr = [7,1,4,2,5,3,9,8,6]
    print(arr)
    heap = Heap(arr)
    heap.heap_sort()
    print(arr)


"""
基于比较的排序：快排，冒泡排序，堆排序灯
不基于比较的排序：桶排序，基数排序
不基于比较的排序适用于数据量有限的情况
"""


def bucket_sort(arr, l, r, bit_num):
    bucket = [0] * (r - l + 1)
    size = 10  # 固定变量，分别代表位数为0-9
    for digit in range (1, bit_num + 1):  # 有多少位，就出入桶多少次
        # count[0] 当前位（d）是0的数字有多少个
        # count[1] 当前位（d）是1的数字有多少个
        # count[2] 当前位（d）是2的数字有多少个
        # count[3] 当前位（d）是3的数字有多少个
        # 以此类推
        count = [0] * size  # 分别存放位数0-9的桶
        for i in range(l, r + 1):
            bit = get_digit(arr[i], digit)
            count[bit] += 1
        for i in range(1, size):
            count[i] += count[i-1]
        for i in range(r, l-1, -1):
            bit = get_digit(arr[i], digit)
            bucket[count[bit] - 1] = arr[i]
            count[bit] -= 1
        j = 0
        for i in range(l, r + 1):
            arr[i] = bucket[j]
            j += 1

    return arr


def get_digit(num, d):
    result = 0
    for i in range(1, d + 1):
        result = num % 10
        num //= 10

    return result


def count_bit(arr):
    max = 0
    for item in arr:

        item = abs(item)
        bit_num = 0
        while item:
            bit_num += 1
            item //= 10

        if bit_num > max:
            max = bit_num
    return max


def absolute(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])


a = 321
print(get_digit(321, 3))
g = Generator(10, 10000)
arr = g.random_generator()
print(arr)
absolute(arr)
print(arr)
bit_num = count_bit(arr)
arr = bucket_sort(arr, 0, len(arr) - 1, bit_num)
print(arr)