from scipy.io import loadmat
import numpy as np
from torch.utils.data import Dataset
import torchvision
from enum import Enum
import os
from PIL import Image
import math
import logging
from pathlib import Path
import shutil
import random
import cv2
from imutils import paths
from tensorflow.keras.preprocessing.image import img_to_array

  
class CVPreClass:
	def __init__(self):
		pass
	def resize_ignore_aspect(data,h,w):
		ret = []
		for img in data:
			ret.append(cv2.resize(img,(w,h),interpolation=cv2.INTER_AREA))
		return np.array(ret)
			
	def keras_dim_rearrange(data,dataFormat=None):
		ret =[]
		for img in data:
			ret.append(img_to_array(img, data_format=dataFormat))
		return np.array(ret)
	def mat_to_classes_array(pathtomat,test=False):
		mat = loadmat(pathtomat)
		a = mat['annotations'][0]
		ret =[]
		ret_classes ={}
		file_index = 5
		class_index = 4

		for el in a:
			ret.append([str(el[0][0]).split(sep="/")[1],el[5][0][0]])
			if el[5][0][0] not in ret_classes:
				ret_classes[el[5][0][0]] = []
			ret_classes[el[5][0][0]].append(str(el[0][0]).split(sep="/")[1])
		return ret,ret_classes
	
	def create_classes_folders(pathtomat,imgsdir,outdir='dataset/'):
		arr,arr_dict = mat_to_classes_array(pathtomat)
		for el in arr:
			#create class folder if does not exist
			Path(outdir+str(el[1])).mkdir(parents=True, exist_ok=True)
			shutil.copy(imgsdir+"/"+str(el[0]),outdir+str(el[1])+"/"+str(el[0]))
		return None
	def train_test_split_per_class(pathtomat,train=0.8,val=0.1,imgsdir='car_ims',outdir='dataset/'):
		arr,arr_dict = mat_to_classes_array(pathtomat)
		for cls in arr_dict:
			farr = arr_dict[cls]
			n = len(farr)
			train_size = math.ceil(train*n)
			val_size = math.ceil(val*n)
			test_size = n - train_size - val_size
			#shuffle list of files 
			random.shuffle(farr)
			#print(farr)
			train_set = farr[0:train_size]
			val_set = farr[train_size:(train_size+val_size)]
			test_set = farr[(train_size+val_size):]
        
			train_path = outdir+'train_spl/'+str(cls) +'/'
			test_path= outdir+'test_spl/' + str(cls) + '/'
			val_path= outdir+'val_spl/' + str(cls) + '/'
			#create class folder if does not exist
			Path(train_path).mkdir(parents=True, exist_ok=True)
			Path(test_path).mkdir(parents=True, exist_ok=True)
			Path(val_path).mkdir(parents=True, exist_ok=True)
			for el in train_set:
				shutil.copy(imgsdir+"/"+str(el),train_path+str(el))
			for el in test_set:
				shutil.copy(imgsdir+"/"+str(el),test_path+str(el))
			for el in val_set:
				shutil.copy(imgsdir+"/"+str(el),val_path+str(el))
			print(cls,"- Train:",str(train_size)," -Val: ",str(val_size)," -Test: ",str(test_size))
			
		return None
	def Classes_as_strings(pathtomat="cars_meta.mat"):
		ret = []
    
		mat = loadmat(pathtomat)
		for el in mat['class_names'][0]:
			ret.append(el[0])
		return ret
	
	def load_images(imgPath, verbose=-1):
		# initialize the list of features and labels
		data = []
		labels = []
		imagePaths = list(paths.list_images(imgPath))

		# loop over the input images
		for (i, imagePath) in enumerate(imagePaths):
			# load the image and extract the class label assuming
			# that our path has the following format:
			# /path/to/dataset/{class}/{image}.jpg
			image = cv2.imread(imagePath)
			label = imagePath.split(os.path.sep)[-2].split(sep='/')[-1]
			#print(labels)


			# treat our processed image as a "feature vector"
			# by updating the data list followed by the labels
			data.append(image)
			labels.append(label)

			# show an update every `verbose` images
			if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
				print("[INFO] processed {}/{}".format(i + 1,
				len(imagePaths)))

			# return a tuple of the data and labels
		return (np.array(data), np.array(labels))
		
		
	
		