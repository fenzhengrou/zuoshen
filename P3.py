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


a = [1, 3, 2, 6, 5, 4]
split(a, 0, len(a)-1)
print(a)
