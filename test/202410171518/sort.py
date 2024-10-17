def bubble_sort(l):
  for i in range(len(l)-1):
    for j in range(len(l)-i-1):
      if l[j] > l[j+1]:
        l[j+1], l[j] = l[j], l[j+1]
        
def selection_sort(l):
  for i in range(0, len(l)-1):
    pivot = i
    for j in range(i+1, len(l)):
      if l[j] < l[pivot]:
        pivot = j
    if pivot != i:
      l[pivot], l[i] = l[i], l[pivot]
      
def insertion_sort(l):
  for i in range(1, len(l)):
    cur = l[i]
    j=i
    while j>0 and l[j-1] > cur:
      l[j] = l [j-1]
      j-=1
    l[j] = cur
  
def merge(l, low, mid, high, new_l):
  a = low
  b = mid
  final = a
  while (a < mid) and (b < high):
    if l[a] < l[b]:
      new_l[final] = l[a]
      a+=1
      final+=1
    else:
      new_l[final] = l[b]
      a+=1
      final+=1

  while a < mid:
      new_l[final] = l[a]
      a+=1
      final+=1
  while b < high:
      new_l[final] = l[b]
      a+=1
      final+=1
  for i in range(l):
    l[i] = new_l[i]
  
def rec_merge_sort(l, low, high, new_l):
  if low < high:
    mid = (low+high) //2
    rec_merge_sort(l, low, mid, new_l)
    rec_merge_sort(l, mid+1, high, new_l)
    merge(l, low, mid, high, new_l)
    
def merge_sort(l):
  new_l = [0]*len(l)
  rec_merge_sort(l, 0, len(l)-1, new_l)

def quick_sort(l):
  pass