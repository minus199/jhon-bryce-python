import shelve

db = shelve.open('capitals')
db['UK'] = 'London'
db['caps'] = {
    'Australia': 'Canberra',
    'Eire': 'Dublin',
    'UK': 'London',
    'US': 'Washington',
    'foo': ["fizz", "fuzz", "fozz"]
}
print(db)
db.sync()
db.close()

db = shelve.open('capitals')
print(db['UK'])
db.close()
