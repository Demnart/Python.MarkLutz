import shelve

db = shelve.open('persondb')
for key in sorted(db):
    print(key,"\t=>",db[key])

sue = db['Sue Jons']
sue.value(0.10)
db['Sue Jons'] = sue

db.close()