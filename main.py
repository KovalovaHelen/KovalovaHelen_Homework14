data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4},
    {'name': 'Test 5', 'position': 5},
    {'name': 'Test 6', 'position': 6}
]


def delete_position(position):
    global data

    for i in range(len(data)):
        if i + 1 == position:
            data.pop(i)
            break

    data = sorted(data, key=lambda x: x['position'])
    for i in range(len(data)):
        data[i]['position'] = i + 1


def add_position(name, position):
    global data
    data.insert(0, {'name': name, 'position': position})
    data = sorted(data, key=lambda x: x['position'])
    for i in range(len(data)):
        data[i]['position'] = i + 1


def change_position(position1, position2):
    global data
    for i in range(len(data)):
        if i + 1 == position1:
            data[i]['position'] = position2
        if i + 1 == position2:
            data[i]['position'] = position1

    data = sorted(data, key=lambda x: x['position'])
    for i in range(len(data)):
        data[i]['position'] = i + 1


delete_position(4)
print(data)

#add_position('Test 1', 1)
#print(data)

#change_position(1, 3)
#print(data)
