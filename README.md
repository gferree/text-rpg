# text-rpg
Beginner Python Project to make a randomized text-rpg dungeon with combat system

I started learning Python as my first programming language about a month ago as of the first version of this program. Please provide any feedback you can about the project, mainly in terms of code structure, functions, etc. but game mechanic feedback and the like are also appreciated.

Typing 'help' when starting the game should give you a detailed description of each action you can take and the syntax you should follow when typing it out. There are different actions you can take while in combat and in shops, so type 'help' in there as well to learn about those specific actions.

Also, in case on first playthrough the map is a little hard to understand, here is a legend with a sample map below:

Player Icon - *
Dead Ends - <, >, ∨, ∧
And lines show which passages you can travel through, eg. ┗ shows you can travel through the north and east passage, ╋ shows you can travel through all passages, etc.

┏ ┓   ┏ ┳ ┓ ┏ ┓ ┏ ┳ > 
┣ ┛   ┗ ┛ ┣ ┫ ┃ ┗ ╋ > 
┣ ━ > ∧   ┗ ╋ ╋ ━ ┛   
┃     ┗ ┓ ┏ ╋ ┻ ┳ ━ > 
┣ ┓ < ━ ┻ ╋ ┻ ━ ╋ ━ > 
┣ ┛   ┏ ┳ * ┓   ┣ ━ > 
∨     ┣ ┫ ┣ ┛ ┏ ┛     
    ∧ ┗ ┻ ┛   ∨ ┏ > ∧ 
┏ ━ ╋ ━ ┳ ┓ ┏ ┳ ╋ ━ ┫ 
┗ ┳ ┛ ┏ ┫ ∨ ┗ ╋ ┫   ┃ 
  ∨   ┗ ┻ ━ > ┗ ┻ > ∨ 
