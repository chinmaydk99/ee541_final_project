# ee541_final_project
Motive:

The goal of this project was to use deep learning techniques for the task of American sign language detection. American sign language is a visual-gestural language used by deaf and hard- of-hearing individuals in the United States and Canada. It is a complex and rich language that relies on hand gestures, facial expressions, and body posture to convey meaning. We have built a custom CNN model to achieve this goal and also trained the non-pretrained ResNet-18 model to compare the performances of the two models.

Dataset:

The dataset comprises 87,000 images of American Sign Language (ASL) alphabets, each measuring 200x200 pixels, categorized into 29 distinct classes. These classes include 26 representing letters A-Z, and 3 vital categories: SPACE, DELETE, and NOTHING, crucial for
real-time applications and classification. While the training dataset is substantial for model development, the test dataset includes
only 29 images, emphasizing the importance of real-world testing scenarios. This dataset isvaluable for ASL recognition systems and can help in building robust models for sign language communication.

The link to the dataset is : [https://www.kaggle.com/datasets/grassknoted/asl-alphabet]

Files Description:

File 1: EE541_Project_Primary_CNN_Model.ipynb - This corresponds to the first model we built during the duration of this project. This is a fairly simple model with just 2 convolutional layers.

File 2: EE541_Project_Secondary_CNN_Model.ipynb - This corresponds to the second model we built during the duration of this project. This is an improved model when compared to the primary model in terms of performance (accuracy and loss)

File 3: EE541_Project_Final_CNN_Model.ipynb - This corresponds to the final model we built during the duration of this project. This is the best model out of the 3 models we built. It generalizes better and also a relatively large model with 5 convolutional layers.

File 4: EE541_Project_ResNet_Model.ipynb - This corresponds to the ResNet-18 model we used to compare our model's performances. This is not a pre-trained model but just a resnet model (untrained) which is trained on our custom dataset.

Getting Started:

Download the dataset from the above link mentoned into a directory.
Chose any of the models from the above 4 files and download into the same directory.
Run the program to train and test the model for the dataset.
Disclaimer: The libraries used in building the model have to be installed on your local machine.
