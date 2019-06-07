import re


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Zadzwon pod numer (415) 555-1011 po przerwie, 415-555-9999 to moje biuro.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Znaleziono numer telefonu: ' + chunk)
print('Gotowe')
print("-------------------------------------------------")
# (){3} - 3 krotne powtorzenie
# (){3,10} - 3 lub 4 lub ... lub 10 krotne powtorzenie
# (){3,} - minimum 3 krotne powtorzenie
# (){,3} - maksimum 3 krotne powtorzenie
phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.search(message)
print(mo.groups())
print("-------------------------------------------------")
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman i Tina Fey')
print(mo1.group())
print("-------------------------------------------------")
mo2 = heroRegex.search('Tina Fey i Batman')
print(mo2.group())
print("-------------------------------------------------")
batRegex = re.compile(r'Bat(man|mobile|copter\bat)')
mo3 = batRegex.search('Batmobile stracił koło')
print(mo3.group())
print(mo3.group(1))
print("-------------------------------------------------")
# ()* - >= 0 dopasowań
# ()? - 0 lub 1 dopasowanie
# ()+ -  >= 1 dopasowań
batRegex2 = re.compile(r'Bat(wo)*man')
mo4 = batRegex2.search('The Adventures of Batman')
print(mo4.group())
print("-------------------------------------------------")
mo5 = batRegex2.search('The Adventures of Batwowowoman')
print(mo5.group())
print("-------------------------------------------------")
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo6 = greedyHaRegex.search('HaHaHaHaHa')
print(mo6.group())
greedyHaRegex2 = re.compile(r'(Ha){3,5}?')
mo7 = greedyHaRegex2.search('HaHaHaHaHa')
print(mo7.group())
print("-------------------------------------------------")
message2 = 'Zadzwon pod numer 415-555-1011 po przerwie, 415-555-9999 to moje biuro.'
phoneNumRegex2 = re.compile(r'(\d{3}-\d{3}-\d{4})')
print(phoneNumRegex2.findall(message2))
print("-------------------------------------------------")
phoneNumRegex3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(phoneNumRegex3.findall(message2))
print("-------------------------------------------------")
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds,\
                        3 hens, 2 doves, 1 partidge'))
