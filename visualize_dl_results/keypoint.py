import cv2

img_path = "../data/image/apples.jpg"
img = cv2.imread(img_path)

centers = [[75, 103], [275, 88], [178, 205], [414, 167]]
for center in centers:
    x, y = center
    cv2.circle(img, center=(x, y), radius=2, color=(0, 255, 0), thickness=2)

cv2.imshow("keypoint of apples", img)
cv2.waitKey()
