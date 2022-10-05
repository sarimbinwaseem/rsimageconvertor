import sys, os, uuid
from PIL import Image

image = "/home/rapidswords/FM/Edited/FM8/To Upload/FM008.png"
print(os.stat(image).st_size/1000/1000)
imageName = os.path.basename(image)
print(imageName)

extension = imageName.split('.')[-1]
print(extension)

# imgName = os.path.split(image)[-1][:-4]
imgName = imageName[:-4]
print(imgName)

uu = uuid.uuid4()
uu = str(uu.node)
outname = uu + '.' + extension

image = Image.open(image)
minus = 20

while True:
	image = image.resize((image.width - minus, image.height - minus))
	image = image.convert("RGB")
	image.save(outname, quality = 95, optimize = True)

	finalSize = os.stat(os.path.abspath(outname)).st_size/1000/1000
	print(finalSize)

	if finalSize <= 2:
		print("GOTCHA")
		image.save(f"{imgName}E.{extension}", quality = 95, optimize = True)
		os.remove(outname)
		break
	else:
		minus += 20
