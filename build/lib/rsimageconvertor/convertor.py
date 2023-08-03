import rawpy, imageio, pyheif
from PIL import Image
import os, sys, uuid

class Convertor:
	def __init__(self):
		self.folder = None
		# self.filename = os.path.split(folder)[1]

	def convertAll(self, folder):
		self.folder = folder
		allFiles = []
		for root, dirs, files in os.walk(self.folder):
			allFiles = files

		# input("Do you want to continue: ")
		formatt = input("PNG or JPG: ")
		for file in files:
			if file.endswith(".dng"):
				file = os.path.join(root, file)
				print(file)
				print("Reading RAW")
				
				with rawpy.imread(file) as raw:
					print("Processing RAW")
					rgbFile = raw.postprocess()

				if formatt.lower() == "jpg":

					print("Saving JPG format")
					print()
					imageio.imsave(file.replace("dng", "jpg"), rgbFile)

				elif formatt.lower() == "png":

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

				if formatt.lower() == "jpg":

					print("Saving as JPG")
					rgbFile.save(file.replace("heic", "jpg"), "JPEG")

				elif formatt.lower() == "png":

					print("Saving as PNG")
					rgbFile.save(file.replace("heic", "png"), "PNG")

	def convertOne(self, filePath):

		root, filename = os.path.split(filePath)
		if filename.endswith(".dng"):
			file = os.path.join(root, filename)
			print(file)
			print("Reading RAW")
			
			with rawpy.imread(file) as raw:
				print("Processing RAW")
				rgbFile = raw.postprocess()

			formatt = input("PNG or JPG: ")
			if formatt.lower() == "jpg":

				print("Saving JPG format")
				print()
				imageio.imsave(file.replace("dng", "jpg"), rgbFile)

			elif formatt.lower() == "png":

				print("Saving PNG format")
				print()
				imageio.imsave(file.replace("dng", "png"), rgbFile)


		elif filename.endswith(".heic"):
			print(filename)
			print("Reading HEIC")
			file = os.path.join(root, filename)
			heicFile = pyheif.read(file)
			print("Converting to Image format")
			rgbFile = Image.frombytes(heicFile.mode, 
	    				heicFile.size, 
	    				heicFile.data,
	    				"raw",
	    				heicFile.mode,
	    				heicFile.stride,)

			formatt = input("PNG or JPG: ")
			if formatt.lower() == "jpg":

				print("Saving as JPG")
				rgbFile.save(file.replace("heic", "jpg"), "JPEG")

			elif formatt.lower() == "png":

				print("Saving as PNG")
				rgbFile.save(file.replace("heic", "png"), "PNG")

	def compressOne(self, image, size, form = "same"):

		divSize = 1024 if sys.platform == "win32" else 1000

		if form not in ["same", "png", "jpg", "jpeg"]:
			print("Invalid image format requested")
			return -1

		else:

			print("Original Picture size:", os.stat(image).st_size / divSize, "KB")
			imageName = os.path.basename(image)
			directory = os.path.dirname(image)

			# directory, imageName = os.path.split(image)

			print("Image Name:", imageName)
			print("Export directory:", directory)

			extension = os.path.splitext(imageName)[-1]
			print("Original Image Extension:", extension)
			print("Export Image Extension:", form)
			
			minus = 2

			# imgName = os.path.split(image)[-1][:-4]

			# This approach b/c some image names could contain extra
			# dots i.e. FGDD5.4.4.jpg as I encountered myself
			# if imageName.endswith(".jpeg"): 
			# 	imgName = imageName[:-5]
			# else:
			# 	imgName = imageName[:-4]

			imgName = os.path.splitext(imageName)[0]
			print("Image Name:", imgName)

			uu = uuid.uuid4()
			uu = str(uu.node)
			
			if form == "same":
				outname = uu + extension
			else:
				outname = uu + '.' + form

			image = Image.open(image)

			while True:
				width = image.width
				height = image.height

				# ff = (width * minus) / 100
				# reqWidth = width - ff
				# cof = width / reqWidth
				# reqHeight = height / cof

				reqWidth = width - minus
				reqHeight = self.adjHeight(width, height, reqWidth)

				print("Req W:", reqWidth)
				print("Req H:", reqHeight)

				image = image.resize((reqWidth, reqHeight))
				# image = image.convert("RGB")
				image.save(outname, quality = 85,
					optimize = True
					)

				finalSize = os.stat(os.path.abspath(outname)).st_size / divSize
				print(f"{finalSize} KB", end = "\r")

				if finalSize <= size:
					print("GOTCHA")
					if form == "same":
						image.save(os.path.join(directory, f"{imgName}E.{extension}"), quality = 85, optimize = True)
					else:
						image.save(os.path.join(directory, f"{imgName}E.{form}"), quality = 85, optimize = True)
					os.remove(outname)
					break
				else:
					minus += 1

	def adjHeight(self, sourceWidth, sourceHeight, width):
		return (sourceHeight * width) // sourceWidth

	def adjWidth(self, sourceWidth, sourceHeight, height):
		return (height * sourceWidth) // sourceHeight

if __name__ == "__main__":
	con = Convertor()
	con.compressOne("/home/rapidswords/Desktop/pexels-stephan-seeber-1261728.jpg",
		1500, "jpg")