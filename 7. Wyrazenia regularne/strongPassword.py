# Program sprawdzający, czy podane hasło to silne hasło
# Hasło jest silne, gdy składa się z przynajmniej ośmiu znaków, zawiera zarówno małe
# jak i duże litery, przynajmniej jedną cyfrę oraz znak specjalny
import re
import pyperclip

hasla = "LatweHaslo TrudneHaslo123 Kot EWAMAKOTA1231 ewamakota3412 Kotek*7&23 nosoroZec"
hasla = text = str(pyperclip.paste())
# ciąg znaków o długości co najmniej 8
passwordRegex = re.compile(r'\S{8,}')
passwordsList = passwordRegex.findall(hasla)
hasla = ''
print(passwordsList)
for password in passwordsList:
    hasla += password + " "

# sprawdzenie czy zawiera co najmniej jedną małą i dużą literę
passwordRegex = re.compile(r'''
    \S*
    [a-z]+
    \S*
    [A-Z]+
    \S* | 
    \S*
    [A-Z]+
    \S*
    [a-z]+
    \S*
    ''', re.VERBOSE)
passwordsList = passwordRegex.findall(hasla)
hasla = ''
print(passwordsList)
for password in passwordsList:
    hasla += str(password) + " "

# sprawdzenie czy zawiera co najmniej jedną cyfrę i znak specjalny
passwordRegex = re.compile(r'''
    \S*
    [0-9]+
    \S*
    [!@#$%^&*()_\-+=\{\}\[\];:\'\"\\|,<.>?/]+
    \S* |
    \S*
    [!@#$%^&*()_\-+=\{\}\[\];:\'\"\\|,<.>?/]+
    \S*
    [0-9]+
    \S*
    ''', re.VERBOSE)
passwordsList = passwordRegex.findall(hasla)
hasla = ''
print(passwordsList)
for password in passwordsList:
    hasla += str(password) + " "
