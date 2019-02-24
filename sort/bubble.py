def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)-1):
            if list[i]>list[j]:
                list[i],list[j] = list[j],list[i]
        print(list)
li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
# print(li)