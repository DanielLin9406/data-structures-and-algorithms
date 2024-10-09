def linear_search(my_list, key):
  for i in range(0, len(my_list)):
    if my_list[i] == key:
      return i
  return -1

def linear_search(l, key):
  for i in range(0, len(l)):
    if key == l[i]:
      return i
  return -1