import cv2
from pymediainfo import MediaInfo


def test_mediainfo(path):
    mi = MediaInfo.parse(path).video_tracks[0]
    width, height = mi.width, mi.height
    fps, count = float(mi.frame_rate), int(mi.frame_count)


def test_cv2(path):
    cap = cv2.VideoCapture(str(path))
    width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps, count = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)
