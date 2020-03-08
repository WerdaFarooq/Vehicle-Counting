# Python program to explain cv2.rectangle() method 

# importing cv2 
import cv2 
image = cv2.VideoCapture('VDO-Traffic_Drone View-16may1045hour.mp4')
# path 


# Reading an image in default mode 
#image = cv2.imread(cap) 

# Window name in which image is displayed 
window_name = 'Image'

# Start coordinate, here (5, 5) 
# represents the top left corner of rectangle 
start_point = (5, 5) 

# Ending coordinate, here (220, 220) 
# represents the bottom right corner of rectangle 
end_point = (620, 620) 

# Blue color in BGR 
color = (255, 0, 0) 

# Line thickness of 2 px 
thickness = 2

# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle((900,800), start_point, end_point, color, thickness) 

# Displaying the image 
cv2.imshow(window_name, image) 
image.release()
image.destroyAllWindows()


##import cv2
##import numpy as np
## 
### create an overlay image. You can use any image
###foreground = np.ones((300,00,6),dtype='uint8')*255
### Open the camera
##cap = cv2.VideoCapture('VDO-Traffic_Drone View-16may1045hour.mp4')
##cap = cv2.rectangle(cap,(384,0),(510,128),(0,255,0),3)
##### Set initial value of weights
####alpha = 0.4
####while True:
####    # read the background
####    ret, background = cap.read()
####    background = cv2.flip(background,1)
####    # Select the region in the background where we want to add the image and add the images using cv2.addWeighted()
####    added_image = cv2.addWeighted(background[150:250,150:250],alpha,foreground[0:300,0:300,:],1-alpha,0)
####    # Change the region with the result
####    background[150:250,150:250] = added_image
####    # For displaying current value of alpha(weights)
####    font = cv2.FONT_HERSHEY_SIMPLEX
####   # cv2.putText(background,'alpha:{}'.format(alpha),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
##cv2.imshow('a',cap)
##k = cv2.waitKey(10)
##    # Press q to break
##
####    # press a to increase alpha by 0.1
####    if k == ord('a'):
####        alpha +=0.1
####        if alpha >=1.0:
####            alpha = 1.0
####    # press d to decrease alpha by 0.1
#))###    elif k== ord('d'):
####        alpha -= 0.1
####        if alpha <=0.0:
####            alpha = 0.0
### Release the camera and destroy all windows         
##cap.release()
##cv2.destroyAllWindows()
##
####import os
####from PIL import Image
####import cv2
####
####
####cap = cv2.VideoCapture('MAH00003.mp4')
####filename1 = 'sample_input_image.jpg'
####bg = Image.open(filename1, 'r')
####text_img = Image.new('RGBA', (600,320), (0, 0, 0, 0))
####text_img.paste(bg, (0,0))
####text_img.paste(cap, (0,0), mask=cap)
####text_img.save("ball.png", format="png")
####
######from tkinter import *
######import cv2
######
######root = Tk()
######image1 = cv2.imread('single_input_image.jpg')
######
######canvas = Canvas(image1)
######canvas.pack()
######canvas.create_rectangle(50,50,380,300, fill="yellow", outline="yellow")
######
######
######root.mainloop()
######
######from tkinter import *
######from PIL import Image, ImageTk
######
######root = Tk()
######
######images = []  # to hold the newly created image
######
######def create_rectangle(x1, y1, x2, y2, **kwargs):
######    if 'alpha' in kwargs:
######        alpha = int(kwargs.pop('alpha') * 255)
######        fill = kwargs.pop('fill')
######        fill = root.winfo_rgb(fill) + (alpha,)
######        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
######        images.append(ImageTk.PhotoImage(image))
######        canvas.create_image(x1, y1, image=images[-1], anchor='nw')
######    canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
######
######canvas = Canvas()
######canvas.pack()
######
######create_rectangle(10, 10, 200, 100, fill='blue')
######create_rectangle(50, 50, 250, 150, fill='green', alpha=.5)
######create_rectangle(80, 80, 150, 120, fill='#800000', alpha=.8)
######
######root.mainloop()
######
######list1, list2, list3, list4 = ([] for i in range(4))
######list3.append(5)
######print(list3)
######
######import numpy as np
######print(np.arange(start=1, stop=10, step=3))
######a = [2,5,20,50,[2,4,6]]
######k=1
######for x in a[0]:
######    diff_list = [] 
######    for x, y in zip(a[0][0::], a[0][1::]): 
######        diff_list.append(y-x)
######        print ("difference list: ", str(diff_list))
######     
########for x in range(0,10):
########    a[0].append(23)
########     
########for x in a[0]:
########    if (x % 2 == 0):
########        k *= x
###### 
#######print(k)
########n = 5
########lists=[1,2,3,4,5]
##########lists = [[] for _ in range(n)]
##########lists[2]=[1,2,3,4,5]
##########b=1,2,3
##########lists[3].append(b)
##########print(lists)
##########lists[3].append(2)
##########print(lists)
##########print(len(lists[3]))
#########print(lists[3]-lists[2])
########a=[1,2,3,4]
########b=[1,4,5,6,7]
########print(list(b-a))
##########import numpy as np
##########array= np.arange(27).reshape(3,3,3)
##########print(array)
##########
############n = 5
############lists = [[] for _ in range(n)]
############print(lists[7])
############
############
##############import numpy as np
##############result_array = np.empty((0, 100))
##############
##############for line in data_array:
##############    result = do_stuff(line)
##############    result_array = np.append(result_array, [result], axis=0)
############
##################from gtts import gTTS 
##################  
################### This module is imported so that we can  
################### play the converted audio 
################import os 
##################  
################### The text that you want to convert to audio 
##################mytext = 'Welcome to geeksforgeeks!'
##################  
################### Language in which you want to convert 
##################language = 'en'
##################  
################### Passing the text and language to the engine,  
################### here we have marked slow=False. Which tells  
################### the module that the converted audio should  
################### have a high speed 
##################myobj = gTTS(text=mytext, lang=language, slow=False) 
##################  
################### Saving the converted audio in a mp3 file named 
################### welcome  
##################myobj.save("welcome.mp3") 
##################
##################def filename():
##################   filename = "welcome.mp3"
##################   os.system("start " + filename)
##################
##################filename()
##################
################import pyttsx3
################engine = pyttsx3.init()
################
################engine.say("Your Text")
################
################engine.runAndWait()
###############print("d"+"\n"+"r")
##############import rhino
##############import scriptcontext
##############import System.Guid
##############
##############def FindObjectsByName():
##############    name = "abc"
##############    settings = Rhino.DocObjects.ObjectEnumeratorSettings()
##############    settings.NameFilter = name
##############    ids = [rhobj.Id for rhobj in scriptcontext.doc.Objects.GetObjectList(settings)]
##############    if not ids:
##############        print ("No objects with the name", name)
##############        return Rhino.Commands.Result.Failure
##############    else:
##############        print ("Found", len(ids), "objects")
##############        for id in ids: print ("  ", id)
##############    return Rhino.Commands.Result.Success
##############
##############if __name__ == "__main__":
##############    FindObjectsByName()
