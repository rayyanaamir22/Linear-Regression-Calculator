# FAREWELL STATEMENT

# Modules
import random

# Do not put periods, they are included on main.py
farewellStatements = ['See you later, Alligator', 'After a while, Crocodile', r'Please give me 100% on midterms']

# Choose random statement from the list
def getFarewellStatement(statements):
  statementsIndex = random.randint(0, len(statements) - 1)
  return statements[statementsIndex]