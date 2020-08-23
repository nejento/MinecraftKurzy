from mcpi import minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Ahoj světe")
mc.postToChat(2+2)

for cislo in range(5):
    mc.postToChat(cislo)

souradnice = mc.player.getPos()
mc.postToChat(souradnice)

mc.player.setPos(souradnice.x, souradnice.y + 10, souradnice.z)

