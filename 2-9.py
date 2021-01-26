from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()

x,y,z = Kiyui.player.getTilePos()
Kiyui.setSign(x,y,z+1,63,0,'Kiyui Only Love Ella')