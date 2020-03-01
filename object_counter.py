# -*- coding: utf-8 -*-
from utils.image_utils import image_saver
import numpy as np

current_frame_number_list = [0]
is_vehicle_detected = [0]
bottom_position_of_detected_vehicle = [0]
veh=[]

def count_objects(r, name1,top, bottom, right, left, crop_img, roi_position, y_min, y_max, deviation):   
        #print(current_frame_number)
        direction = "n.a." # means not available, it is just initialization
        speed = 0
        isInROI = True # is the object that is inside Region Of Interest
        update_csv = False
        #print(width)

        if (r==crop_img):
          update_csv = True
          is_vehicle_detected.insert(0,2)
          print("Detection.............")
          print(name1)
          veh.insert(0,name1)
          #update_csv = True
          #print(crop_img)
          print("##################")
          image_saver.save_image(crop_img) # save detected object image
        return (direction, speed, is_vehicle_detected, update_csv, veh)


##        if(bottom > bottom_position_of_detected_vehicle[0]):
##                direction = "↓" #down
##        else:
##                direction = "↑" #up
##
##        bottom_position_of_detected_vehicle.insert(0,(bottom))

        
##        if isInROI:
##                pixel_length = bottom - bottom_position_of_detected_vehicle[0]
##                scale_real_length = pixel_length * 44  # multiplied by 44 to convert pixel length to real length in meters (chenge 44 to get length in meters for your case)
##                total_time_passed = current_frame_number - current_frame_number_list[0]
##                scale_real_time_passed = total_time_passed * 24  # get the elapsed total time for a vehicle to pass through ROI area (24 = fps)
##                if scale_real_time_passed != 0:
##                    speed = scale_real_length / scale_real_time_passed / 1# performing manual scaling because we have not performed camera calibration
##                    speed = speed / 6 * 40  # use reference constant to get vehicle speed prediction in kilometer unit
##                    current_frame_number_list.insert(0, current_frame_number)
##                    bottom_position_of_detected_vehicle.insert(0, bottom)
                    #print(speed)

        #return (direction, speed, is_vehicle_detected, update_csv, name)


        #return direction, is_vehicle_detected, update_csv

