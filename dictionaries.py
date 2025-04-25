# Dictionaries
band = {
    'vocals': 'plant',
    'guitar': 'page'
}

band2 = dict(vocals='plant', guitar='page')

print(band)
print(band2)

print(type(band))
print(len(band))

# Access items
print(band['vocals'])
print(band.get('guitar'))

# listall keys
print(band.keys())

# list all values
print(band.values())