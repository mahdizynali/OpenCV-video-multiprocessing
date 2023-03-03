# OpenCV-frame-multiprocessing
with this script, it will be possible to process video frames, may webcam input frames or a single image,
faster than usual mode, by multiprocessing and seprating frames into some parts and process each part by a thread and add
them into a queue, so finally stick the queue processing result together.

# Script Flowchart
considering that a system contain 4 unit of processing, so the script will seprating burden of processing into 4 unit
<a href="https://github.com/maze80/Soccer-Robot-Playground"><img src="https://s2.uupload.ir/files/screenshot_from_2023-03-03_17-43-33_bt4.png" alt="HSL" width="500"></a>
