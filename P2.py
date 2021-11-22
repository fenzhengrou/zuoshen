from generator import *
# 异或运算
# 相同则为0， 不相同则为1 / 不进位相加
# 满足交换律， 结合律 a ^ b = b ^ a, a ^ b ^ c = a ^ c ^ b
# a^0 = a, a^a = 0

def swap(arr, i, j):
    """
    第一次： i = i^j
    第二次： j = i^j = i^j^j = i^0 = i
    第三次： i^j = i^j^i = 0^j = j
    交换完成，不需要新建内存
    当两个变量指向同一地址时，不适用（地址自己^自己 = 0）
    相当于^操作是针对地址进行的
    :param i:
    :param j:
    :return:
    """
    # print(f"i is {arr[i]}, j is {arr[j]}")
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]
    # print(f"i is {arr[i]}, j is {arr[j]}")


def get_right_one(num):
    """
    得到一个数最右侧的1
    a = 1010101100
    ~a(取反) = 0101010011
    ~a+1 = 0101010100
    a and (~a+1) = 0000000100
    :param num:
    :return:
    """
    tmp = (~num) + 1
    result = tmp & num
    return result


def find_num():
    """
    如果一个数组中，一个数出现了奇数次，其他数都是偶数次，找出出现奇数次的数
    :return:
    """
    a = [1,1,1,1,2,2,3,3,3]
    tmp = 0
    for i in a:
        tmp^=i
    print(tmp)


def find_num2():
    """
    一个数组中两个数出现了奇数次，其他数都出现了偶数次，找出这两个数
    先把所有的数异或一遍，得到eor = a^b，偶数次的数异或起来全是0，两个不同的奇数次的数异或起来，在二进制上必定有一位是1（假设第8位）
    （因为不同，所以二进制上有且至少有一位是不同的，异或 = 1）
    于是整个数组可以被分为两类：A，第八位为1的；B，第八位为0的（两类中a和b必定不为同一类）
    于是类A和类B就成了两个数组，每个数组中只有一个数出现了奇数次，其他都是偶数次
    令新变量eor'与其中任意一类中的所有数异或，可以得到 a 或 b 中的一个,假设得到a
    eor' ^ eor = a ^ a ^ b = b, 得到另一个数
    :return:
    """
    a = [1,2,2,4,4,4,4,5,5,5,5,5]
    eor = 0
    for i in a:
        eor ^= i
    right_one = get_right_one(eor)
    eor2 = 0
    for i in a:
        if i&right_one == right_one: # = 0/right_one
            eor2 ^= i
    another = eor ^ eor2
    print(f"one of them is {eor2}, another one is {another}")


def bubble_sort(arr):
    # print(f"before sorting: {arr}")
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                swap(arr, i, j)

    # print(f"after sorting: {arr}")


def insert_sort(arr):
    # print(f"before sorting: {arr}")
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] < arr[j] and (j-1) >= 0:
                break
            else:
                swap(arr,j, j-1)
    # print(f"after sorting: {arr}")


def bi_find(arr, n):
    """
    二分法找到大于等于一个数的最左边的位置
    :param arr:
    :return:
    """
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    if arr[mid] >= n:
        return bi_find(arr[0:mid], n)
    else:
        return bi_find(arr[mid:], n)


def main():
    times = 10
    flag = True
    for i in range(times):
        g = Generator(1000,100)
        arr = g.random_generator()
        cpy_arr = g.cpy_arr(arr)
        cpy_arr.sort()
        insert_sort(arr)
        for j in range(len(arr)):
            if arr[j] != cpy_arr[j]:
                flag = False
                break
    print("Nice" if flag else "Error")

    # swap(3,5)
    # find_num()
    # get_right_one(5)
    # find_num2()
    # arr = [0,1,2,5,6,7,8]
    # arr = [7,6,5,2,1,0,8]
    # insert_sort(arr)
    # bubble_sort(arr)
    # print(bi_find(arr, 4))


if __name__ == "__main__":
    main()