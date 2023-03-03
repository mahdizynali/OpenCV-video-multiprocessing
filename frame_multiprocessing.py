from multiprocessing.pool import ThreadPool
from collections import deque
import cv2 as cv
import time


def frameProcessing (frame, t0):
    '''in this function, each frame of video will be processed'''
    
    # for example we try to creat a circle on each frame of video
    # you can put your own procedure instead of bellow
    cv.circle(frame,(200, 50), 30, (0,255,0), 0)

    return frame, t0


def multiprocess ():
    '''multiprocess function sets core numbers and makes queue of processing and strats process'''
    
    
    # declaring input and output file
    cap = cv.VideoCapture("input.mp4")   
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv.CAP_PROP_FPS)
    output = cv.VideoWriter("output.mp4",cv.VideoWriter_fourcc(*"mp4v"), fps, (width, height))  
      
    # set processors
    process_number = cv.getNumberOfCPUs()
    pool = ThreadPool(processes = process_number)
    queue = deque()
    time.process_time()

    while True:       
        while len(queue) > 0 and queue[0].ready():
            result, t0 = queue.popleft().get() 
            cv.imshow('result video', result)
            output.write(result) # write output video file
            
        if len(queue) < process_number:
            _ret, frame = cap.read()
            
            if not _ret:
                time.sleep(0.1) # stop process if frames become empty
                break
            
            t = time.process_time()
            
            process_queue = pool.apply_async(frameProcessing, (frame.copy(), t))
            queue.append(process_queue)
            
        display = cv.waitKey(1)
        if display == 27:
            time.sleep(0.1)
            break
        
    cap.release()
    output.release()


multiprocess()
cv.destroyAllWindows()