def bubble_sort(l):
  for i in range(len(l)-1):
    for j in range(len(l)-i-1):
      if l[j] < l[j-1]:
        l[j-1], l[j] = l[j], l[j-1]
        

def selection_sort(l):
  for i in range(1, len(l)):
    pivot = i
    for j in range(i, len(l-1)):
      if l[pivot] < l[j]:
        pivot = j
    if pivot != i:
      l[pivot], l[i] = l[i], l[pivot]
      
      
      
def insertion_sort(l):
  for i in range(len(l)):
    cur = l[i]
    j=i
    while j>0 and l[j-1] > cur:
      l[j] = l [j-1]
      j-=1
    l[j] = cur
    
def merge_sort(l):
  pass

def quick_sort(l):
  pass