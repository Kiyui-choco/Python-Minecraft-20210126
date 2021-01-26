from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()

x,y,z = Kiyui.player.getTilePos()

answer = int(input('你要放沙小方塊拉淦:'))
Kiyui.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,answer)