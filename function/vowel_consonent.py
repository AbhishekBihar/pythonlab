ages = [5, 12, 17, 18, 24, 32]
a=[54,34,23,12,17,32,9]
def myFunc(x):
  if x < 18:
    return True
  else:
    return False

adults = filter(myFunc,a)

for x in adults:
  print(x)