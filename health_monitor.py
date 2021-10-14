"""
1. program description
2. write program
3. push to github
"""

"""
HEALTH MONITOR

the health monitor will ask you to input thse itemes
input: heart rate(hr), blood presure(bp), body temperature(bt), breathing status(bs). 
return: the helth monitor will tell you if your healthy by checking if youre in the healthy status ie not too high not too low
return: if youre input is not in  the health satus then it will tell you that youre not health
"""
import json
import numpy as np

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
  print('________________________________________________________________________________________________')

  return status

def read_data(file):
  f = open(file)
  data = json.load(f)
  f.close()

  return data

def check_risk(data):
  at_risk = []

  print("\nNew patient:")

  # Heart Rate
  hr_data = data['heart rate']  
  if take_measurement(hr_data['min'], hr_data['max'], hr_data['metric']) == 'at risk':
    at_risk.append(hr_data['metric'])

  # Bloot Pressure
  maxbp=1202
  minbp=60
  if take_measurement(minbp, maxbp, 'blood pressure') == 'at risk':
    at_risk.append('blood pressure')

  # Body Temprature
  maxbt=37.2
  minbt=36.1
  take_measurement(minbt, maxbt, 'body temperature')

  #Breathing Status
  maxbs=20
  minbs=12
  take_measurement(minbs, maxbs, 'breathing status')

  return at_risk


def main():
  dataPATH = 'params.json'
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

  for i in range (nb_patients):
    patients.append(check_risk(data))

  if output:
    f = open('patient_data.txt', 'w')

    for patient in patients:
      for val in patient:
        f.write(val + " ")
      f.write("\n")

    f.close()

 
  
if __name__ == "__main__":
  main()