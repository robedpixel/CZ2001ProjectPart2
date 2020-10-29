import random


def gen_ran_hospital_locations(number_of_nodes: int, number_of_hospitals: int) -> list:
    output = list()
    for x in range(number_of_hospitals):
        random_number = random.randint(0, number_of_nodes-1)
        number_is_present = False
        added = False
        while not added:
            for value in output:
                if value == random_number:
                    number_is_present = True
            if not number_is_present:
                output.append(random_number)
                added = True
            else:
                random_number = (random_number+1) % number_of_nodes
                number_is_present = False
    return output
