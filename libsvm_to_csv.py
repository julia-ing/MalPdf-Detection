import os
import pandas as pd
from ML import my_model 

f = open('../test-data.libsvm', 'r')

lines = f.readlines()
result = os.popen("cat ../features.nppf | wc -l")
result = result.read()

for line in lines:
  minus_list = [-1]*(int(result)-1)

  l = line.split(' #')[0]
  l = l.split(' ')
  file_name = lines[0].split(' #')[1].strip('\n')

  for i in range(len(l)):
    if i != 0:
      key = int(l[i].split(':')[0])
      val = float(l[i].split(':')[1])
      minus_list[key-1]=val

  #if int(l[0]) == 1:
   # mb = 'M'
  #else:
   # mb = 'B'

  #result_string[0].append(str(minus_list).strip('[]'))
  result_string = str(minus_list).strip('[]')

  print(result_string)
  print(len(result_string))

print("#############")
tmp = [[]]
for i in range(len(result_string.split(','))):
  tmp[0].append(result_string.split(',')[i])

final = pd.DataFrame(tmp)
#print(final)
my_model(final)

