import cv2

import numpy

import pylab

import matplotlib.pyplot as plt

#imgfile = input("heightmap.png")

#txtfile = input("height_data.txt")
print("读取图片")

img=cv2.imread("/home/jero/backup/dem_neor_navigation/src/neor_mini_foxy/worlds/autogen_terrain/materials/textures/heightmap.png",cv2.IMREAD_GRAYSCALE)
print("输出原始img",img)
height_img=12*img/255
print("输出height_img",height_img)




numpy.savetxt("/home/jero/backup/dem_neor_navigation/src/neor_mini_foxy/worlds/autogen_terrain/materials/textures/height_data.txt",height_img,fmt='%f',delimiter=',')
# for i in range(129):
#     for j in range(129):
#         print(img[i][j])
		
# print("读取成功")
# print(img[129][129])

#设定通过插值之后图片的size
new_dimension = (645,645)

def img_draw_subplot(subplot_position,img,title_name,cmap):
    plt.subplot(subplot_position)
    plt.title(title_name)
    plt.imshow(img,cmap)

def image_interpolation(img,new_dimension,inter_method):
    inter_img = cv2.resize(img,new_dimension,interpolation=inter_method)
    print("插值之后的图片大小",inter_img.shape)
    print("插值之后的图片大小已保存到文件中")
    numpy.savetxt("/home/jero/backup/dem_neor_navigation/src/neor_mini_foxy/worlds/autogen_terrain/materials/textures/inter_height_data.txt",inter_img,fmt='%f',delimiter=',')
    return inter_img

#设置cmap
cmap = "gray"


#双线性插值算法,resize函数默认的插值算法
linear_img = image_interpolation(height_img,new_dimension,cv2.INTER_LINEAR)
print(linear_img)
#三次样条插值算法
#cubic_img = image_interpolation(img,new_dimension,cv2.INTER_CUBIC)

img_draw_subplot(231,height_img,"src Image",cmap=cmap)

img_draw_subplot(233,linear_img,"Linear interpolation",cmap=cmap)

#img_draw_subplot(234,cubic_img,"cubic interpolation",cmap=cmap)
#numpy.savetxt("/home/jero/backup/dem_neor_navigation/src/neor_mini_foxy/worlds/autogen_terrain/materials/textures/inter_height_data.txt",cubic_img,fmt='%f',delimiter=',')

plt.show()


print("图像的形状,返回一个图像的(行数,列数,通道数):",img.shape)

print("图像的像素数目:",img.size)

print("图像的数据类型:",img.dtype)
