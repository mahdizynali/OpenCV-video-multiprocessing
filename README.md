# OpenCV Video Parallel Processing

<p align="center">
  <strong>Fast and simple OpenCV video frame processing with Python, worker pools, queues, and Tkinter GUI support.</strong>
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python">
  </a>
  <a href="https://opencv.org/">
    <img src="https://img.shields.io/badge/OpenCV-4.x-green.svg" alt="OpenCV">
  </a>
  <a href="https://docs.python.org/3/library/tkinter.html">
    <img src="https://img.shields.io/badge/GUI-Tkinter-orange.svg" alt="Tkinter">
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  </a>
</p>

---

## Overview

`OpenCV-video-multiprocessing` is a small educational project that demonstrates how to process video frames faster and more cleanly using OpenCV, Python worker pools, and a frame queue.

The repository includes two examples:

- `frame_multiprocessing.py` — command-line OpenCV video processing.
- `tk_multiprocessing.py` — Tkinter GUI example that keeps the interface responsive while video processing runs.

> Important: the current implementation uses `multiprocessing.pool.ThreadPool`, so it is best described as **threaded/asynchronous frame processing**, not true process-based multiprocessing.

---

## Why this project is useful

Processing video frame by frame in a single loop can become slow when each frame needs expensive OpenCV operations.

This project shows a simple pattern for improving throughput:

1. Read frames from a video source.
2. Send frames to a worker pool.
3. Store pending results in a queue.
4. Collect processed frames when they are ready.
5. Display and save the processed video.

This is useful for:

- OpenCV experiments
- video preprocessing pipelines
- webcam or camera demos
- frame-by-frame computer vision tasks
- GUI applications that should not freeze
- learning how to structure asynchronous video processing

---

## Features

- Process video frames using a worker pool
- Automatically detect available CPU cores
- Keep processed frames organized with a queue
- Display output frames with OpenCV
- Save processed frames into a video file
- Tkinter GUI example with non-blocking processing
- Easy-to-customize `frameProcessing()` function
- Includes sample `input.mp4` for quick testing

---

## Repository structure

```text
OpenCV-video-multiprocessing/
├── frame_multiprocessing.py   # OpenCV video processing example
├── tk_multiprocessing.py      # Tkinter GUI processing example
├── input.mp4                  # Sample input video
├── README.md                  # Project documentation
└── LICENSE                    # MIT license
```

---

## How it works

The project is built around a custom frame-processing function:

```python
def frameProcessing(frame, t0):
    """
    Process one video frame.

    Parameters
    ----------
    frame:
        The current OpenCV frame.
    t0:
        Timestamp or frame timing value.

    Returns
    -------
    frame, t0:
        The processed frame and its timing value.
    """

    # Add your OpenCV logic here.
    cv.circle(frame, (200, 50), 30, (0, 255, 0), 0)

    return frame, t0
```

Frames are submitted to a worker pool:

```python
process_number = cv.getNumberOfCPUs()
pool = ThreadPool(processes=process_number)
```

Each frame is processed asynchronously:

```python
process_queue = pool.apply_async(frameProcessing, (frame.copy(), t))
queue.append(process_queue)
```

When a frame is ready, it is collected from the queue, displayed, and written to the output video.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mahdizynali/OpenCV-video-multiprocessing.git
cd OpenCV-video-multiprocessing
```

### 2. Create a virtual environment

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install opencv-python
```

Tkinter is included with many Python installations. On some Linux distributions, you may need to install it manually:

```bash
sudo apt install python3-tk
```

---

## Usage

### Run the OpenCV example

```bash
python frame_multiprocessing.py
```

This will:

1. Read `input.mp4`
2. Process its frames
3. Show the processed frames in an OpenCV window
4. Save the result as `output.mp4`

Press `Esc` to stop the OpenCV window.

---

### Run the Tkinter GUI example

```bash
python tk_multiprocessing.py
```

Click the **Start process** button to begin video processing.

The processing runs in a separate thread, so the Tkinter window stays responsive while the video is being processed.

---

## Use your own video

Change this line:

```python
cap = cv.VideoCapture("input.mp4")
```

Example:

```python
cap = cv.VideoCapture("my_video.mp4")
```

You can also use a webcam:

```python
cap = cv.VideoCapture(0)
```

---

## Change output video settings

The output video is created with `cv.VideoWriter`.

For MP4 output:

```python
output = cv.VideoWriter(
    "output.mp4",
    cv.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)
```

For AVI output:

```python
output = cv.VideoWriter(
    "output.avi",
    cv.VideoWriter_fourcc("M", "J", "P", "G"),
    fps,
    (width, height)
)
```

> Make sure the output file extension and codec match. If they do not match, the generated video may not play correctly.

---

## Customize frame processing

To use your own OpenCV logic, edit only the body of `frameProcessing()`.

Keep the same input and return format:

```python
def frameProcessing(frame, t0):
    # Your processing code here
    return frame, t0
```

### Example: grayscale output

```python
def frameProcessing(frame, t0):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    result = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    return result, t0
```

### Example: Canny edge detection

```python
def frameProcessing(frame, t0):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 100, 200)
    result = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    return result, t0
```

### Example: resize frames

```python
def frameProcessing(frame, t0):
    result = cv.resize(frame, None, fx=0.5, fy=0.5)
    return result, t0
```

### Example: draw text on every frame

```python
def frameProcessing(frame, t0):
    cv.putText(
        frame,
        "Processed with OpenCV",
        (30, 50),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    return frame, t0
```

---

## Change the number of workers

By default, the script uses the number of CPU cores detected by OpenCV:

```python
process_number = cv.getNumberOfCPUs()
pool = ThreadPool(processes=process_number)
```

You can manually set the number of workers:

```python
process_number = 4
pool = ThreadPool(processes=process_number)
```

A higher worker count is not always faster. The best value depends on:

- CPU model
- video resolution
- frame-processing complexity
- memory usage
- whether the workload is mostly OpenCV/native code or pure Python

---

## Performance notes

This project is designed as a simple learning example.

Because it uses `ThreadPool`, it can be helpful when the heavy work is handled by OpenCV native functions or when processing includes I/O-like waiting.

For heavy pure-Python CPU-bound tasks, Python's Global Interpreter Lock may limit speedup. In that case, consider using:

- `multiprocessing.Pool`
- `concurrent.futures.ProcessPoolExecutor`
- Cython
- Numba
- native C++ OpenCV code

---

## GUI processing with Tkinter

The Tkinter example uses a separate thread to start the video-processing function:

```python
thread = threading.Thread(target=multiprocess)
```

Then the thread is started from a button:

```python
Button(
    window,
    text="Start process",
    bd=5,
    command=thread.start
).pack()
```

This prevents the GUI from freezing while OpenCV processing is running.

---

## Common issues

### Output video does not play

Check that the codec and file extension match.

For `.mp4`, try:

```python
cv.VideoWriter_fourcc(*"mp4v")
```

For `.avi`, try:

```python
cv.VideoWriter_fourcc("M", "J", "P", "G")
```

---

### OpenCV window does not close

Make sure the script checks for the `Esc` key:

```python
if cv.waitKey(1) == 27:
    break
```

Also make sure OpenCV windows are destroyed at the end:

```python
cv.destroyAllWindows()
```

---

### Tkinter window freezes

Use the threaded approach from `tk_multiprocessing.py`.

Do not run long video-processing loops directly inside a Tkinter button callback.

---

### Processing is not faster

Small frame operations may not benefit much from a worker pool.

Try testing with heavier operations such as:

- filtering
- object detection
- segmentation
- edge detection
- feature extraction
- image enhancement

Also try different worker counts.

---

## Recommended improvements

Good next steps for this project:

- Add `requirements.txt`
- Add command-line arguments for input/output paths
- Add webcam mode
- Add FPS benchmark output
- Add processing-time comparison between normal and threaded modes
- Add a true multiprocessing version with `ProcessPoolExecutor`
- Add example filters
- Add GitHub Actions for linting
- Add screenshots or GIF demos

---

## Recommended `requirements.txt`

```txt
opencv-python
```

Optional, if you want NumPy explicitly:

```txt
opencv-python
numpy
```

---

## Roadmap

- [ ] Add CLI arguments
- [ ] Add benchmark mode
- [ ] Add webcam support
- [ ] Add real multiprocessing example
- [ ] Add progress bar
- [ ] Add GUI file picker
- [ ] Add example filters
- [ ] Add FPS comparison table
- [ ] Add demo GIF to README

---

## Project description

Suggested GitHub repository description:

```text
OpenCV video frame processing with Python ThreadPool, queues, and Tkinter GUI support.
```

Suggested topics:

```text
opencv python video-processing multithreading threadpool tkinter computer-vision opencv-python
```

---

## License

This project is licensed under the MIT License.

See the [LICENSE](./LICENSE) file for details.

---

## Author

Created by [Mahdi Zeinali](https://github.com/mahdizynali).

If this project helped you, consider giving it a star.
