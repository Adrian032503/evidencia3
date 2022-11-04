import json

datos = {
  'nombre':'juan perez',
  'edad' :18,
  'pais' :'panama'
}

json_str = json.dumps(datos)

print('datos en formato JSON:',json_str)