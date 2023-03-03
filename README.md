# OpenCV-frame-multiprocessing
with this script, it will be possible to process video frames, may webcam input frames or a single image,
faster than usual mode, by multiprocessing and seprating frames into some parts and process each part by a thread and add
them into a queue, so finally stick the queue processing result together.\
there is two specific scripts in this repository that one of them works terminal bases and the other one developed to use for\
Gui systems like tkinter or may pyqt and other; we will introduce both of them.

# frame_multiprocessing.py
Considering that a system contain 4 units of processing, so the script will seprating burden of processing into 4 units.\
if we have a video which has 60 min frames, so we can process for example first 10 frames with 4 units instead of 1 !!\
as a result, we have a output video 4 times faster than normal processing.
<a href="https://github.com/maze80/Soccer-Robot-Playground"><img src="https://s2.uupload.ir/files/screenshot_from_2023-03-03_17-43-33_bt4.png" alt="HSL" width="500"></a> \
diagnosing the number of system's core is automatically but in order to implement your own workers number, just try to change pool number: 
```python
# default code to get number of processors

process_number = cv.getNumberOfCPUs()
pool = ThreadPool(processes = process_number)
```
```python
# modifying
pool = ThreadPool(processes = 4)
```
in order to use use this script, just you have to change frameProcessing function and put your own code :
```python
# Do not change return and input case of function !!

def frameProcessing (frame, t0):
    # you can put your own procedure here.

    return frame, t0
```

# tk_multiprocessing.py
In this script, we use an extra processor to make a switch case between script and gui program by creating a thread line that \
perform us to update ui window simultaneously when multiprocess is under working; it mean that the ui window won't intrrupt and never \
freeze during the procedure so we can set our orders into ui window :)) \
it's a sample of tkinter opencv video multiprocessing module that can be developed for other kind of gui systems. \
<a href="https://github.com/maze80/Soccer-Robot-Playground"><img src="https://s2.uupload.ir/files/screenshot_from_2023-03-03_18-20-48_auvd.png" alt="HSL" width="500"></a> \
with set a button into thread strater, all the issues will be handeled :
```python
# switch thread to the multiprocess function
thread = threading.Thread(target=multiprocess)

# for example, tk button , startsButton(window,text='start process',bd=5,command=thread.start).pack()
outlable=Label(window)
outlable.pack() thread line
Button(window,text='start process',bd=5,command=thread.start).pack()
outlable=Label(window).pack()
```

# Notice !!
there is a sample mp4 file in repo in order to test script, but if you want to use other formats to input and outout results, \
you have to modify this section of source code :
```python
cap = cv.VideoCapture("input.mp4")   
output = cv.VideoWriter("output.mp4",cv.VideoWriter_fourcc(*"mp4v"), fps, (width, height))  

# or maybe

cap = cv.VideoCapture("input.mp4")   
output = cv.VideoWriter("output.avi",cv.VideoWriter_fourcc(M','J','P','G'), fps, (width, height)) 
```
if the format of output file doesn't match to the processing encoding, video result won't be correct and never play.
