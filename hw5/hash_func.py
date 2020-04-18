<<<<<<< HEAD
=======
#!/usr/bin/python
>>>>>>> ayushi
'''
reference: https://www.pythoncentral.io/hashing-strings-with-python/
'''
import hashlib
def hash10(word):
    obj=hashlib.sha3_512(word.encode())
<<<<<<< HEAD
    print(int(obj.hexdigest(),16)%1024)

hash10("Ayushi")
hash10("\n\n\n")
hash10("Hello!")
hash10("")
=======
    #print(int(obj.hexdigest(),16)%1024)
    return int(obj.hexdigest(),16)%1024

#hash10("Ayushi")
#hash10("\n\n\n")
#hash10("Hello!")
#hash10("")
>>>>>>> ayushi
