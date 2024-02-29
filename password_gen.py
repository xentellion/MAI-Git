import random
import string


total = string.ascii_letters + string.digits + string.punctuation
len = int(input("Введите длину пароля: "))
password = "".join(random.sample(total, len))
print("Ваш пароль: ", password)