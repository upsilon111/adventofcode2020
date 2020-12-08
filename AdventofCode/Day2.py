
passwords_example=['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

  
def splitter(arr):
  password=arr.split(': ')[1]
  first_half=arr.split(':')[0]
  char=first_half.split(' ')[1]
  span=first_half.split(' ')[0]
  lower=int(span.split('-')[0])
  upper=int(span.split('-')[1])
  return [lower, upper, char, password]

def valid_password(arr):
  lower=arr[0]
  upper=arr[1]
  char=arr[2]
  password=arr[3]
  count=0
  for letter in password:
    if letter==char:
      count+=1
  if lower<=count<=upper:
    return True
  return False

def counter(arr):
  count=0
  for password in arr:
    if valid_password(splitter(password)):
      count+=1
  return count
 
print(counter(passwords_example))
