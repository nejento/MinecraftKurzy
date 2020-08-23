from mcturtle import minecraftturtle
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

pos =  mc.player.getPos()

turtle = minecraftturtle.MinecraftTurtle(mc, pos)

turtle.speed(0) # Protože nechceme dlouho čekat

# Základy domku

turtle.penblock(block.WOOD_PLANKS.id)
for i in range(5):
    for j in range(4):
        turtle.forward(8)
        turtle.right(90)
    vyskaTurtla = turtle.position.y # Zjistí výšku turtla
    turtle.sety(vyskaTurtla + 1) # Posune turtla nahoru

# Střecha domu

# Není potřeba zvyšovat turtla, jelikož poslední vysunutí nahoru bylo provedené u zdí
delkaStrechy = 8
turtle.penblock(block.BRICK_BLOCK.id)
while delkaStrechy >= 0: # Dokud můžeme stavět střechu, stavme
    for i in range(4):
        turtle.forward(delkaStrechy)
        turtle.right(90)
    pozice = turtle.position
    # Podle toho, jak vidím, kde se staví zdi, zkontroluji souřadnice, o kolik se musím posunout
    turtle.setposition(pozice.x + 1, pozice.y + 1, pozice.z + 1)
    delkaStrechy -= 2
