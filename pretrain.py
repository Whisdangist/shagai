import os

dir_ = "pos"
ii = 1
namelist = []

if dir_ == "pos":
	for file in os.listdir("pos"):
		os.rename("pos/" + file, "pos/pos_%.3d.jpg" % ii)
		namelist.append("pos/pos_%.3d.jpg 1 0 0 40 30\n" % ii)
		ii = ii + 1

	with open("pos.txt", "w") as fo:
		fo.writelines(namelist)

elif dir_ == "neg":
	for file in os.listdir("neg"):
		os.rename("neg/" + file, "neg/neg_%.3d.jpg" % ii)
		namelist.append("neg/neg_%.3d.jpg\n" % ii)
		ii = ii + 1

	with open("neg.txt", "w") as fo:
		fo.writelines(namelist)

elif dir_ == "test":
	for file in os.listdir("test"):
		os.rename("test/" + file, "test/test_%.3d.jpg" % ii)
		ii = ii + 1
