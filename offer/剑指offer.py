def Find(target, array):
    # write code here
    # write code here
    n = len(array)
    flag = "false"
    for i in range(n):
        if target in array[i]:
            flag = "true"
            break

    return flag
# print(Find(5,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
def replaceSpace(s):
    # write code here
    # print(s.split())
    return "%20".join(s.split(" "))
# print(replaceSpace("哈哈哈哈 iiiii"))


def reverse(l):
    print(l[::-1])
# reverse([1,2,3])
def StrToInt(s):
    num = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9","+","-"]
    flag  = q
    sum = 0
    for i in s:
        if i in num:
            if i=="-":
                flag = -1
            elif i =="+":
                flag = 1
            else:
                sum = sum * 10 + num.index(i)
        else:
            return 0
    return flag*sum
# print(StrToInt("123"))
def maxInWindows(num, size):
    if size <= 0:
        return []
    res = []
    for i in range(len(num) - size + 1):
        res.append(max(num[i:size + i]))
    return res
# x = maxInWindows([2,3,4,2,6,2,5,1],8)
# print(x)
def FindNumbersWithSum(array, tsum):

    a = []
    for i,item in enumerate(array):
        if tsum-item in array[i+1:]:
            a.append([item,tsum-item])

    if a !=[]:
        return a[0]
    else:
        return a
# x = FindNumbersWithSum([],5)
# print(x)
# ll = [1,2,3,3]
# print(ll[0:])
def FindGreatestSumOfSubArray(array):
    sum = array[0]
    for i in range(1,len(array)):
        if sum + array[i] <array[i]:
            return i
        else:
            sum = sum+array[i]

# x = FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2])
# print(x)
# x=[[1,2,3],[2,3,4],[3,4,5]]
# print(len(x))
# def printMatrix(matrix):
#     row = len(matrix)
#     col = len(matrix[0])
#     ll = []
#     for i in range(col):
#         ll.append(matrix[0][i])
#         ll.append(matrix[1])
#
# print ("%d" % 0xFFFFFFFF)
# print ("%x" % -0xFFFFFFFF)
# print ("%x" % -10)
# def binary_chop(alist, data):
#     """
#     非递归解决二分查找
#     :param alist:
#     :return:
#     """
#     n = len(alist)
#     first = 0
#     last = n - 1
#     while first<last:
#         mid = (first+last)//2
#         if data>alist[mid]:
#             first = mid+1
#         elif data<alist[mid]:
#             last = mid-1
#         else:
#             return True
#     return False
#
# if __name__ == '__main__':
#     lis = [2,4, 5, 12, 14, 23]
#     binary_chop(lis, 14)
def fun():

    temp=[lambda x:x*i for i in range(4)]
    return temp
for every in fun():
    print(every(2))
