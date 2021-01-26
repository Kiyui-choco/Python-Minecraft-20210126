from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()

x,y,z = Kiyui.player.getTilePos()

long = 10
big = 8
high = 7

block = 213
air = 0

Kiyui.setBlocks(x,y,z,x+long,y+high,z+big,block)
Kiyui.setBlocks(x+1,y+1,z+1,x+long-1,y+high-1,z+big-1,air)