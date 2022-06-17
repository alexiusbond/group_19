# from calculator import addition, multiplication
from calculator import addition as add
from person import Person
from random import randint as genarate_random_number
import termcolor
import os
from envparse import env

print(add(88, 1))
# Hi teacher
person = Person("John", 22)
termcolor.cprint('Hello, World!', 'green', attrs=['underline'])

print(os.environ.get('LOGIN_FOR_DB'))

env.read_envfile('options.env')
print(os.environ.get('PASSWORD'))
