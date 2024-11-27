names = names_string.split(", ")

import random

num_items = len(names)

random_choice = random.randint(0, num_items -1)

print(names[random_choice])