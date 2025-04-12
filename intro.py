import cv2

img = cv2.imread("Assets/image.jpg", cv2.IMREAD_COLOR)
# print(img.shape)
# print(img[0, 0])
#cv2.imshow("Taoheed", img)


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("Assets/GreyTaoheed.jpg", gray_img)

cv2.waitKey(0)

cv2.destroyAllWindows()