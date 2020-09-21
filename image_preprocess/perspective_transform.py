import cv2
import numpy as np

img_path = "../data/image/signboard.jpg"
img = cv2.imread(img_path)

centers = [[415, 177], [540, 291], [544, 377], [419, 269]]
dst_x0, dst_y0, dst_w, dst_h = 100, 100, 160, 32

# 透视变化
src = np.float32(centers)
dst = np.float32([[dst_x0, dst_y0], [dst_x0+dst_w, dst_y0], [dst_x0+dst_w, dst_y0+dst_h], [dst_x0, dst_y0+dst_h]])
perspective_matrix = cv2.getPerspectiveTransform(src, dst)
transformed_img = cv2.warpPerspective(img, perspective_matrix, (512, 256))

src_h = img.shape[0]
pad_bottom = src_h - 256
transformed_img = cv2.copyMakeBorder(transformed_img,
                                     0, pad_bottom,  # 上下
                                     0, 0,  # 左右
                                     borderType=cv2.BORDER_CONSTANT)

for center in centers:
    x, y = center
    cv2.circle(img, center=(x, y), radius=2, color=(0, 255, 0), thickness=1)


cv2.imshow("transformed", transformed_img)
cv2.waitKey()
