from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()

while True:
    x,y,z = Kiyui.player.getTilePos()
    block1 = Kiyui.getBlock(x,y-1,z)
    block2 = Kiyui.getBlock(x,y-1,z+1)
    block3 = Kiyui.getBlock(x,y-1,z-1)
    block4 = Kiyui.getBlock(x-1,y-1,z)
    block5 = Kiyui.getBlock(x+1,y-1,z)
    if block1 == 8 or block1 == 9 or block2 == 8 or block2 == 9 or block3 == 8 or block3 == 9 or block4 == 8 or block4 == 9 or block5 == 8 or block == 9 :
        Kiyui.setBlock(x,y-1,z,57)
        Kiyui.setBlock(x,y-1,z+1,57)
        Kiyui.setBlock(x,y-1,z-1,57)
        Kiyui.setBlock(x-1,y-1,z,57)
        Kiyui.setBlock(x+1,y-1,z,57)