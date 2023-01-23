import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
length=int(input("Enter the length of the password:"))
pass_word="".join(random.sample(password,length))
print("Password is ",pass_word)
