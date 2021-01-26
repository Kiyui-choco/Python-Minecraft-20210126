from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()

import random,time
while True:
    x,y,z = Kiyui.player.getTilePos()

    color = random.randrange(0,16)
    Kiyui.setBlocks(x+10,y,z+10,x-10,y,z-10,251,color)
    time.sleep(3)