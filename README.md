
<!-- ![banner Image](Graphs/class_montage.jpg?raw=true "banner") -->

# Deep Learning Car Classification
credit: [Abdulaziz Alsshe](https://github.com/AbdulazizAlshehri) & [Ibrahin Alzuhairi](https://github.com/ibalzuhairi)

## About
Computer Vision project to classify cars picture by make and model. 
</br>
![Car Classification Cam Image](Graphs/car_classification_security_cam.png?raw=true "Car Classification Cam")


## 1. Dataset
Dataset used in this experiment is Stanford Car dataset [source](http://ai.stanford.edu/~jkrause/cars/car_dataset.html), which contains ~16k total images. We splited them as follows: ~9k for training, ~4k images for validation, ~3k for testing. 
</br> 
![Dataset Example Image](Graphs/dataset.jpg?raw=true "Dataset Example")

### Preparing Dataset
The original dataset had 16k images stored in one folder, where all labels provided in .mat file.
1) restructuring image files to the following LabelID/Imagefile.jpg

2) custom train_test split per class (Note: this will create a balanced split across all classes)

![Dataset_Preparation](Graphs/PreparingDataset.JPG?raw=true "Dataset Example")

## 2. Experiment

### ShalowNet Only

### MobileNet Only

### VGG16 Only

### Augmentation
Due to the small number of training data image-augmentation applied to the training data (i.e. scaling, rotation, brightness) to avoide overfitting, for example by applying augmentation on the following image:
</br>
<img src="Graphs/Augmentation_original.jpg" height="140">

the folllowwing 5 new images created:
![Augmentation Result Images](Graphs/Augmentation2.png?raw=true "Augmentation Result")

### MobileNet with Augmentation

### VGG16 with Augmentation

### Regularization

### MobileNet with Augmentation and Regularization

### VGG16 with Augmentation and Regularization

## 3. Conclusion


