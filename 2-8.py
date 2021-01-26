from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()

userName = input('請輸入姓名:')
message = input('請輸入發言:')
Kiyui.postToChat(' <'+userName + '> ' + message)
