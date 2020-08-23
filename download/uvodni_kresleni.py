from mcturtle import minecraftturtle
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
pos =  mc.player.getPos()
turtle = minecraftturtle.MinecraftTurtle(mc, pos)

# Počítáme od nuly 

# Nakresli čáru 5 bloků dlouhou
turtle.forward(5)

# Napiš písmeno L
turtle.forward(3)
turtle.left(90) # 90 = 90 stupňů
turtle.forward(2)

# Zrychli stavbu
turtle.speed(10)

# Vytvoř čtverec
for i in range(4):
    turtle.forward(5)
    turtle.left(90)

# Nakresli přerušovanou čáru
for i in range(5):
    turtle.forward(2)
    turtle.penup()
    turtle.forward(2)
    turtle.pendown()

# Kresli různými bloky
blok = 1
for i in range(10):
    turtle.forward(1)
    turtle.penblock(blok)
    blok += 1

turtle.penblock(block.DIRT.id)

# Postav sloupek
turtle.up(90)
turtle.forward(9)

# Postav čtverec, ale zase aby byl vodorovně!
turtle.down(90) # Tohle zatím zatajit!
for i in range(4):
    turtle.forward(5)
    turtle.left(90)