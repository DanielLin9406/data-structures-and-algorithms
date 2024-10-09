l=[[1,2,3,4,5],[6,7,8,9,10]]

# for x in range(0,len(l)):
#   for y in range(0, len(l[x])):
#     print(y)
    
    
for idx, x in enumerate(l):
  for idy, y in enumerate(l[idx]):
    print(y)