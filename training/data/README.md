## Datasets

1. Threat detection: [Youtube-GDD](https://github.com/UCAS-GYX/YouTube-GDD/tree/main), [Gun detection dataset](https://drive.google.com/drive/folders/179q_MNjx0ipzybhdjpQTxVu3IbI-5lWl)
2. Person and threat detection: [Youtube-GDD](https://github.com/UCAS-GYX/YouTube-GDD/tree/main)
3. Person detection: [MS COCO](https://cocodataset.org/#download)
4. Face recognition: Creates dataset based on photos of the class.

## Preprocessing

### YOUTUBE-GDD

[Youtube-GDD](https://github.com/UCAS-GYX/YouTube-GDD/tree/main) is already preprocessed, you have to download the zip file, unzip it with the labels you want, and put them in the YOLO format on any directory you want(note that you'll have to change the path of the model's yaml file you want to train):

        YOUTUBE-GDD

                images

                        train
                        val
                        test

                labels

                        train
                        val

### Gun detection dataset

[Gun detection dataset](https://drive.google.com/drive/folders/179q_MNjx0ipzybhdjpQTxVu3IbI-5lWl) is not preprocessed for YOLO format, the preprocessing notebook is already on the drive. This is the default preprocessing from the drive, but you'll need to change some parameters if you want to use it, as I did.

### Person

### Face recognition dataset

If you want to make a classifier for a set of people, then you'll need to create a dataset where all these people are. There is 2 options:

1.  Create it from previous photos: You can create a dataset labeling each individual photo in their respective classes(in this case name), for example:

        data

                dad

                        image_1.jpg
                        image_2.jpg
                        image_3.jpg
                mom
                        image_4.jpg
                sister
                        image_5.jpg
                brother
                        image_6.jpg
                me
                        image_7.jpg

THE FILES NAMES MUST NOT REPEAT.

THE BIGGER THE DATASET, THE BETTER RESULTS.

# NOTE:

These datasets are already preprocessed:

Youtube-GDD

Gun Detection Dataset

access [here](https://drive.google.com/drive/folders/1S-LVrZYJnvE6kyAmZD0TXXXVHlIOJu1P)

To preprocess the person detection dataset, you have to run `dataset.py` from the respective folder. Then move the train data and validation data from `C:\\Users\\{user}\\fiftyone\\coco-2017\\` to the respective image folders from the current directory `/person_detection/YOLO_data/images/` and sort them in the corresponding folders. Your folder path would look:

                person_detection
                        default
                        YOLO_data
                                images
                                        train
                                                (here you have to move the images from train data)
                                        val
                                                (here you have to move the images from validation data)
                                        test
                                labels
                                        train
                                        val
                        dataset.py
                        person_detection_model.py
                        person_detection.yaml
