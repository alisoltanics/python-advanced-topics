Python pickle module is used for serializing and de-serializing a
Python object structure. Any object in Python can be pickled so that it can
be saved on disk. What pickle does is that it “serializes” the object first
before writing it to file. Pickling is a way to convert a python
object (list, dict, etc.) into a character stream. The idea is that this
character stream contains all the information necessary to reconstruct the object
in another python script.



Warning: The pickle module is not secure against erroneous or maliciously constructed data. Never unpickle data received from an untrusted or unauthenticated source.





import pickle
  
def storeData():
    # initializing data to be stored in db
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
    'age' : 21, 'pay' : 40000}
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
    'age' : 50, 'pay' : 50000}
  
    # database
    db = {}
    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish
      
    # Its important to use binary mode
    dbfile = open('examplePickle', 'ab')
      
    # source, destination
    pickle.dump(db, dbfile)                     
    dbfile.close()
  
def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')     
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()
  
if __name__ == '__main__':
    storeData()
    loadData()
Output:

omkarpathak-Inspiron-3542:~/Documents/Python-Programs$ python P60_PickleModule.py
Omkar => {'age': 21,  'name': 'Omkar Pathak',  'key': 'Omkar',  'pay': 40000}
Jagdish => {'age': 50,  'name': 'Jagdish Pathak',  'key': 'Jagdish',  'pay': 50000}





Pickling without a file

# initializing data to be stored in db
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}
  
# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish
  
# For storing
b = pickle.dumps(db)       # type(b) gives <class 'bytes'>
  
# For loading
myEntry = pickle.loads(b)
print(myEntry)






####################################################################

How to Serialize and Deserialize a Python object:
https://www.techiedelight.com/serialize-deserialize-python-object/

####################################################################



https://www.geeksforgeeks.org/understanding-python-pickling-example/
