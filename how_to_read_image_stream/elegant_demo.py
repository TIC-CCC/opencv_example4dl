import cv2
import logging
import time


def get_frame(source):
    cap = None
    while True:
        while cap is None:
            cap = cv2.VideoCapture(source)
            if not cap.isOpened():
                logging.error('Error opening video stream')
                cap = None
                time.sleep(60)
            else:
                logging.info('Success opening video stream')

        ret, frame = cap.read()
        if ret:
            yield frame
        else:
            logging.error('Error reading frame from video stream')
            cap = None


if __name__ == "__main__":
    video_path = "../data/video/recognize_licence_plate.mp4"
    camera_id = 0
    url = "rtsp://admin:aimall2018!@192.168.1.231"

    inp_src = video_path
    for frame in get_frame(inp_src):  # 关键字yield使得get_frame变成一个迭代器(generator)
        """
        你可以在此处对frame进行处理
        """
        cv2.imshow('frame', frame)
        k = cv2.waitKey(20)
        if k == 27:
            break
