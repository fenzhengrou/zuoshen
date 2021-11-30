import random

"""
int >> 1 就是除以2， 而且比除以2要快
"""

"""
归并排序
split: 将列表二分成小列表
merge：排序后合并
"""

def split(arr, l, r):
    if l == r:
        return
    mid = l + ((r-l) >> 1)
    split(arr, l, mid)
    split(arr, mid+1, r)
    merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    help = [0] * (r-l+1)
    i = 0
    p1 = l
    p2 = mid+1
    while (p1 <= mid and p2 <= r):
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            p1 += 1
        else:
            help[i] = arr[p2]
            p2 += 1
        i += 1
        # help[i] = arr[p1] if arr[p1] <= arr[p2] else arr[p2]
        # i += 1
        # p1 += 1
        # p2 += 1
    while (p1 <= mid):
        help[i] = arr[p1]
        i += 1
        p1 += 1
    while (p2 <= r):
        help[i] = arr[p2]
        i += 1
        p2 += 1

    for i in range(len(help)):
        arr[l+i] = help[i]


"""
小和问题：
1 3 4 2 5
1的左侧没有比它小的，小和为0
3的左侧有1比它小， 小和为1
4的左侧有1，3比它小，小和为1+3
2的左侧有1比它小，小和为1
5的左侧有1，3，4，2比它小，小和为1+3+4+2
数   小和
1     0
3     1
4     4
2     1
5     10
总共小和为16
也可以看成：
1的右侧，有四个数比它大，所以1会被加四次，即4个1
3的右侧，有两个数比它大，所以3会被加两次，即2个3
4的右侧，有一个数比它大，所以4会被加一次，即1个4
2的右侧，有一个数比它大，所以2会被加一次，即1个2
总共是4+6+4+2 = 16
接下来利用归并排序解决该问题：
在每次merge的时候，由小到大通过比较可以知道较小的数会被加几次，最后可得小和
"""
def small_sum(arr):
    if not arr or len(arr) < 2:
        return 0
    else:
        return split2(arr, 0, len(arr) - 1)


def split2(arr, l, r):
    if l == r:
        return 0  # 此时只有一个数，所以小和为0
    mid = l + ((r-l)>>1)
    return split2(arr, l, mid) + split2(arr, mid+1, r) + merge2(arr, l, mid, r)


def merge2(arr, l, mid, r):
    help = [0] * (r-l+1)
    i = 0
    p1 = l
    p2 = mid+1
    result = 0
    while(p1 <= mid and p2 <= r):
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            result += arr[p1] * (r- p2+ 1)
            p1 += 1
        else:
            help[i] = arr[p2]
            result += 0  # 只用看一个数的右边有没有比它大的，如果右侧的数比该数小，则不用计算小和
            p2 += 1
        i += 1

    while (p1 <= mid):
        help[i] = arr[p1]
        i += 1
        p1 += 1
    while (p2 <= r):
        help[i] = arr[p2]
        i += 1
        p2 += 1

    for i in range(len(help)):
        arr[l+i] = help[i]  # 不能直接+i，会导致arr中的元素被打乱，l代表已经完成排序的部分
    return result


def quick_sort(arr, l, r):
    if l < r:
        idx = random.randint(l, r)
        swap(arr, idx, r)
        interval = partition(arr, l, r)
        quick_sort(arr, l, interval[0] - 1)
        quick_sort(arr, interval[1] + 1, r)


def partition(arr, l, r):
    less = l - 1
    more = r  # 最后一个数为划分值
    while l < more:
        if arr[l] < arr[r]:
            swap(arr, less + 1, l)
            less += 1
            l += 1
        elif arr[l] > arr[r]:
            swap(arr, l, more - 1)
            more -= 1
        else:
            l += 1
    swap(arr, more, r)
    return [less + 1, more]


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def main():
    arr = [3, 6, 2, 5, 7, 5]
    # print(small_sum(arr))
    quick_sort(arr, 0, len(arr) - 1)
    a = [1, 3, 2, 6, 5, 4]
    split(a, 0, len(a)-1)
    print(a)


if __name__ == '__main__':
    main()