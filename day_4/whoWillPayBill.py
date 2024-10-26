import random

people=["haris","aryan","vansh","varun","akhil"]
len_of_list=len(people)

random_person_index=random.randint(0,len_of_list-1)

random_person=people[random_person_index]

print(f"{random_person} will pay the bill.")

# other way
'''
print(random.choice(people))
'''