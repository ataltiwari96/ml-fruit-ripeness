import os
import sys
import cv2
import numpy as np

def color():
    img = cv2.imread('test1.jpg',0)
    img2 = img.copy()
    template = cv2.imread('ap.jpg',0)
    w, h = template.shape[::-1]
    methods = ['cv2.TM_SQDIFF']
    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        #print "",res
        a=res[0,0]
        b=np.int_(a)
        print "color=",b
        if (b>99000000):
            print "matched"
        else:
            print " no match"
    cv2.waitKey()
    return b

c=color()
if(c>99000000):
         print "Unrippen Fruit"
else:
	 print "ripened fruit"
