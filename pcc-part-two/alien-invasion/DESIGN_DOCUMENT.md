# 👾 Design document: Alien Invasion

A short, descriptive first-attempt at design document I made as a newbie. Might add a lot of new stuff here.

Altough I want to be a backend developer, I really enjoy video games and always wanted to create mine. I was never a gamedesigner or programmer, but now I can actually try.

---

## 🧩 Genre & Core gameplay 

### Genre: 

Arcade, Fixed shoot em up.

### Core gameplay:

Alien invasion is a game about shooting the alien ships moving from above right to the player below. Player has to shoot them all not to loose and earn points. This game is arcade so technically, the loop is infinite and player can play as much as he wants.

---

## 🎮 The game

### What can the player do?

You play as a ship that can move by pressing the Arrow Keys and shoot via the Spacebar. You can destroy the aliens if enough damage dealt. You also have just three "lifes" - it's your HP (Health points). You can play as long as you want or untill your HP is 0.

### What can the aliens do?

Aliens start to move from the left upper corner of the game's screen and slowly moving to the right, lowering the row each time when the row reaches the horisontal screen border. Each wave appears after a whole row of aliens have been destroyed, they will have increased speed, too. Each alien has it's own points value that will be added to the score. From time to time, aliens will shoot at you to deal damage and also will damage you whenever they reach the bottom corner of the screen.

### Win condition:

You can't actually win in this game since it's an arcade. Arcade genre implies that you play this game rather for fun and achieving new high score than to actually win. So technically, you can't win here, but de-facto every new high score is your small victory that you can share or keep it to yourself.

### Lose condition:

Your HP is reduced to zero. This happens if happens either of this condition:

* Alien reaches the bottom part of the screen.
* Alien hits the player with a projectile.

If you will loose 3 HP - the game will end and display the score you've earned throughout the run.

