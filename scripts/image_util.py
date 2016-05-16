import cv2
import numpy as np
import os
from read_config import read_config

map_x = (read_config()["map_size"][0])
map_y = (read_config()["map_size"][1])
MAP_SHAPE = (((map_x * (20 + 4)) + 4), ((map_y * (20 + 4)) + 4), 3)

up = cv2.imread("../img/up.jpg")
down = cv2.imread("../img/down.jpg")
left = cv2.imread("../img/left.jpg")
right = cv2.imread("../img/right.jpg")
goal = cv2.imread("../img/goal.jpg")
wall = cv2.imread("../img/wall.jpg")
pit = cv2.imread("../img/pit.jpg")

img_map = {
    "WALL": wall,
    "PIT": pit,
    "GOAL": goal,
    "N": up,
    "S": down,
    "W": left,
    "E": right
}

height, width, layers = MAP_SHAPE

def save_image_for_iteration(policy_list, iteration):
    #Creating an empty map of white spaces
    empty_map = np.zeros(MAP_SHAPE)
    empty_map.fill(255)
    for row in range(len(policy_list)):
        for col in range(len(policy_list[0])):
            new_pos_row = ((row + 1) * 4) + (row * 20)
            new_pos_col = ((col + 1) * 4) + (col * 20)
            empty_map[new_pos_row : new_pos_row + 20, new_pos_col : new_pos_col + 20] = img_map[policy_list[row][col]]
    cv2.imwrite("../saved_video/iteration_" + str(iteration) + ".jpg", empty_map)


def generate_video(no_of_iterations):
    video = cv2.VideoWriter("../saved_video/video.avi", cv2.cv.CV_FOURCC('m', 'p', '4', 'v'), 1, (width, height))

    for i in range(no_of_iterations):
        file_name = "../saved_video/iteration_" + str(i) + ".jpg"
        img = cv2.imread(file_name)
        video.write(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
        #This removes the image after stitching it to the video. Please comment this if you want the images to be saved
        os.remove(file_name)
    video.release()
