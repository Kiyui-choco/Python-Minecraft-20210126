from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()

import random
while True:
    x,y,z = Kiyui.player.getTilePos()

    color = random.randrange(0,9)
    Kiyui.setBlock(x,y,z-1,38,color)
    Kiyui.setBlock(x,y,z+1,38,color)
    Kiyui.setBlock(x-1,y,z,38,color)
    Kiyui.setBlock(x+1,y,z,38,color)
    Kiyui.setBlock(x,y+1,z-1,38,color)
    Kiyui.setBlock(x,y+1,z+1,38,color)
    Kiyui.setBlock(x-1,y+1,z,38,color)
    Kiyui.setBlock(x+1,y+1,z,38,color)