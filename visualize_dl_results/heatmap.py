import cv2
import numpy as np

from utils.draw_guassian import draw_umich_gaussian

img_path = "../data/image/apples.jpg"
img = cv2.imread(img_path)

h, w = img.shape[:2]
heatmap = np.zeros((h, w))

centers = [[75, 103], [275, 88], [178, 205], [414, 167]]
bboxes = [[18, 37, 137, 158], [213, 25, 333, 139], [89, 117, 270, 278], [339, 90, 482, 230]]

for center, bbox in zip(centers, bboxes):
    bbox_w, bbox_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    radius = int((bbox_w+bbox_h)/4)
    heatmap = draw_umich_gaussian(heatmap, center=center, radius=radius)

heatmap = (255 * heatmap).astype(np.uint8)
heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
cv2.imshow('heatmap', heatmap)

img = cv2.addWeighted(img, 0.5, heatmap, 0.5, 0)
cv2.imshow('heatmap_with_image', img)

cv2.waitKey()
