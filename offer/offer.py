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
    flag  = 1
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

####二分查找#####
def binary_chop(alist, data):
    n = len(alist)
    first = 0
    last = n - 1
    while first<last:
        mid = (first+last)//2
        if data>alist[mid]:
            first = mid+1
        elif data<alist[mid]:
            last = mid-1
        else:
            return True
    return False

# lis = [2,4, 5, 12, 14, 23]
# print(binary_chop([],14))
#

# if __name__ == '__main__':
#     lis = [2,4, 5, 12, 14, 23]
#     binary_chop(lis, 14)
# def fun():
#
#     temp=[lambda x:x*i for i in range(4)]
#     return temp
# for every in fun():
#     print(every(2))



####字符串最长公共子串
def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    print(record)
    return str1[p - maxNum:p], maxNum

#
# res = getNumofCommonSubstr("assa", "sas")
# print(res)



###快速排序
#QuickSort by Alvin

def QuickSort(myList,start,end):
    i,j = start,end
    base = myList[i]
    while i<j:
        while i<j and myList[j]>=base:
            j = j-1
        myList[i]=myList[j]
        while i<j and myList[i]<=base:
            i=i+1
        myList[j]=myList[i]
    myList[i] = base
    QuickSort(myList,start,i-1)
    QuickSort(myList,j+1,end)

def quick_sort(lst):
    if not lst:
        return []
    pivot = lst[0]
    left = quick_sort([x for x in lst[1:] if x < pivot])
    right = quick_sort([x for x in lst[1:] if x >= pivot])


    return left + [pivot] + right

# myList = [49,38,65,97,76,13,27,49]
# print(quick_sort(myList))
# print("Quick Sort: ")
# QuickSort(myList,0,len(myList)-1)
# print(myList)


#####冒泡排序####
def BubbleSort(myList):
    length = len(myList)
    for i in range(length-1):
        # 注意这个地方，因为还有一个j+1,所以j的取值是length-i-1
        for j in range(length-i-1):
            if myList[j]>myList[j+1]:
                myList[j],myList[j+1] = myList[j+1],myList[j]
        print(myList)
# BubbleSort([49,38,65,97,76,13,27])


#####选择排序######
def Selection_sort(myList):
    length = len(myList)
    # 总共需要length-1次，因为第length次前面的都定了
    for i in range(length-1):
        min_index = i
        for j in range(i,length):
            if myList[j]<myList[min_index]:
                min_index = j
        if min_index != i:
            myList[i],myList[min_index]=myList[min_index],myList[i]
        print(myList)
# Selection_sort([49,38,65,97,76,13,27])



# #####插入排序###
# def insert_sort(myList):
#     length = len(myList)
#     for i in range(1,length):
#         for j in range(i,0,-1):
#             if myList[j]<myList[j-1]:
#                 myList[j],myList[j-1] = myList[j-1],myList[j]
#         print(myList)
# #
def insert_sort(myList):
    length = len(myList)
    for i in range(1,length):
        if myList[i]<myList[i-1]:
            index = i
            temp = myList[i]
            while index>0 and myList[index-1]>temp:
                myList[index]=myList[index-1]
                index = index-1
            myList[index] = temp



# insert_sort([49,38,65,97,76,13,27,49])


######反转链表####



########字符串的全排列######
def Permutation(ss):
    if len(ss) == 0 or len(ss) == 1:
        return ss
    charList = list(ss)
    charList.sort()
    ll = []
    length = len(ss)

    for i in range(length):
        last = Permutation(ss[0:i]+ss[i+1:])




# print(Permutation("aa"))
class Solution:
    def getNumofCommonSubstr(self, str1, str2):
        l1 = len(str1)
        l2 = len(str2)

        maxNum = 0
        flag = 0
        for j in range(l2):
            for i in range(l1):
                lenper = 0
                while i < l1 and j < l2 and str2[j] == str1[i]:
                    j += 1
                    i += 1
                    lenper += 1
                if lenper > maxNum:
                    maxNum = lenper
                    flag = i
        return str1[flag - maxNum:flag], maxNum



# ss = Solution()
# print(ss.getNumofCommonSubstr('ashsjdn','shs'))

####字符全排列
def permutation(s,i):
    if i == len(s):
        print(s)
    else:
        for j in range(i,len(s)):
            s[j],s[i] = s[i],s[j]
            permutation(s,i+1)
            s[j],s[i] = s[i],s[j]
# test = "abc"
# s = list(test) # 字符串转为数组 ["a","b","c"]
# permutation(s,0)

def cut(s: str):
    results = []
    former = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            results.append(s[x:i + x + 1])
            former.append(s[i:i+x+1])
    return results,former


# print(cut('abc'))

####字符串全排列
def Permutation(ss):
    # write code here
    if not ss:
        return []
    if len(ss) == 1:
        return list(ss)

    charList = list(ss)
    charList.sort()
    pStr = []
    for i in range(0, len(charList)):
        if i > 0 and charList[i] == charList[i - 1]:
            continue
        temp = Permutation(''.join(charList[:i]) + ''.join(charList[i + 1:]))
        for j in temp:
            pStr.append(charList[i] + j)

    return pStr
# print(Permutation("abcd"))

def FindGreatestSumOfSubArray( array):
    # write code here
    if not array:
        return 0

    cur_sum = 0
    max_sum = array[0]

    for i in range(len(array)):
        if cur_sum <= 0:
            cur_sum = array[i]
        else:
            cur_sum += array[i]

        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum
# print(FindGreatestSumOfSubArray([3,4,-5]))


######十进制转n进制
def f(x,n):
    l = []
    while x:
        s = x//n
        l.append(x%n)
        x = s
    l.reverse()
    for i in l:
        print(i, end='')
def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])
# print(dec2bin(19))

######二进制转十进制
def bin2dec(x):
    ll = list(str(x))
    result = 0
    for i in range(len(ll)):
        if ll[i]=='1':
            result = result+pow(2,len(ll)-i-1)
    print(result)
bin2dec(10000)



# f(19,2)
import pdb
#####数字在排序数组中出现的次数
class Solution:
    def GetNumberOfK(self, data, k):
        left=0
        right=len(data)-1
        leftk=self.getleftK(data,k,left,right)
        rightk=self.getrightK(data,k,left,right)
        return rightk-leftk+1
    def getleftK(self,data,k,left,right):###查找重复数字中最左边的那个数字位置
        while left<=right:
            middle=(left+right)//2
            if data[middle]<k:
                left=middle+1
            else:
                right=middle-1
        return left
    def getrightK(self,data,k,left,right):###查找重复数字最右边的那个数字位置
        while left<=right:
            middle=(left+right)//2
            if data[middle]<=k:
                left=middle+1
            else:
                right=middle-1
        return right
# c = Solution()
# # print(c.GetNumberOfK([1,2,3,3,3,4,6],4))
# pdb.run(c.GetNumberOfK([1,2,3,3,3,4,6],4))