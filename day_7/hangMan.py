import random

word_list=['aardvark','baboon','camel']

choosen_word=word_list[random.randint(0,len(word_list)-1)]

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/             

''')
print(choosen_word)
guess=input("Guess a letter: ")
guess=guess.lower()

len_of_choosen=len(choosen_word)
for i in range(0,len_of_choosen-1):
    if guess==choosen_word[i]:
        print("Right")
        break

