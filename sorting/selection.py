# Time worst O(n^2)
# Time avg O(n^2)
# Time best O(n^2)
# Space O(1)

def selection_sort(my_list):
  for i in range(0, len(my_list) -1):
    pivot = i
    for j in range(i+1, len(my_list)):
      if my_list[j] < my_list[pivot]:
        pivot = j
    if pivot != i:
      my_list[pivot], my_list[i] = my_list[i], my_list[pivot]
    
def selection_sort2(l):
  n = len(l)
  for i in range(n - 1):
    pivot = i
    for j in range(i+1, n):
      if l[j] < l[pivot]:
        pivot = j
    if pivot != i:
      l[pivot], l[i] = l[i], l[pivot]


list2 = [5,4,3,7,8,9]
selection_sort2(list2)
print(list2)