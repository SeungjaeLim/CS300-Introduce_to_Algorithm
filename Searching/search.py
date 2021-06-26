import random

def main():
    print('hello')
    for i in range(-1,10):
        print(i,binary_search([1,3,5,7,9],i))



def linear_search(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
    pass



def binary_search(arr, x):
    l = -1
    r = len(arr)
    while l + 1 < r:
        n = int((l+r)/2)
        if x >= arr[n]:
            l = n
        else:
            r = n
    return r


def distinct(arr):
    p = 0
    y = [0 for i in range(20011)]
    k = random.randrange(1,20011)
    for i in range(len(arr)):
        p = (arr[i]*k)%20011
        while y[p] != 0:
            if y[p] == arr[i]:
                return 0
            p = (p+1)%20011
        y[p] = arr[i]
    return 1
    pass


if __name__ == "__main__":
    main()
