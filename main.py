# Lab12 - Factory
# LeAnh Ly, Derek Mean (Group 16)
# 11/15/22
# Description: Create a program that allows the user to wander through a dungeon maze and fight monsters that they encounter as they explore

# Imports
import hero
import map
import check_input
import random
import beg_factory
import exp_factory

def main():

  # Prompt user for their name
  user_name = input("What is your name, traveler? ") 
  # Prompt user for the difficulty
  difficulty = check_input.get_int_range("Difficulty:\n1. Beginner\n2. Expert\n", 1, 2)

  # Creates factory of enemies depending on selected difficulty
  if difficulty == 1:
    factory = beg_factory.BeginnerFactory()
  else:
    factory = exp_factory.ExpertFactory()
    
  # Create hero and map objects
  user = hero.Hero(user_name, 25)
  map_1 = map.Map()

  # Tracks what map it's on
  current_map = 1
  
  user_direction = 0
  # Repeat until the user quits/dies
  while user_direction != 5 and user.get_hp > 0:
    print()
    print(user)
    # Show map
    print(map_1.show_map(user.get_loc))
    # Tracks user's previous location before movement
    user_prevloc = user.get_loc

    # Present direction menu
    user_direction = check_input.get_int_range("\n1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter Choice: ", 1, 5)

    # NORTH
    if user_direction == 1:
      # Move user
      user_move = user.go_north()
      if user_move == "x":
        print("You cannot go that way...")
      # Reveal spot
      map_1.reveal(user.get_loc)

        
    # SOUTH 
    elif user_direction == 2:
      # Move user
      user_move = user.go_south()
      if user_move == "x":
        print("You cannot go that way...")
      # Reveal spot
      map_1.reveal(user.get_loc)

      
    # EAST
    elif user_direction == 3:
      # Move user
      user_move = user.go_east()
      if user_move == "x":
        print("You cannot go that way...")
      # Reveal spot
      map_1.reveal(user.get_loc)

      
    # WEST
    elif user_direction == 4:
      # Move user
      user_move = user.go_west()
      if user_move == "x":
        print("You cannot go that way...")
      # Reveal spot
      map_1.reveal(user.get_loc)


    # If the user travels to a valid location, proceed to room
    if user_move != "x":
      room = map_1[user.get_loc[1]][user.get_loc[0]]    
      # Present encounter
      
      # MONSTER
      if room == "m":
        # Create enemy object from factory
        monster = factory.create_random_enemy()
        print(f"\nYou encounter a {monster.get_name}")
        # Return health of the monster
        print(f"HP: {monster.get_hp}/{monster._max_hp}")
  
        enemy_choice = 0
        while enemy_choice != 2 and user.get_hp > 0:
          # Prompt user to attack or run away until they run away/user dies
          enemy_choice = check_input.get_int_range(f"1. Attack {monster.get_name}\n2. Run Away\nEnter Choice: ", 1, 2)
        
          if enemy_choice == 1:
            print(user.attack(monster))
            if monster.get_hp > 0:
              # If the monster is not dead, attack the user
              print(monster.attack(user))
              if user.get_hp <= 0:
                print("You are dead.")
            else:
              print(f"You have slain a {monster.get_name}")
              # When the monster is defeated, remove "m" from the location
              map_1.remove_at_loc(user.get_loc)
              break
          else:
            # User decides to run away from enemy
            map_1.reveal(user.get_loc)
            run = False
            print("You ran away!\n")
              
            while run == False:
              # Select a random location to run in
              rand_direction = random.randint(1, 4)
              if rand_direction == 1:
                # User goes north randomly
                if user.get_loc[1] == 0:
                  continue
                else:
                  user.go_north()
                  run = True
              if rand_direction == 2:
                # User goes south randomly
                if user.get_loc[1] == 4:
                  continue
                else:
                  user.go_south()
                  run = True
              elif rand_direction == 3:
                # User goes east randomly
                if user.get_loc[0] == 4:
                  continue
                else:
                  user.go_east()
                  run = True
              elif rand_direction == 4:
                # User goes west randomly
                if user.get_loc[0] == 0:
                  continue
                else:
                  user.go_west()
                  run = True
            # Reveal location
            map_1.reveal(user.get_loc)
              
      # INVALID DIRECTION
      elif room == "x":
        # User travels to invalid location
        print("You cannot go that way...")
  
      # NOTHING
      elif room == "n":
        # User travels to a location that contains nothing
        print("There is nothing here...")
  
      # START
      elif room == "s":
        # User returns to starting location
        if user_direction == 5:
          break
        elif user_prevloc == (0,0):
          print("You cannot go that way...")
        else:
          print("You have returned to the start.")
  
      # ITEM ROOM
      elif room == "i":
        if user.get_hp == 25:
          # If the user is at full health, save the potion for later
          print("You found a Health Potion! Your health is maxed so you save it there for later.")
        else:
          # User drinks potion and heals if below max health
          print("You found a Health Potion! You drink it to restore your health.")
          user.heal()
          # Remove item from location
          map_1.remove_at_loc(user.get_loc)
  
      # FINISH
      elif room == "f":
        # User finishes the maze
        print("Congratulations! You found the stairs to the next floor of the dungeon.")
  
        if (current_map + 1) > 3:
          # If the map number exceeds 3, set map number to 1
          current_map = 1
        else:
          # If not, increment map number
          current_map += 1
        # Load next map
        map_1.load_map(current_map)

  print("Game Over")
  
main()

