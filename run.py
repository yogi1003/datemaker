import sys
from os import system

'''
datemonthyear
dateyearmonth
monthyeardate
monthdateyear
yearmonthdate
yeardatemonth
'''

sys.stdout=open("date.txt","w")
for i in range(1, 32): #you can change this range with whatever you want. 32 for dates
 x = str(i).zfill(2)
 for u in range(1, 13): #13 for months
  y = str(u).zfill(2)
  for e in range(23): #23 for years
   z = str(e).zfill(2)
   print(x, end='')
   print(y, end='')
   print(f"20{z}") #you can change this too
sys.stdout.close()
