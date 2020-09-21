import cv2
import numpy as np


def resize_with_padding(img, size1, size2):
    h, w = img.shape[0:2]

    scale_factor = min(size1 / w, size2 / h)
    new_w, new_h = int(np.round(w * scale_factor)), int(np.round(h * scale_factor))
    target_w, target_h = size1, size2
    pad_left, pad_top = (target_w - new_w) // 2, (target_h - new_h) // 2  # a//b 等价于 int(a/b)

    if new_w != w or new_h != h:
        # cv2.INTER_AREA可以避免锯齿效应但速度不及cv2.INTER_LINEAR
        img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

    if new_w != target_w or new_h != target_h:
        img = cv2.copyMakeBorder(img,
                                 pad_top, target_h - pad_top - new_h,  # 上下
                                 pad_left, target_w - pad_left - new_w,  # 左右
                                 cv2.BORDER_CONSTANT)

    return img, ((w, h), (new_w, new_h), (target_w, target_w), (pad_left, pad_top))


if __name__ == "__main__":
    img_path = "../data/image/train.jpg"
    img = cv2.imread(img_path)
    cv2.imshow('before', img)

    copied_img = img.copy()
    copied_img = cv2.resize(copied_img, (256, 256))  # 无法保持图像长宽比
    cv2.imshow("simple_resize", copied_img)

    img, append_info = resize_with_padding(img, 256, 256)  # 可以保持图像长宽比
    cv2.imshow('resize_with_padding', img)
    cv2.waitKey()
