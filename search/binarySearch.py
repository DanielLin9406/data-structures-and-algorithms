def binary_search(my_list, key):
  low = 0
  high = len(my_list) - 1
  while low <= high:
    mid = (low+high) // 2
    if key > my_list[mid]:
      low = mid + 1
    elif key < my_list[mid]:
      high = mid - 1
    else:
      return mid
  return -1

def binary_search_recursive(my_list, key, low, high):
    if (low > high):
      return -1
    mid = (low+high) // 2
    if key < my_list[mid]:
      return binary_search_recursive(my_list, key, low, mid -1)
    elif key > my_list[mid]:
      return binary_search_recursive(my_list, key, mid + 1, high)
    else:
      return mid
    
def binary_search(l, key):
  low =0
  high = len(l)-1
  while low <= high:
    mid = (low+high)//2
    if l[mid] == key:
      return mid
    elif key < l[mid]:
      high = mid -1
    elif key > l[mid]:
      low = mid + 1
  return -1

def binary_search_recursive(l, key, low, high):
  if (low > high):
    return -1
  mid = (low+high)//2
  if key < l[mid]:
    return binary_search_recursive(l, key, low, mid -1)
  elif key > l[mid]:
    return binary_search_recursive(l, key, mid + 1, high)
  else:
    return mid