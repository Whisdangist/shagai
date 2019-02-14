import os
from lxml import etree

annotations = open("fddb/a.txt", "w")
images_list = open("fddb/l.txt", "w")
label_path = "test/label/"
for label in os.listdir(label_path):
	elems = etree.parse(label_path+label)
	boxes = elems.xpath("//bndbox")
	folder = elems.xpath("folder")[0].text
	filename = elems.xpath("filename")[0].text.strip('.jpg')
	filepath = folder + "/" + filename
	print >> annotations, filepath
	print >> images_list, filepath
	print >> annotations, len(boxes)
	for box in boxes:
		x = int(box.xpath("xmin")[0].text)
		y = int(box.xpath("ymin")[0].text)
		w = int(box.xpath("xmax")[0].text) - x
		h = int(box.xpath("ymax")[0].text) - y
		print >> annotations, x, y, w, h, 120
annotations.close()
images_list.close()