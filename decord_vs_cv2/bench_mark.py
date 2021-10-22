from block_timer.timer import Timer
import cv2
from decord import VideoReader
from decord import cpu, gpu


def opencv_decode(file_path: str):
    with Timer(title='CV2'):
        cap = cv2.VideoCapture(file_path)
        while True:
            success, _ = cap.read()
            if not success:
                break


def decode_decode(file_path: str):
    with Timer(title='Decode'):
        vr = VideoReader(file_path)
        while True:
            batch = vr.next()
            if not batch:
                break


if __name__ == '__main__':
    video_path = './S001C001P001R001A001_rgb.avi'
    # opencv_decode(video_path)
    decode_decode(video_path)
