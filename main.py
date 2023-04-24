# Margarita Chistiakova
# 10/3/2022
# Easter game

print(
  "Hello! I am going to calculate the date of Easter Sunday in the year you want me to!\n"
)
# I welcomed the user

print("What year do you want to know the date of Easter Sunday of?\t", end='')
year = int(input())
# now the user can enter the year that he wants to know the date of Easter Sunday

# now I am going to do several calculations
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7

easter = 22 + d + e

# now I am trying to solve mistake with these four years as they show 7 days later than the date that we need
if year == 1954:
  easter = easter - 7
elif year == 1981:
  easter = easter - 7
elif year == 2049:
  easter = easter - 7
elif year == 2076:
  easter = easter - 7

# let's eliminate the possibility of getting outcome of dates being more than 31
if easter > 31:
  easter = easter - 31
  print(f"Easter is April {easter} ")
else:
  print(f"Easter is March {easter} ")

print(
  f"Thank you for participating in my project!\nNow you know the date of Easter Sunday in {year} "
)
