import random
cpu_input = random.randint(1, 100)

while True:
  player_input = input("Guess the number (1-100): ")
  if not player_input.isdigit():
    print("Invalid input. Try again...")
    continue
  player_num = int(player_input)
  if player_num == cpu_input:
    print("You guess it!")
    break
  elif player_num < cpu_input:
    print("Too Low!")
  else:
    print("Too High!")