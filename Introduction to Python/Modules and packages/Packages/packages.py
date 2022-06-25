import functions.goodbye as bye
import functions.greeting.hello
from classes import calculator
# Import the `official` module here
from functions.greeting import official

print(functions.greeting.hello.hello('Susan'))
print(bye.good_bye('Alex'))

c = calculator.Calculator()
c.add(2)
c.multiply(10)
print(c.get_current())

print(official.hello('Sam'))
