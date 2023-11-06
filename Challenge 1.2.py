# Leap year or non Leap year
def isleapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter a year : "))
if isleapyear(year):
  print('{} is a Leap Year.'.format(year))
else:
  print('{} is Not a Leap Year.'.format(year))