import hashlib

ANY_STRING = input("Enter any String : ")
Result = hashlib.md5(ANY_STRING.encode("utf-8")).hexdigest()
print(Result)