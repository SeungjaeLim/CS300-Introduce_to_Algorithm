import math

class Solution(object):
    sol_list = []
    mid_list = []
    min_list = []
    max_list = []
    cnt_range = 0
    def __init__(self, points):
        """
        Initialize this class instance.

        Parameters
        ----------
        points : list of integer coordinates, each of form [x,y], that is
                 [[x1,y1], [x2,y2], ... , [xN,yN]]
        """
        points.sort()
        self.sol_list = [0]*(pow(2,math.ceil(math.log(len(points),2))+1))
        self.mid_list = [0]*(pow(2,math.ceil(math.log(len(points),2))+1))
        self.min_list = [0]*(pow(2,math.ceil(math.log(len(points),2))+1))
        self.max_list = [0]*(pow(2,math.ceil(math.log(len(points),2))+1))
        self.build(0, len(points)-1, 1, points)
        pass

    #build tree of y_subtree
    def build(self, left, right, idx, points):
        if left >= right:
            self.sol_list[idx] = [points[left]]
            self.mid_list[idx] = points[left]
            self.min_list[idx] = points[left]
            self.max_list[idx] = points[left]
            return
        else:
            self.build(left, (left + right)//2, 2 * idx, points)
            self.build((left + right)//2+1, right, 2 * idx + 1, points)
            y_tree = points[left : right + 1]
            self.mid_list[idx] = points[(left+right)//2]
            self.min_list[idx] = points[left]
            self.max_list[idx] = points[right]
            y_tree.sort(key = lambda x : x[1])
            self.sol_list[idx] = y_tree
            return

    def query(self, rect) -> int:
        """
        Find the number of points within the given rectangle

        Parameters
        ----------
        rect: [[xL,xR], [yL,yR]]
              where xL, xR, yL and yR are integers with xL <= xR and yL <= yR

        Returns
        -------
        int
            the number of point (x, y)
            such that xL <= x <= xR and yL <= y <= yR
        """
        self.cnt_range = 0
        self.binsearch_x(1, rect)
        return self.cnt_range

    def binsearch_x(self, idx, rect):
        if self.sol_list[idx] == 0:
            return
        elif self.max_list[idx][0] < rect[0][0]:
            return
        elif self.min_list[idx][0] > rect[0][1]:
            return
        elif self.max_list[idx][0] <= rect[0][1] and self.min_list[idx][0] >= rect[0][0]:
            self.cnt_range = self.cnt_range + self.query_y(rect, self.sol_list[idx])
        else:
            self.binsearch_x(2*idx, rect)
            self.binsearch_x(2*idx+1, rect)



    def query_y(self, rect, y_tree) -> int:
        l = self.binary_search(y_tree, rect[1][0])
        r = self.binary_search(y_tree, rect[1][1] + 1)
        if r-l <= 0:
            return 0
        else:
            return r-l

    def binary_search(self, arr, y):
        l = -1
        r = len(arr)
        while l + 1 < r:
            n = int((l+r)/2)
            if y > arr[n][1]:
                l = n
            else:
                r = n
        return r


if __name__ == "__main__":
    # sample 1
    points = [[1, 1], [3, 3], [2, 2], [1, 3]]
    sol = Solution(points)
    print(sol.query([[1,3], [1,3]]))
    print(sol.query([[1,5], [2,5]]))
