# Construír unha función que permita facer a procura de inmobles en función dun orzamento dado. A función
# recibirá como entrada a lista de inmobles e un prezo, e devolverá outra lista cos inmobles cuxo prezo sexa
# menor ou igual que o dado. Os inmobles da lista que se devolva deben incorporar un novo atributo do a cada
# dicionario co prezo do inmoble, onde o prezo dun inmoble calcúlase coa seguinte fórmula en función da zona:

# Zona A: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100)
# Zona  B: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100) * 1.5

data : list = [
    {'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe':  True, 'zona': 'A'},
    {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe':  True, 'zona': ' B'},
    {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe':  False, 'zona': 'A'},
    {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe':  True, 'zona': ' B'},
    {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe':  False, 'zona': 'A'}
]

def giveMeHousesBelowThisPrice(house_data, price):
    houseList : list = []
    for house in house_data:
        housePrice = house['ano'] * 1000 + house['metros'] * 5000 + house['habitacións'] * 1000 + house['garaxe'] * 15000

        if house['zona'] == 'A':
            zoneAPrice = housePrice * (1- (2025 - house['ano'])/100)
            house_copy = dict(house)  # Create a copy of the house dict
            house_copy['precio'] = zoneAPrice
            if zoneAPrice <= price:
                houseList.append(house_copy)
        else:
            zoneBPrice = housePrice * (1 - (2025 - house['ano']) / 100) * 1.5
            house_copy = dict(house)  # Create a copy of the house dict
            house_copy['precio'] = zoneBPrice
            if zoneBPrice <= price:
                houseList.append(house_copy)
    return houseList

print(giveMeHousesBelowThisPrice(data, 2000000))