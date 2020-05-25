import random

female_name_list = ['Eryn', 'Breanne', 'Riva', 'Winona', 'Casandra', 'Katia', 'Agripina', 'Florentina', 'Denna', 'Margurite', 'Larissa']
male_name_list = ['Lenard', 'Broderick', 'Robert', 'Wilburn', 'Jayson', 'Dominick', 'Philip', 'Clint', 'Florencio', 'Chip', 'Taylor']
quality_list = ['Tough', 'Feared', 'One-Eyed Bandit', 'Badass', 'Dangerous', 'Limitless', 'Toothless', 'Cretin', 'Merciless', 'Dark']

name_list = female_name_list + male_name_list

first_name = random.choice(name_list)
last_name = random.choice(quality_list)

print(first_name, "the", last_name)

