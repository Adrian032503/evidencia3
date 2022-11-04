import json

books = [
  {
   'title':'Conceptos basicos de Python',
        'price':'79.00'
  },
  {
   'title': 'Rastreador web scrapy',
   'price': '56.00'
   }
]
json_str = json.dumps(books,ensure_ascii=False)

with open('books.json','w') as fp:
    fp.write(json_str)
    