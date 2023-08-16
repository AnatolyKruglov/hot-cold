# hot-cold
The 'Hot-cold' game using text embeddings (as a telegram bot)

This is a raw idea, but the beta-version allows minimal gameplay
After the target word is set (hardcoded in the script), players try to guess that word. All attempts are assigned a number R - their distance to the target in a text embedding. For a correct guess (when attempt == target), R equals zero, and otherwise it is a positive number. Players are notified when they are moving in the correct ('hot') or incorrect ('cold') direction: if R decreases or increases over time. After the game, the text embedding for all the attempts and the target is projected on a plane (pca-transformed into 2d) and sent to the players as 'their route' of the game.

Example gameplay:

Anatolii Kruglov, [07.08.2023 3:08]
/start

HotCold, [07.08.2023 3:08]
Guess the word with hints 'hot-cold'

Anatolii Kruglov, [07.08.2023 3:08]
nature

HotCold, [07.08.2023 3:08]
0°, good start!

Anatolii Kruglov, [07.08.2023 3:08]
tree

HotCold, [07.08.2023 3:08]
+3°, warm)

Anatolii Kruglov, [07.08.2023 3:08]
leaf

HotCold, [07.08.2023 3:08]
+5°, warm)

Anatolii Kruglov, [07.08.2023 3:08]
branch

HotCold, [07.08.2023 3:08]
-13°, cold(

Anatolii Kruglov, [07.08.2023 3:09]
green

HotCold, [07.08.2023 3:09]
100°, congratulations!

HotCold, [07.08.2023 3:09]
![image](https://github.com/AnatolyKruglov/hot-cold/blob/main/photo_2023-08-16_12-15-22.jpg) 
