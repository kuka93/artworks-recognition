# USAGE
# python search.py --db artworks.csv --artworks artworks --query queries/query01.png

# import the necessary packages
from lib.artworkdescriptor import ArtworkDescriptor
from lib.artworkmatcher import ArtworkMatcher
import argparse
import glob
import csv
import cv2
import numpy as np
import urllib


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--db", required = True,
	help = "path to the book database")
ap.add_argument("-a", "--artworks", required = True,
	help = "path to the directory that contains our artworks")
ap.add_argument("-q", "--query", required = True,
	help = "path to the query artwork")
args = vars(ap.parse_args())

# initialize the database dictionary of artworks
db = {}

# loop over the database
for l in csv.reader(open("artworks.csv")):
	# update the database using the image ID as the key
	db[l[0]] = l[1:]

# initialize the artwork descriptor and artwork matcher
cd = ArtworkDescriptor()
cv = ArtworkMatcher(cd, glob.glob(args["artworks"] + "/*.jpg"))

# load the query image, convert it to grayscale, and extract keypoints and descriptors
queryImage = cv2.imread(args["query"])

# read the query image from URL
# resp = urllib.urlopen("http://www.viviversilia.it/images/girasoli.jpeg")
# queryImage = np.asarray(bytearray(resp.read()), dtype="uint8")
# queryImage = cv2.imdecode(queryImage, cv2.IMREAD_COLOR)

gray = cv2.cvtColor(queryImage, cv2.COLOR_BGR2GRAY)
(queryKps, queryDescs) = cd.describe(gray)

# try to match the artwork to a known database of images
results = cv.search(queryKps, queryDescs)

# show the query artwork
cv2.imshow("Query", queryImage)

# check to see if no results were found
if len(results) == 0:
	print "I could not find a match for that artwork!"
	cv2.waitKey(0)

# otherwise, matches were found
else:
	# loop over the results
	for (i, (score, awPath)) in enumerate(results):
		# grab the book information
		(author, title) = db[awPath[awPath.rfind("\\") + 1:]]
		print "%d. %.2f%% : %s - %s" % (i + 1, score * 100, author, title)

		# load the result image and show it
		result = cv2.imread(awPath)
		cv2.imshow("Result", result)
		cv2.waitKey(0)