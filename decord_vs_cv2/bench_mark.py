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
    with Timer(title='Decord'):
        vr = VideoReader(file_path)
        for i in range(len(vr)):
            batch = vr[i]


if __name__ == '__main__':
    video_path = 'Sunny Bunnies _ The Big Bunny Race _ SUNNY BUNNIES COMPILATION _ Cartoons for Children [3SeoRakT74s].mp4'
    opencv_decode(video_path)
    decode_decode(video_path)

    """
    [CV2] Total time 18.47167 seconds.
    [Decord] Total time 28.63321 seconds.
    """
