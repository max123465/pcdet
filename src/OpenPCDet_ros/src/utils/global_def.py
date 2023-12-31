#! /usr/bin/env python3.8
"""
Created on 23 Dec 2022

@author: Kin ZHANG (https://kin-zhang.github.io/)
% Copyright (C) 2022, RPL, KTH Royal Institute of Technology

Part of codes also refers: https://github.com/kwea123/ROS_notes
"""

DETECTION_COLOR_MAP = {'Car': (255,255,255), 
'car': (255,255,255), 
'truck': (255,255,0),
'construction_vehicle': (255,255,0),
'bus': (255,255,0),
'trailer': (255,255,0),
'motorcycle': (255,255,0), 
'bicycle': (255,255,0),
'traffic_cone': (255,255,0),
                       'barrier': (255,255,0),
                       'Pedestrian': (0, 226, 255), 
                       'Cyclist': (141, 40, 255)} # color for detection, in format bgr

# connect vertic
LINES = [[0, 1], [1, 2], [2, 3], [3, 0]] # lower face
LINES+= [[4, 5], [5, 6], [6, 7], [7, 4]] # upper face
LINES+= [[4, 0], [5, 1], [6, 2], [7, 3]] # connect lower face and upper face
LINES+= [[4, 1], [5, 0]] # front face and draw x

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
