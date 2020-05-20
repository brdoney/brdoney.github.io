---
title: Arena Fighter
order: 15
type: exercise
---

There's nothing quite as heart-pounding as a close fight against a boss enemy in a game. Using all we've learned, let's create a program that lets us play through just that!

## Outline

1. Print out information about the health of the player and the health of the enemy
2. Ask the player if they would like to...

```rawtext
1) Attack the boss
2) Heal
```

3. Do the action based on their choice
   - If the player wants to attack, do a random number of damage to the enemy by subtracting the number from the enemy's health
   - If the player wants to heal, add a random number to the player's health points
4. Have the enemy attack by doing a random number of damage to the player by subtracting the number from the player's health
5. As long as the player and the enemy both still have health, start back at step 1 again. Otherwise, stop looping at go on to step 6
6. Based on who has more health, print out a message saying who won the fight

## More Ideas

- Add a third option, running away, and stop running the program if the player chooses it
- Add a shop that lets the user buy equipment that changes how much damage and health they have in the fight
- Add the ability for the user to fight more enemies after the first one dies, as long as they want
