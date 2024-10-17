def linear_search(l, key):
  for i in range(len(l)-1):
    if l[i] == key:
      return i
  return -1

def binary_search(l, key):
  low = 0
  high = len(l) -1
  while low < high:
    mid = (low+high) //2
    if key < l[mid]:
      high = mid
    elif key > l[mid]:
      low = mid
    else:
      mid
  return -1

def binary_search_rec(l, key, low, high):
  if (low > high):
    return -1
  mid = (low+high) //2
  if key < l[mid]:
    return binary_search_rec(l, key, low, mid-1)
  elif key > l[mid]:
    return binary_search_rec(l, key, mid+1, high)
  else:
    return mid