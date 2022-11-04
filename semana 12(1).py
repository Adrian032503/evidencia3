import csv

headers = ['name','age','classroom']
values = [
    ('zhiliao',18,'111'),
    ('wena',20,'222'),
    ('bbc',21,'111')
]
with open ('test.csv','w', newline='') as fp:
    writer = csv. writer(fp)
    writer.writerow(headers)
    writer.writerows(values)