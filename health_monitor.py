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

def take_measurement(min, max, metric):

  if metric == 'body temperature':
    measurement = float(input('Enter the ' + metric +'\n'))
  else:
    measurement = int(input('Enter the ' + metric +'\n'))

  if (measurement < min) or (measurement > max):
    print('at risk')
  else:
    print('healthy')
  print('________________________________________________________________________________________________')


def read_data(file):
  
  f = open(file)
  data = json.load(f)

  return data

def main():
  dataPATH = 'params.json'
  data = read_data(dataPATH)

  # Heart Rate
  hr_data = data['heart rate']
  take_measurement(hr_data['min'], hr_data['max'], hr_data['metric'])


  # Bloot Pressure
  maxbp=120
  minbp=60
  take_measurement(minbp, maxbp, 'blood pressure')


  # Body Temprature
  maxbt=37.2
  minbt=36.1
  take_measurement(minbt, maxbt, 'body temperature')


  #Breathing Status
  maxbs=20
  minbs=12
  take_measurement(minbs, maxbs, 'breathing status')

 
  # TO DO: file adding
  
if __name__ == "__main__":
  main()