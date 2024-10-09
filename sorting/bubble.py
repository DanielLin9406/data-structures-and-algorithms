# Time worst O(n^2)
# Time avg O(n^2)
# Time best O(n)
# Space O(1)

def bubble_sort(my_list):
  for i in range(0, len(my_list)-1):
    for j in range(0, len(my_list) - i -1):
      if my_list[j] > my_list[j+1]:
        my_list[j+1], my_list[j] = my_list[j], my_list[j+1]
        