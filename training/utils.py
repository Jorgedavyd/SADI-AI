import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, Dense, GlobalMaxPooling2D
from tensorflow.keras.applications import VGG16
#Functionalities
def preprocess(sample):
    # Get the image data
    image = sample["filepath"]

    # Get the bounding box annotations
    bboxes = sample["open_images"]["detections"]
    # Format the bounding boxes as (xmin, ymin, xmax, ymax, label)
    bboxes = [(box["bbox"]["xmin"], box["bbox"]["ymin"],
               box["bbox"]["xmax"], box["bbox"]["ymax"],
               box["label"]) for box in bboxes]

    # Read the image file
    image = tf.io.read_file(image)
    image = tf.image.decode_image(image, channels=3)

    return image, bboxes

def to_tensorflow_dataset(dataset):
    
    dataset = dataset.map(preprocess)

    # Unpack the dataset into images and labels
    images, labels = zip(*dataset)

    # Convert the images and labels to TensorFlow tensors
    images = tf.stack(images)
    labels = tf.ragged.constant(labels)

    # Create a TensorFlow dataset
    dataset = tf.data.Dataset.from_tensor_slices((images, labels))

    return dataset
def build_model(): 
    input_layer = Input(shape=(120,120,3))
    
    vgg = VGG16(include_top=False)(input_layer)

    # Classification Model  
    f1 = GlobalMaxPooling2D()(vgg)
    class1 = Dense(2048, activation='relu')(f1)
    class2 = Dense(1, activation='sigmoid')(class1)
    
    # Bounding box model
    f2 = GlobalMaxPooling2D()(vgg)
    regress1 = Dense(2048, activation='relu')(f2)
    regress2 = Dense(4, activation='sigmoid')(regress1)
    
    facetracker = Model(inputs=input_layer, outputs=[class2, regress2])
    return facetracker

#Models

class FaceDetection(tf.Models):
    def __init__(self, data, facetracker):
        super(FaceDetection, self).__init__()
        self.model = facetracker
        self.data = data
    def compile(self, opt, classloss, localizationloss, **kwargs):
        super().compile(**kwargs)
        self.closs = classloss
        self.lloss = localizationloss
        self.opt = opt
    def train_step(self, batch, **kwargs): 
        
        X, y = batch
        
        with tf.GradientTape() as tape: 
            classes, coords = self.model(X, training=True)
            
            batch_classloss = self.closs(y[0], classes)
            batch_localizationloss = self.lloss(tf.cast(y[1], tf.float32), coords)
            
            total_loss = batch_localizationloss+0.5*batch_classloss
            
            grad = tape.gradient(total_loss, self.model.trainable_variables)
        
        self.opt.apply_gradients(zip(grad, self.model.trainable_variables))
        
        return {"total_loss":total_loss, "class_loss":batch_classloss, "regress_loss":batch_localizationloss}
    
    def test_step(self, batch, **kwargs): 
        X, y = batch
        
        classes, coords = self.model(X, training=False)
        
        batch_classloss = self.closs(y[0], classes)
        batch_localizationloss = self.lloss(tf.cast(y[1], tf.float32), coords)
        total_loss = batch_localizationloss+0.5*batch_classloss
        
        return {"total_loss":total_loss, "class_loss":batch_classloss, "regress_loss":batch_localizationloss}
        
    def call(self, X, **kwargs): 
        return self.model(X, **kwargs)
    
class FaceRecognition(FaceDetection):
    def __init__(self, face_recognition_model, data):
        super(FaceRecognition, self).__init__()

        
    def call(self, xb):
        return self.model(xb)