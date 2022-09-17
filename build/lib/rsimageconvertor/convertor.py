import rawpy, imageio, pyheif
from PIL import Image
import os

folder = input("Enter folder path: ")


allFiles = []
for root, dirs, files in os.walk(folder):
	allFiles = files

input("Do you want to continue: ")

for file in files:
	if file.endswith(".dng"):
		file = os.path.join(root, file)
		print(file)
		print("Reading RAW")
		
		with rawpy.imread(file) as raw:
			print("Processing RAW")
			rgbFile = raw.postprocess()

		print("Saving PNG format")
		print()
		imageio.imsave(file.replace("dng", "png"), rgbFile)

	elif file.endswith(".heic"):
		print(file)
		print("Reading HEIC")
		file = os.path.join(root, file)
		heicFile = pyheif.read(file)
		print("Converting to Image format")
		rgbFile = Image.frombytes(heicFile.mode, 
    				heicFile.size, 
    				heicFile.data,
    				"raw",
    				heicFile.mode,
    				heicFile.stride,)
		print("Saving as JPG")
		rgbFile.save(file.replace("heic", "jpg"), "JPEG")