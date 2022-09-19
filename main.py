from random import choice
from arts import stages, logo
from words import word_list


print(logo)
user_lives = 6
# print(user_lives)

random_word = choice(word_list)
# print(random_word)

length_of_str = len(random_word)
# print(length_of_str)

underscores = []
for _ in range(length_of_str):
  underscores += "_"


print(f"Here is the mysterious word: {' '.join(underscores)}")


while "_" in underscores:
  guess = input("Guess a letter: ").lower()
  if guess in underscores:
      print(f"You already tried {guess}")
    
  for index in range(length_of_str):
      if random_word[index] == guess:
        underscores[index] = random_word[index]
  print(f"{' '.join(underscores)}")
  
  
  if guess not in random_word:
    print(f"You tried {guess}, you loose a life!")
    user_lives -= 1
    print(stages[user_lives])
    if user_lives < 1:
      print(f"You lost!!! The word was {random_word}")
      break

if "_" not in underscores:
  print("You won!!!")
    


