#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-10-2-2.py
fileName="/autogen_terrain/materials/textures/heightmap.png"
print("文件内容:")
with open(fileName,'rb') as fileObject:
    fileTxts=fileObject.read()
    print("PNG文件标识:")
    for data in fileTxts[:8]:
        print("{:#x}".format(data),end=" ") 
    print("\n图像长度:")
    data=fileTxts[16:20]
    print(int.from_bytes(data,"big"))
    print("\n图像宽度:")
    data=fileTxts[20:24]
print(int.from_bytes(data,"big"))   
