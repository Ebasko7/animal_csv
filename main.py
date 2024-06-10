import csv

dog_data = {}
cat_data = {}

with open('data/dogs.csv', 'r') as dogs:
    data = csv.reader(dogs, delimiter=',')
    headers = next(data)  # Skip the header row
    for row in data:
        name = row[0]
        age = row[1]
        breed = row[2]
        dog_data[name] = {'Age': age, 'Breed': breed}

with open('data/cats.csv', 'r') as cats:
    data = csv.reader(cats, delimiter=',')
    headers = next(data)
    for row in data:
        name = row[0]
        age = row[1]
        breed = row[2]
        cat_data[name] = {'Age': age, 'Breed': breed}

def animal_lookup():
    animal = input('Enter "cat" if you are interested in cats, otherwise type in "dog"')
    if animal == 'dog':
        print(dog_data.items())
    elif animal == 'cat':
        print(cat_data.items())
    else:
        print("I don't know what that animal is")

animal_lookup()