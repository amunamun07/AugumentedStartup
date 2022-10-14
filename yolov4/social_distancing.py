import os
import cv2
import time
import math
import random
import numpy as np
from itertools import combinations


def is_close(p1, p2):
    """
    This function helps to calculate euclidian distance between two points
    :param p1: point one
    :param p2: point two
    :return: distance between point one and point two
    """
    return math.sqrt(p1 ** 2 + p2 ** 2)


def xywh_to_xyxy(x, y, w, h):
    """
    To convert xywh format bounding box to xyxy format bounding box
    :param x: center x coordinate
    :param y: center y coordinate
    :param w: width of bbox
    :param h: height of bbox
    :return: left top and right bottom coordinate
    """
    xmin = int(round(x - (w/2)))
    xmax = int(round(x + (w/2)))
    ymin = int(round(y - (h/2)))
    ymax = int(round(y + (h/2)))
    return xmin, ymin, xmax, ymax
