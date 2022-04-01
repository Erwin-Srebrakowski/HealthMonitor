"""
1. program description
2. write program
3. push to github
"""

"""
HEALTH MONITOR

the health monitor will ask you to input these itemes
input: heart rate(hr), blood presure(bp), body temperature(bt), breathing status(bs). 
return: the helth monitor will tell you if your healthy by checking if youre in the healthy status ie not too high not too low
return: if youre input is not in  the health satus then it will tell you that youre not health
"""
import numpy as np
from utils import *

dataPATH = 'params.json' #Global variable

def main():
  data = read_data(dataPATH)

  nb_patients = int(input('Please specify number of patients: \n'))
  
  while True:#error hadling line 25 to 35 (WhileTrueTry)
    record_data = input('Would you like to record the data? (y/n)')

    if record_data.lower() == 'y':
      output = True #Local variable
      break
    elif record_data.lower() == 'n':
      output = False
      break
    else:
      print('Please type y or n.')

  patients = []
  patient_ids = np.zeros(nb_patients)

  for i in range (nb_patients):
    while True:#error hadling line 41 to 50 (WhileTrueTry)
      try:
        id = int(input('Please enter patient id (eg. 1 if inputing only 1 patient, 1 then 2 if inputing 2 patients): \n'))
      except ValueError:
        print('[ERROR] Please enter interger for patient id')
      finally:
        if id > nb_patients:
          print('[ERROR] Please enter a number smaller than the total number of patients ')
        else:
          break
    
    patients.append(check_risk(data, id))
    patient_ids[i] = id

  ordered_ids = set(patient_ids) 

  if output:
    f = open('patient_data.txt', 'w')

    for patient in patients:
      for val in patient:
        f.write(str(val) + " ")
      f.write("\n")

    f.close()

  print('Checked patients ID:')
  print(ordered_ids)
  

 
if __name__ == "__main__":
  main()