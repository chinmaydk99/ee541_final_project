# ee541_final_project
Motive:

The primary motive of the project is to bridge the communication gap for the deaf and hard-of-hearing community. Utilizing advanced computer vision and machine learning techniques, specifically a custom-built Convolutional Neural Network, the project aims to accurately interpret American Sign Language from images. This initiative not only enhances accessibility and inclusivity but also serves as an educational tool, promoting wider understanding and use of sign language. Ultimately, it strives to integrate the deaf community more seamlessly into a world dominated by verbal and auditory communication.

Dataset:

The dataset comprises 87,000 images of American Sign Language (ASL) alphabets, each measuring 200x200 pixels, categorized into 29 distinct classes. These classes include 26 representing letters A-Z, and 3 vital categories: SPACE, DELETE, and NOTHING, crucial for
real-time applications and classification. While the training dataset is substantial for model development, the test dataset includes
only 29 images, emphasizing the importance of real-world testing scenarios. This dataset isvaluable for ASL recognition systems and can help in building robust models for sign language communication.

The link to the dataset is : [https://www.kaggle.com/datasets/grassknoted/asl-alphabet]

Files Description:

File 1: Sign_Language_Final.ipynb - This corresponds to the final CNN model built for sign recognition. It comprises of 4 convolutional and pooling layers followed by batch normalization to stabilize training.

File 2: handTracker.py - This module is built using Mediapipe library to extract hand landmarks from live webcam feed and to process it and define the Region of Interest.

File 3: Final prediction module final.ipynb - This combines the earlier two files and we obtain predictions on live webcam feed.

File 4: model_card_ee541_group_24 - This gives a concise statement of the model and its training parameters, use cases and factors that might affect it's performance.

Getting Started:

Download the dataset from the above link mentoned into a directory.
Chose any of the models from the above 4 files and download into the same directory.
Run the program to train and test the model for the dataset.
Disclaimer: The libraries used in building the model have to be installed on your local machine.
