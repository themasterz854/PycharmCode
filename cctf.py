import cv2

im1 = cv2.imread("./image1.png", cv2.IMREAD_UNCHANGED)
im2 = cv2.imread("./image2.png", cv2.IMREAD_UNCHANGED)

result = cv2.bitwise_xor(im1, im2)
cv2.imshow("XOR", result)
cv2.waitKey(0)
