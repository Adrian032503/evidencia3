import json
data = {}
data['clients'] = []
data['clients'].append({
  'first_name':'sigrid',
  'last_name':'mannock',
  'age':27,
  'amount':7.17})
data['clients'].append({
  'first_name':'joe',
  'last_name':'hinners',
  'age':31,
  'amount':[1.90,5.50]})
data['clients'].append({
  'first_name':'theodoric',
  'last_name':'rivers',
  'age':36,
  'amount':1.11})
with open('data.json','w') as file:
  json.dump(data,file,indent=4)