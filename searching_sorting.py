# Linear Searching
# Binary

# Sleep Sort
# Monkey Sort
# Bubble Sort
# Selection
# Merge Sort
# Quick Sort
# Insertion Sort
     

#? Linear Search
# Brute Force

def linear_search(arr,item):

  for i in range(len(arr)):

    if arr[i] == item:
      return i

  return -1
     

arr = [12,34,56,1,67,100,47,99]

linear_search(arr,121)

# Time Complexity is O(N)
# No sorting required
     

#? Binary Search
# Sorted Array 

def binary_search(arr, low, high, item):

  if low <= high:
    # search

    mid = (low + high)//2

    if arr[mid] == item:
      return mid
    elif arr[mid] > item:
      return binary_search(arr, low, mid-1,item)
    else:
      return binary_search(arr,mid+1,high,item)
  else:
    return -1
     

arr = [12,24,35,46,57,68,80,99,100]
print(binary_search(arr,0,len(arr)-1,-5))

# Sorting

def is_sorted(arr):

  sorted = True

  for i in range(len(arr) - 1):
    if arr[i]>arr[i+1]:
      sorted = False
  
  return sorted
     

arr = [1,2,3,4,8,6]
is_sorted(arr)

#? Monkey sort

import random

a=[1,2,3,4]
random.shuffle(a)
a
     
[2, 1, 3, 4]

import time


def monkey_sort(arr):

  while not is_sorted(arr):
    time.sleep(1)
    random.shuffle(arr)
    print(arr)
  print(arr)
     

a = [12,24,11,56,34,20]
monkey_sort(a)
     

#? bubble sort
def bubble_sort(arr):

  for i in range(len(arr) - 1):
    flag = 0
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
        flag =1

    if flag == 0:
      break
  
  return arr
     

arr = [23,12,34,11,100,56,78]
bubble_sort(arr)
     

#? selection sort
def selection_sort(arr):

  for i in range(len(arr) - 1):

    min = i

    for j in range(i+1,len(arr)):
      if arr[j] < arr[min]:
        min = j
    
    arr[i],arr[min] = arr[min],arr[i]

  return arr


     

arr = [23,12,34,11,100,56,78]
selection_sort(arr)
     

L = []

import random

for i in range(10000):
  L.append(random.randint(1,10000))
     

len(L)
     
10000

L1 = L[:]
# cloning
     

import time

start = time.time()
bubble_sort(L)
print("Time taken",time.time() - start,"secs")
     

start = time.time()
selection_sort(L1)
print("Time taken",time.time() - start,"secs")

# Not Adaptive

#? Merge Sort
    
def merge_arrays(arr1, arr2):
    i = 0
    j = 0
    new_arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        new_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        new_arr.append(arr2[j])
        j += 1

    return new_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_arrays(left, right)

# Example usage
arr1 = [1, 2, 6, 7, 8]
arr2 = [2, 3, 5]

print(merge_arrays(arr1, arr2))  # Output: [1, 2, 2, 3, 5, 6, 7, 8]

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [3, 9, 10, 27, 38, 43, 82]

def merge_arrays(arr1, arr2, arr):
    i = 0
    j = 0
    k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge_arrays(left, right, arr)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)  # Output: [3, 9, 10, 27, 38, 43, 82]


#? quick sort     

def quick_sort(arr):

  if len(arr) <= 1:
    return arr

  pivot = arr.pop()

  items_left = []
  items_right = []

  for item in arr:
    if item < pivot:
      items_left.append(item)
    else:
      items_right.append(item)

  return quick_sort(items_left) + [pivot] + quick_sort(items_right)



     

arr = [2,1,4,6,3,7,5]
quick_sort(arr)
     

def quick_sort(arr,low,high):

  if len(arr) == 1:
    return arr

  if low < high:

    pi = partition(arr,low,high)

    quick_sort(arr,low,pi-1)
    quick_sort(arr,pi+1,high)
     

def partition(arr,low,high):

  i = low - 1
  pivot = arr[high]

  for j in range(low,high):

    if arr[j] <= pivot:
      i+=1
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[high] = arr[high],arr[i+1]

  return i+1
     

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quick_sort(arr, 0, n-1)
print(arr)
     
