def indexEqualsValueSearch(arr):
    left_pointer = 0
    right_pointer = len(arr)-1
    
    while left_pointer < right_pointer:
        mid = (left_pointer + right_pointer)//2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left_pointer = mid + 1
        else:
            right_pointer = mid - 1
    
    
    return -1

arr = [-8,0,2,5] #2
arr2 = [-1,0,3,6] #-1
print(indexEqualsValueSearch(arr))    
print(indexEqualsValueSearch(arr2))

"""""

[-8,0,2,2,3,8,9,]
  i     M     j
  strategy: using two poniters
  1. check the middle value if it equals the index
   middle value == 2
   index == 3
   return index 
  2. if the value at the middle is less than the index
  is 2 less than 3 yes
  3.adjust left to mid + 1
  4. adjust right to mid - 1
"""""

