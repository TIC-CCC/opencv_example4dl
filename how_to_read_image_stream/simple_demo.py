import cv2

# 1. 读取本地视频中的图像流
video_path = "../data/video/recognize_licence_plate.mp4"
cap = cv2.VideoCapture(video_path)

# # 2. 读取本地摄像头的图像流
# camera_id = 0
# cap = cv2.VideoCapture(camera_id)

# # 3. 读取网络摄像头的图像流
# url = "rtsp://admin:aimall2018!@192.168.1.231"
# cap = cv2.VideoCapture(url)

if cap.isOpened():  # 判断是否正确读取到视频
    ret, frame = cap.read()
    while ret:  # 判断是否读取到当前帧
        """
        你可以在此处对frame进行处理
        """
        cv2.imshow("frame", frame)
        if cv2.waitKey(20) == 27:  # 阻塞50ms, 并判断是否按下按Esc键
            break  # 退出循环
        ret, frame = cap.read()  # 继续读取下一帧
