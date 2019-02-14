import cv2
import os


def run():
	for ii in range(1, 42):
		imgname = "test_%.3d" % ii
		img = cv2.imread('test/%s.jpg' % imgname)
		# path = "g:/data"
		# for cascade in os.listdir(path):
			# face_haar = cv2.CascadeClassifier(os.path.join(path, cascade))
		face_haar = cv2.CascadeClassifier("../cascade.xml")

		gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		#gray_img = cv2.GaussianBlur(gray_img, (5,5), 0, 0) 

		faces = face_haar.detectMultiScale(gray_img, 1.1, 3)
		for face_x,face_y,face_w,face_h in faces:
		    cv2.rectangle(img, (face_x, face_y), (face_x+face_w, face_y+face_h), (0,255,0), 2)

		#cv2.imwrite('d:/photo/08_3.jpg', img)
		cv2.namedWindow(imgname, cv2.WINDOW_NORMAL)
		cv2.setWindowProperty(imgname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
		cv2.imshow(imgname, img)
		key = cv2.waitKey(0)
		if key == 113:  # 'q'
			return
	cv2.destroyAllWindows()


run()