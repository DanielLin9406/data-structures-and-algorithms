# Time worst O(n^2)
# Time avg O(n^2)
# Time best O(n)
# Space O(1)

def insertion_sort(my_list):
  for i in range(1, len(my_list)):
    cur = my_list[i]
    j = i
    while j > 0 and my_list[j-1] > cur:
      my_list[j] = my_list[j-1]
      j-=1
    my_list[j] = cur
    
def insertion_sort2(l):
  for i in range(1, len(l)):
    cur = l[i]
    j = i
    while j > 0 and l[j-1] > cur:
      l[j-1] = l[j]
      j-=1
    l[j] = cur
    
    
def insertion_sort3(l):
  for i in range(1, len(l)):
    curr = l[i]
    j=i
    while j>0 and l[j-1] > curr:
      l[j] = l[j-1]
      j-=1
    l[j] = curr
    
list = [5,4,3,7,8,9]
insertion_sort3(list)
print(list)