import cv2
import os
import fiftyone as fo
from fiftyone import ViewField as F

# Filter the dataset by a specific class

train = fo.zoo.load_zoo_dataset(
    "coco-2017",
    split="train",
    label_types=["detections"],
    classes=["person"]
)
val = fo.zoo.load_zoo_dataset(
    "coco-2017",
    split="validation",
    label_types=["detections"],
    classes=["person"]
)


train = train.filter_labels("ground_truth", F("label") == "person")

val = val.filter_labels("ground_truth", F("label") == "person")


def get_dataset(mode: str, dataset): 
    try:
        os.makedirs('/person_detection/images/train')
        os.makedirs('/person_detection/images/val')
        os.makedirs('/person_detection/images/test')
        os.makedirs('/person_detection/labels/train')
        os.makedirs('/person_detection/labels/val')
    except FileExistsError:
        pass
    for i in dataset:
        filepath = i['filepath']
        name = os.path.basename(filepath)
        for k in i['ground_truth'].detections:
            x,y,w,h = k.bounding_box
            with open(f'data/labels/{mode}/{name[:-4]}.txt', 'a') as label:
                label.write(f'0 {x} {y} {w} {h}\n')

        image = cv2.imread(filepath)
        cv2.imwrite(f'data/images/{mode}/{name}', image)
        print(f'data/images/{mode}/{name}')

if __name__ == '__main__':
    get_dataset(mode = 'train', dataset = train)
    get_dataset(mode = 'val', dataset = val)
    


