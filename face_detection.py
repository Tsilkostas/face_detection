import cv2
detect= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img= cv2.VideoCapture("elon.jpg")

res, img= imp_img.read()
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces= detect.detectMultiScale(gray, 1.3, 5)

cv2.imshow("Elon Image", img)

cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()