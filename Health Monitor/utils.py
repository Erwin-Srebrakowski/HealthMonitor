import json

def take_measurement(min, max, metric):#error hadling line 3 to 21 (WhileTrueTry)
  
  incorrect_input = True

  while incorrect_input:
    try:
      if metric == 'body temperature':
        measurement = float(input('Enter the ' + metric +'\n'))
      else:
        measurement = int(input('Enter the ' + metric +'\n'))
      incorrect_input = False
    except ValueError:
      print('[ERROR] Please enter correct value for {}.'.format(metric))#talks to the json file to input the right metric in the sring
      incorrect_input = True

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
