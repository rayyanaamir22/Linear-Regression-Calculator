# FAREWELL STATEMENT

# Modules
import random

 # Do not put periods, they are included on main.py
farewellStatements = ['See you later, Alligator', 'After a while, Crocodile', 'Goodbye']

# Choose random statement from the list
def getFarewellStatement(statements):
  statementsIndex = random.randint(0, len(statements) - 1)
  return statements[statementsIndex]
