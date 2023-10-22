import cv2

path_sour = "/Users/rnks/Documents/VCET/HandsOn/Tutorial/assets/assignment1/original/aisa "
path_dest = "/Users/rnks/Documents/VCET/HandsOn/Tutorial/assets/assignment1/rotate/aisa_rotate "

for i in range (1,11):
    
    path_source = path_sour + str(i) + '.jpg'
    print(path_source)
    
    img = cv2.imread(path_source,0)
    img = cv2.rotate(img,cv2.ROTATE_180)
    
    path_destination = path_dest + str(i) + '.jpg'
    print(path_destination)
    
    cv2.imwrite(path_destination,img)