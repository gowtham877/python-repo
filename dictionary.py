states = {
    'Tamil Nadu': 'TN',
    'Kerela': 'Kl',
    'Karnatka': 'KA'
    }

cities = {
    'TN': 'Chennai',
    'KA': 'Bangalore'
}

cities['Kl'] = 'kannur'
cities['KA'] = 'Tumkur'

print cities['TN'] #states
print states['Kerela'] #cities

print cities[states['Karnatka']]

#printing the states and its abbreviations
for state, abbrev in states.items():
    print state, abbrev

#printing the city and state
for abbrev, city in cities.items():
    print abbrev, city

for state, abbrev in states.items():
    print state, abbrev, cities[abbrev]

states.get('Andhra')

if not states:
    print "State not present."
