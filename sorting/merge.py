def merge_sort(my_list):
  empty_list = [0]*len(my_list)
  recur_merge_sort(my_list, 0, len(my_list)-1, empty_list)
  
def recur_merge_sort(my_list, first_idx, last_idx, empty_list):
  if first_idx < last_idx:
    mid_idx = (first_idx + last_idx) // 2
    recur_merge_sort(my_list, first_idx, mid_idx, empty_list)
    recur_merge_sort(my_list, mid_idx+1, last_idx, empty_list)
    merge(my_list, first_idx, mid_idx+1, last_idx, empty_list)
      
def merge(my_list, first_idx, mid_idx, last_idx, empty_list):
  a_idx = first_idx
  b_idx = mid_idx
  empty_idx = last_idx
  
  while (a_idx < mid_idx) and (b_idx < last_idx):
    if my_list[a_idx] <= my_list[b_idx]:
      empty_list[empty_idx] = my_list[a_idx]
      a_idx += 1
    else:
      empty_list[empty_idx] = my_list[b_idx]
      b_idx += 1
    empty_idx+=1
    
  while (a_idx < mid_idx):
      empty_list[empty_idx] = my_list[a_idx]
      a_idx += 1
      empty_idx+=1
  while (b_idx < last_idx):
      empty_list[empty_idx] = my_list[b_idx]
      b_idx += 1
      empty_idx+=1
      
  for i in range(first_idx, last_idx+1):
    my_list[i] = empty_list[i]
    
    
    
def merge_sort(l):
  empty_list = [0]*len(l)
  recur_merge_sort(l, 0, len(l)-1, empty_list)
  
def recur_merge_sort(l, low, high, new_list):
  if low < high:
    mid = (low+ high) // 2
    recur_merge_sort(l, low, mid, new_list)
    recur_merge_sort(l, mid+1, high, new_list)
    merge(l, low, mid+1, high, new_list)
    
def merge(l, low, mid, high, new_l):
  a_idx = low
  b_idx = mid
  new_idx = new_l
  
  while (a_idx < mid) and (b_idx < high):
    if l[a_idx] < l[b_idx]:
      new_l[new_idx] = l[a_idx]
      a_idx += 1
    else:
      new_l[new_idx] = l[b_idx]
      b_idx += 1      
    new_idx+=1
    
  while (a_idx < mid):
    new_l[new_idx] = l[a_idx]
    a_idx += 1
    new_idx+=1
          
  while b_idx < high:
    new_l[new_idx] = l[b_idx]
    b_idx += 1      
    new_idx+=1    
    
  for i in range(low, high+1):
    new_l[i] = l[i]