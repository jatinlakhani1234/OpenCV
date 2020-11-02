import cv2

list1 = [i for i in dir(cv2) if 'EVENT' in i]
print(len(list1))
for num, i in enumerate(list1):
    print(num+1, ": "+ i)