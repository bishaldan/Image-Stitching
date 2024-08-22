import cv2
import os
mainFolder = 'img'
myFolder = os.listdir(mainFolder)
print(myFolder)

for folder in myFolder:
    path = mainFolder+'/'+folder
    images = []
    mylist = os.listdir(path)
    print(f' Total no of images detected {len(mylist)}')
    for imgN in mylist:
        curImg = cv2.imread(f'{path}/{imgN}')
        curImg = cv2.resize(curImg,(0,0),None,0.8,0.8)
        images.append(curImg)
    stritcher = cv2.Stitcher.create()
    (status,result) = stritcher.stitch(images)
    if (status == cv2.STITCHER_OK):
        print('Panorama Generated')
        cv2.imshow(folder,result)
        cv2.waitKey(2)
    else:
        print('panorama Genration unsuccessful')
cv2.waitKey(0)
    # print(len(images))
