from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()

x,y,z = Kiyui.player.getTilePos()
Kiyui.setBlock(x,y,z+2,57)
Kiyui.setBlock(x,y,z-2,57)
Kiyui.setBlock(x-2,y,z,57)
Kiyui.setBlock(x+2,y,z,57)
Kiyui.setBlock(x-1,y,z+1,57)
Kiyui.setBlock(x+1,y,z+1,57)
Kiyui.setBlock(x+1,y,z-1,57)
Kiyui.setBlock(x-1,y,z-1,57)