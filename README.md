
![banner Image](Graphs/class_montage.jpg?raw=true "banner")

# Deep Learning Car Classification

## About
Computer Vision project to classify cars picture by make and model. 
</br>
![Car Classification Cam Image](Graphs/car_classification_security_cam.png?raw=true "Car Classification Cam")


## Dataset
Dataset used in this experiment is Stanford Car dataset [source](http://ai.stanford.edu/~jkrause/cars/car_dataset.html), which contains ~16k total images. We splited them as follows: ~9k for training, ~4k images for validation, ~3k for testing. 
</br> 
![Dataset Example Image](Graphs/dataset.jpg?raw=true "Dataset Example")


## Augmentation

Due to the small number of training data image-augmentation applied to the training data (i.e. scaling, rotation, brightness) to avoide overfitting, for example by applying augmentation on the following image:
</br>
<img src="Graphs/Augmentation_original.jpg" height="140">

the folllowwing 5 new images created:
![Augmentation Result Images](Graphs/Augmentation2.png?raw=true "Augmentation Result")


