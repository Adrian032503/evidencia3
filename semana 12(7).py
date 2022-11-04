import json

str_json= """
  {
    "nombre":"Juan Perez",
    "edad":18,
    "pais":"panama"
  }
"""

json_dat = json.loads(str_json);

print("objeto tipo diccionario:",json_dat)