import cv2
import numpy as np

img_path = "../data/image/signboard.jpg"
img = cv2.imread(img_path)
cv2.imshow("origin_image", img)


# 仿射变换矩阵求解需要3组点
dst_x0, dst_y0, dst_w, dst_h = 100, 100, 160, 32
src_pts = [[415, 177], [540, 291], [544, 377]]
dst_pts = [[dst_x0, dst_y0], [dst_x0+dst_w, dst_y0], [dst_x0+dst_w, dst_y0+dst_h]]


# 仿射变化
src_pts = np.float32(src_pts)
dst_pts = np.float32(dst_pts)
perspective_matrix = cv2.getAffineTransform(src_pts, dst_pts)
transformed_img = cv2.warpAffine(img, perspective_matrix, (512, 256))


# draw result
src_h, src_w = img.shape[:2]
pad_bottom = src_h - 256
transformed_img = cv2.copyMakeBorder(transformed_img,
                                     0, pad_bottom,  # 上下
                                     0, 0,  # 左右
                                     borderType=cv2.BORDER_CONSTANT)  # 需要将transformed_img补边和原图高度相同，否则无法拼接
img = cv2.hconcat([img, transformed_img])  # 图像拼接

src_pts = src_pts.astype(np.int).tolist()
dst_pts[:, 0] += src_w
dst_pts = dst_pts.astype(np.int).tolist()

for i, (pt1, pt2) in enumerate(zip(src_pts, dst_pts)):
    x1, y1 = pt1
    x2, y2 = pt2
    cv2.line(img, (x1, y1), (x2, y2), color=(0, i*60, 255), thickness=1)
    cv2.circle(img, center=(x1, y1), radius=2, color=(0, 255, 0), thickness=2)
    cv2.circle(img, center=(x2, y2), radius=2, color=(0, 255, 0), thickness=2)

cv2.imshow("result", img)
cv2.waitKey()
