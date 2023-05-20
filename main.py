import random


def get_doors():
    doors = [1, 2, 3]
    random.shuffle(doors)
    return doors


def choose_door():
    return random.randrange(1, 4, 1)


def remove_door(doors, choice):
    doors.pop(doors.index(choice))
    for index, door in enumerate(doors):
        if door != 3:
            doors.pop(index)
            return doors[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count1 = 0
    count2 = 0
    count3 = 0
    num_range = int(input("number of iterations: "))
    for x in range(num_range):
        doors = get_doors()
        choice = choose_door()
        swapped = remove_door(doors, choice)
        always_switch = swapped
        never_switch = choice
        random_switch = random.choice([choice, swapped])
        if always_switch == 3:
            count1 += 1
        if never_switch == 3:
            count2 += 1
        if random_switch == 3:
            count3 += 1
    print(f"percentage won if always switching: {count1/num_range}%")
    print(f"percentage won if never switching: {count2 / num_range}%")
    print(f"percentage won if randomly switching: {count3 / num_range}%")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
