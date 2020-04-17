'''
reference: https://www.pythoncentral.io/hashing-strings-with-python/
'''
import hashlib
def hash10(word):
    obj=hashlib.md5(word.encode())
    print(int(obj.hexdigest(),16)%1024)

hash10("Ayushi")
hash10("\n\n\n")
hash10("Hello!")
hash10("")