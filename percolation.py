# coding: utf-8
import sys
import numpy as np
import random


class Percolation(object):
    """Percolation
    Args:
        n(int): 构造矩阵的大小，构造成 (n, n)；0表示关闭，1表示打开
    """

    def __init__(self, n):
        self.n = n
        self.data = np.zeros((self.n, self.n))
        # self.data = [[0] * n] * n
        self.cnt = 0
        self.unionSet = {"start":[], "end":[]}

        '''
        your code
        '''

    # 判断系统中放个(row, col)是否是打开状态
    def is_open(self, row, col):
        if self.data[row][col]:
            return True
        return False

    # 打开(row, col)这个格子，状态从0变成1
    def open(self, row, col):
        self.data[row][col] = 1
        if row == 0:
            self.unionSet["start"] = [row, col]
        elif row == self.n - 1:
            self.unionSet["end"] = [row, col]
        else:

        self.cnt += 1

    # 返回打开的格子数
    def number_of_open_sites(self):
        return self.cnt

    # 返回当前系统的状态，是nxn的矩阵
    def get_current_status(self):
        return self.data

    def do_percolation(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.data[i][j]:
                    if i == 0:
                        self.data[i][j] = 2
                    elif j == 0:
                        if self.data[i][j+1] or self.data[i-1][j]:
                            self.data[i][j] = 2
                    elif j == self.n - 1:
                        if self.data[i][j - 1]or self.data[i-1][j]:
                            self.data[i][j] = 2
                    else:
                        if self.data[i][j - 1] or self.data[i][j+1] or self.data[i-1][j]:
                            self.data[i][j] = 2

    # 可视化系统，将满足从上到下系统的格子，进行显示，
    # 你需要将满足从第一行就连通的格子的状态，从1变成2
    def show_percolates(self):
        for i in range(self.n):
            print(self.data[i])

    # 返回true or false，表示当前系统是否是渗透的
    def percolates(self):
        for i in range(self.n):
            if 2 not in self.data[i]:
                return False
        return True

    # 运行模拟实验，每次打开一个格子，直到系统联通; 返回打开的格子个数
    def run(self):
        while not self.percolates():
            row = random.randrange(self.n)
            col = random.randrange(self.n)
            if not self.is_open(row, col):
                self.open(row, col)
            self.do_percolation()
        return self.cnt


class PercolationStats(object):
    def __init__(self, n, t):
        self.n = n
        self.t = t
        pass

    # sample mean of percolation threshold
    # 渗透系统的阈值
    def mean(self):
        return 0.0

    # sample standard deviation of percolation threshold
    # T次实验渗透系统阈值对应的标准差
    def stddev(self):
        return 0.0

    # low endpoint of 95% confidence interval
    # 95置信区间的下届
    def confidenceLow(self):
        return 0.0

    # high endpoint of 95% confidence interval
    # 95置信区间的上届
    def confidenceHigh(self):
        return 0.0

    # 系统会默认调用这个函数进行评测，这个函数必须实现
    # 进行t次模拟实验，需要返回5元组
    # <mean(渗透阈值), std(方差), low_conf(置信区间下界), high_conf(置信区间上界), precolation_status(T次实验中随机一个可视化的状态，需要将能够从上到下渗透的格子从1标记成2)>
    def run(self):
        pass
        # return (mean, std, low_conf, high_conf, precolation_status)


if __name__ == "__main__":
    n = 20
    t = 20
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        t = int(sys.argv[2])
    percolation = Percolation(n)
    percolation.run()
    # percolation.open(0,2)
    # percolation.open(1,2)
    # percolation.open(2,2)
    percolation.show_percolates()
    # print(percolation.percolates())
    # print(percolation.get_current_status())
    # percolation_stats = PercolationStats(n, t)
    # percolation_stats.run()