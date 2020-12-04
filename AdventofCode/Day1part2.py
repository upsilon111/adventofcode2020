
list = [1721,979,366,299,675,1456]


def sum_to_2020 (array, sum):
  for i in range(0, len(array)):
    for j in range(0, len(array)):
      for k in range(0, len(array)):
         if sum == array[i] + array[j] + array[k]:
           return array[i] * array[j] * array[k]
  return False

print(sum_to_2020(list,2020))
