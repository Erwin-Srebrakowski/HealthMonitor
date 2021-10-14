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
import json
import numpy as np

dataPATH = 'params.json'

def take_measurement(min, max, metric):
  if metric == 'body temperature':
    measurement = float(input('Enter the ' + metric +'\n'))
  else:
    measurement = int(input('Enter the ' + metric +'\n'))

  if (measurement < min) or (measurement > max):
    status = 'at risk'
  else:
    status = 'healthy'
    
  print(status)
  print('__________________________________________________')

  return status

def read_data(file):
  f = open(file)
  data = json.load(f)
  f.close()

  return data

def check_risk(data, id):
  at_risk = [id]

  print("\nChecking patient " + str(id))

  for measurement in data:
    health_data = data[measurement]  

    if take_measurement(health_data['min'], health_data['max'], health_data['metric']) == 'at risk':
      at_risk.append(health_data['metric'])

  return at_risk


def main():
  data = read_data(dataPATH)

  nb_patients = int(input('Please specify number of patients: \n'))
  
  while True:
    record_data = input('Would you like to record the data? (y/n)')

    if record_data.lower() == 'y':
      output = True
      break
    elif record_data.lower() == 'n':
      output = False
      break
    else:
      print('Please type y or n.')

  patients = []
  patient_ids = np.zeros(nb_patients)

  for i in range (nb_patients):
    id = int(input('Please enter patient id: \n'))
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

  print('Checked patints ID:')
  print(ordered_ids)

 
if __name__ == "__main__":
  main()