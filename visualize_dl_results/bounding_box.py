import cv2

img_path = "../data/image/apples.jpg"
img = cv2.imread(img_path)

bboxes = [[18, 37, 137, 158], [213, 25, 333, 139], [89, 117, 270, 278], [339, 90, 482, 230]]
for bbox in bboxes:
    x0, y0, x1, y1 = bbox
    cv2.rectangle(img, pt1=(x0, y0), pt2=(x1, y1), color=(0, 255, 0), thickness=1)

cv2.imshow("bounding boxes of apples", img)
cv2.waitKey()
