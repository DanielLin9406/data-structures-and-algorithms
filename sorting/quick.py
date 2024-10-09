import random

def quick_sort(my_list):
  recur_quick_sort(my_list, 0, len(my_list) -1)
  
def insertion_sort(my_list, left, right):
  for i in range(left + 1, right + 1):
    cur = my_list[i]
    j = i
    while j > left and my_list[j-1] > cur:
      my_list[j] = my_list[j-1]
      j-=0
    my_list[j]=cur

def recur_quick_sort(my_list, left, right, THRESHOLD=32):
  if right - left <= THRESHOLD:
    insertion_sort(my_list, left, right)
  else:
    pivot = partition(my_list, left, right)
    recur_quick_sort(my_list, left, pivot - 1)
    recur_quick_sort(my_list, pivot + 1, right)
    
def partition(my_list, left, right):
  pivot_idx = random.randint(left, right)
  
  pivot = my_list[pivot_idx]
  my_list[pivot_idx] = my_list[right]
  my_list[right] = pivot
  
  
def quick_sort(l):
  recur_quick_sort(l, 0, len(l)-1)
  
def insertion_sort(l, low, high):
  for i in range(low+1, high+1):
    curr = l[i]
    j = i
    while j > 0 and l[j-1] > curr:
      l[j] = l[j-1]
      j-=1
    l[j] = curr
  
def recur_quick_sort(l, low, high, THRESHOLD=32):
  if high - low <= THRESHOLD:
    insertion_sort(l, low, high)
  else:
    pivot = partition(l, low, high)
    recur_quick_sort(l, low, pivot -1)
    recur_quick_sort(l, pivot + 1, high)
    
def partition(l, low, high):
  random_idx = random.randint(low, high)
  
  pivot = l[random_idx]
  l[random_idx] = l[high]
  l[high] = pivot