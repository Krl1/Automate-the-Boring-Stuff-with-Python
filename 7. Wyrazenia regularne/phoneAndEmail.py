# phoneAndEmail.py - Wyszukuje numery telefonów i adresy e-mail w schowku.

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # Numer kierunkowy
    (\s|-|\.)?                      # Separator
    (\d{3})                         # Pierwsze trzy cyfry
    (\s|-|\.)                       # Separator
    (\d{4})                         # Ostatnie cztery cyfry
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Numer wewnętrzny
    )''', re.VERBOSE)

# Utworzenie wyrażenia regularnego dopasowującego adres e-mail
emailRegex = re.compile(r'''(
    ((\w)|[.%+-])+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# Wyszukanie dopasować w schowku
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Skopiowanie wyników do schowka
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Skopiowano do schowka:')
    print('\n'.join(matches))
else:
    print('Nie znaleziono żadnego numeru telefonu lub adresu e-mail.')
