class MathFacts:
  def __init__(self, list_nums):
    self.data = list_nums

  def average(self):
    sum = 0 # built in function
    n = 0
    for ele in self.data:
      sum += ele
      n += 1
    return sum / n # if n is 0

  def max(self):
    # built in function
    # it assume positive list
    # cur = None
    # if len(self.data) > 0:
    #   cur = self.data[0]
    # else:
    #   cur = -9999999
    # for ele in self.data: # value
    # # for i in range(len((list))) index
    #   if (ele > cur):
    #     cur = ele
    # return cur # edge case [-1, -2, -3]
  
    for i in range(0, len(self.data)):
      cur = self.data[i]
      j = i
      while j > 0 and self.data[j-1] < cur:
        self.data[i] = self.data[j-1]
        j-=1
      self.data[i] = cur
    return self.data[0]
  
a=MathFacts([-1,-2,-3])
print(a.average())
print(a.max())