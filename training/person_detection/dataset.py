import os
import fiftyone as fo
from fiftyone import ViewField as F
import shutil



def copy_dataset(source_dir, destination_dir):
    # Get the list of files in the source directory
    files = os.listdir(source_dir)

    for file_name in files:
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)

        # Copy the file to the destination directory
        shutil.copy(source_file, destination_file)

    print("Dataset copied.")


# Call the function to copy files

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
    os.makedirs('YOLO_data/images/train', exist_ok=True)
    os.makedirs('YOLO_data/images/val', exist_ok=True)
    os.makedirs('YOLO_data/images/test', exist_ok=True)
    os.makedirs('YOLO_data/labels/train', exist_ok=True)
    os.makedirs('YOLO_data/labels/val', exist_ok=True)

    source_dir = f'C:\\Users\\jorge\\fiftyone\\coco-2017\\{mode}\\data'
    destination_dir = (os.getcwd(), f'YOLO_data/images/{mode}')
    

    copy_dataset(source_dir, destination_dir)

    for i in dataset:
        filepath = i['filepath']
        name = os.path.basename(filepath)
        for k in i['ground_truth'].detections:
            x,y,w,h = k.bounding_box
            with open(f'YOLO_dataset/labels/{mode}/{name[:-4]}.txt', 'a') as label:
                label.write(f'0 {x} {y} {w} {h}\n')


if __name__ == '__main__':
    get_dataset(mode = 'train', dataset = train)
    get_dataset(mode = 'val', dataset = val)
    


