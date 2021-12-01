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


class Heap:
    def __init__(self):
        pass

    def heap_sort(self, arr):
        """
        时间复杂度 O(NlogN)
        空间复杂度 O(1)
        :param arr:
        :return:
        """
        if not arr or len(arr) < 2:
            return

        # 将数字插入堆中
        for i in range(len(arr)):
            self.heap_sort(arr)

        heapSize = len(arr)
        swap(arr, 0, heapSize - 1)
        heapSize -= 1
        while heapSize:
            self.heapify(arr, 0, heapSize)
            swap(arr, 0, heapSize - 1)
            heapSize -= 1

    def heap_insert(self, arr, idx):
        # 如果下标为idx的节点值比其父节点的值大，则将其交换，继续向上比较
        # 不比其父节点的值大时，退出循环
        while arr[idx] > arr[int((idx - 1) / 2)]:
            swap(arr, idx, int((idx - 1) / 2))
            idx = int((idx - 1) / 2)

    def heapify(self, arr, idx, heap_size):
        """
        堆化，从某个idx向下出发，将整个二叉树变成堆的过程
        :param arr:
        :param idx:
        :param heap_size:
        :return:
        """
        left = idx*2 + 1  # 左孩子下标
        while left < heap_size:  # 当left < heap_size时说明左孩子下标没有越界，即根节点idx存在一个左孩子

            # 将下标为idx的根节点的左孩子与右孩子进行比较，得到拥有较大值的孩子下标
            largest = left + 1 if left+1 < heap_size and arr[left + 1] > arr[left] else left

            # 如果较大的孩子值比根节点大，则largest不变，以便后续将其与根节点进行交换，
            # 反之，largest = idx,代表根节点已经是该子二叉树中最大的值了，不需要再进行堆化。后续退出循环
            largest = largest if arr[largest] > arr[idx] else idx

            if largest == idx:
                break

            # 如果没有退出循环，则将较大的孩子节点与根节点进行交换
            swap(arr, largest, idx)

            # 然后根节点的下标变为上一步中较大的孩子节点的下标，继续堆化
            idx = largest

            # left变为新根节点下标的左孩子下标
            left = idx * 2 + 1