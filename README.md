# OpenCV-frame-multiprocessing
with this script, it will be possible to process video frames, may webcam input frames or a single image,
faster than usual mode, by multiprocessing and seprating frames into some parts and process each part by a thread and add
them into a queue, so finally stick the queue processing result together.\
there is two specific scripts in this repository that one of them works terminal bases and the other one developed to use for\
Gui systems like tkinter or may pyqt and other; we will introduce both of them.

# frame_multiprocessing Flowchart
Considering that a system contain 4 units of processing, so the script will seprating burden of processing into 4 units.\
if we have a video which has 60 min frames, so we can process for example first 10 frames with 4 units instead of 1 !!\
as a result, we have a output video 4 times faster than normal processing.
<a href="https://github.com/maze80/Soccer-Robot-Playground"><img src="https://s2.uupload.ir/files/screenshot_from_2023-03-03_17-43-33_bt4.png" alt="HSL" width="500"></a> \
diagnosing the number of system's core is automatically but in order to implement your own workers number, just try to change pool number: 
```
# default code to get number of processors

process_number = cv.getNumberOfCPUs()
pool = ThreadPool(processes = process_number)
```
```
# modifying

pool = ThreadPool(processes = 4)
```

