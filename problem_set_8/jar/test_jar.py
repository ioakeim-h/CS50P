
from jar import Jar

oreo_jar = Jar()
oreo_jar.deposit(5)
print(f"Capacity: {oreo_jar.capacity}\nCookies: {oreo_jar.size}")
oreo_jar.withdraw(5)
print(f"Cookies: {oreo_jar.size}")
