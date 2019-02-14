import os
from lxml import etree

file = open("fddb/a.txt", "w")
file_list = open("fddb/l.txt", "w")
# for file in os.listdir("test"):
for ii in range(1, 42):
	img = "test/test_%.3d" % ii
	elems = etree.parse(img+".xml")
	boxes = elems.xpath("//bndbox")
	print >> file, img
	print >> file_list, img
	print >> file, len(boxes)
	for box in boxes:
		x = int(box.xpath("xmin")[0].text)
		y = int(box.xpath("ymin")[0].text)
		w = int(box.xpath("xmax")[0].text) - x
		h = int(box.xpath("ymax")[0].text) - y
		print >> file, x, y, w, h, 1
file.close()
file_list.close()