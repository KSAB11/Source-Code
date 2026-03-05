
asean = {
    "Brunei": "Bandar Seri Begawan",
    "Cambodia": "Phnom Penh",
    "Indonesia": "Jakarta",
    "Laos": "Vientiane",
    "Malaysia": "Kuala Lumpur",
    "Myanmar": "Naypyidaw",
    "Philippines": "Manila",
    "Singapore": "Singapore",
    "Thailand": "Bangkok",
    "Vietnam": "Hanoi"
}

def get_capital(country):
    return asean.get(country, "Country not found")

capital = input("Enter the ASEAN country: ").lower().title()
capital = get_capital(capital)
print(f"The capital of the country is: {capital}")

