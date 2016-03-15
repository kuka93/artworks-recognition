# import the necessary packages
import numpy as np
import cv2

class ArtworkDescriptor:
	def __init__(self, kpMethod = "SIFT", descMethod = "SIFT"):
		# store the keypoint detection method and descriptor method
		self.kpMethod = kpMethod
		self.descMethod = descMethod

	def describe(self, image):
		# detect keypoints in the image
		detector = cv2.FeatureDetector_create(self.kpMethod)
		kps = detector.detect(image)

		# extract local invariant descriptors from each keypoint, then convert the keypoints to a numpy array
		extractor = cv2.DescriptorExtractor_create(self.descMethod)
		(kps, descs) = extractor.compute(image, kps)
		kps = np.float32([kp.pt for kp in kps])

		# return a tuple of keypoints and descriptors
		return (kps, descs)