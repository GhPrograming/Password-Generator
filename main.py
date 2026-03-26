import secrets
import string 
# X will have random value
X = string.ascii_letters + string.digits + string.punctuation

parola = "" 
for _ in range(10):
    parola = parola + secrets.choice(X)

print(parola)

with open("fisier.txt", "a") as f:  
    f.write(parola + "\n")  
