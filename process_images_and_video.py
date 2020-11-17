# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:51:25 2020

@author: bjorn

This script takes a video and makes images out of it, and vice-versa.
"""

import cv2
vid_path = "C:/Users/bjorn/OneDrive/Skrivbord/test_vid.mp4"
save_pic_path = "C:/Users/bjorn/OneDrive/Dokument/projects/object_detection_video/test_images"
vidcap = cv2.VideoCapture(vid_path)
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite(save_pic_path+"image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)