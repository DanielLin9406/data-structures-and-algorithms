def merge(list_a, list_b, last_a, last_b):
  idx_a = last_a -1
  idx_b = last_b -1
  idx_merge=last_a+last_b-1
  
  while(idx_b >= 0):
    if (idx_a >=0 and list_a[idx_a] > list_b[idx_b]):
      list_a[idx_merge] = list_a[idx_a]
      idx_a-=1
    else:
      list_a[idx_merge] = list_b[idx_b]
      idx_b-=1
    idx_merge-=1
    
a=[1,3,5,7,9,11,0,0,0,0,0,0,0,0]
b=[2,4,6,8] 
merge(a, b, 6, 4)
print(a)