# Program sprawdzający, czy podane hasło to silne hasło
# Hasło jest silne, gdy składa się z przynajmniej ośmiu znaków, zawiera zarówno małe
# jak i duże litery, przynajmniej jedną cyfrę oraz znak specjalny
import re

haslo = "LatweHaslo"
haslo2 = "TrudneHaslo123"
passwordRegex = re.compile(r'\w*')
print(passwordRegex.findall(haslo2))
