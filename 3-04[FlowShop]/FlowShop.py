#!/usr/bin/python 
# Filename: FlowShop.py 

class JobType:
  def judgeJob(self, x, y):
    self.job = (x <= y)
    self.key = x if x <= y else y 
    return self.job 
  def judgeIndex(self, index):
    self.index = index 
      
def sort(array, n):
  for i in range(0, n - 1):
    k = i
    for j in range(i + 1, n):
      if array[k].key > array[j].key:
        k = j
    temp = array[k]
    array[k] = array[i]
    array[i] = temp


def FlowShop(n, a, b, c):
  d = []
  temp = JobType()
  for i in range(0, n):
    d.append(JobType())
    d[i].judgeJob(a[i], b[i])
    d[i].index = i
#     print d[i].job, d[i].key, d[i].index

  sort(d, n)

  '''
  for i in range(0, n):
    print d[i].job, d[i].key, d[i].index
  '''

  j = 0
  k = n - 1
  for i in range(0, n):
    if d[i].job:
      c[j] = d[i].index
      j += 1
    else:
      c[k] = d[i].index
      k -= 1
  
  j = a[c[0]]
  k = j + b[c[0]]
  for i in range(1, n):
    j += a[c[i]]
    k = (k + b[c[i]]) if j < k else (j + b[c[i]])
  
  return k

# The main program
a = [5, 12, 4, 8]
b = [6, 2, 14, 7]
c = [-1, -1, -1, -1]

t = FlowShop(4, a, b, c)

for i in range(0, 4):
  c[i] += 1

print t

print c
