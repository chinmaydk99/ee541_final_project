# Model card for "Computer Vision for American Sign Language Recognition"

Sections and prompts from the [model cards paper](https://arxiv.org/abs/1810.03993), v2.

Jump to section:

- [Model details](#model-details)
- [Intended use](#intended-use)
- [Factors](#factors)
- [Metrics](#metrics)
- [Evaluation data](#evaluation-data)
- [Training data](#training-data)
- [Quantitative analyses](#quantitative-analyses)
- [Ethical considerations](#ethical-considerations)
- [Caveats and recommendations](#caveats-and-recommendations)

## Model details

_Basic information about the model._

Review section 4.1 of the [model cards paper](https://arxiv.org/abs/1810.03993).

- Chinmay Dattanand Kuchinad, Priyanka Holla Bhadravati Girish
- December 6th, 2023
- v1.0
- Convolutional Neural Network(CNN)
- Training algorithms and features:
  * Custom-built CNN for ASL recognition
  * Utilized hand landmarks extracted using MediaPipe library
  * Training on an ASL dataset comprising 87,000 images across 29 classes
- https://www.researchgate.net/publication/353486480_Convolutional_Neural_Network_Hand_Gesture_Recognition_for_American_Sign_Language
- S. Chavan, X. Yu and J. Saniie, "\textbf{Convolutional Neural Network Hand Gesture Recognition for American Sign Language}," 2021 IEEE International Conference on Electro Information Technology (EIT)


## Intended use

### Primary intended uses
To detect and interpret sign language for enhancing accessibility for deaf and hard-of-hearing individuals.

### Primary intended users
Researchers, Developers in assistive technologies, Educational institutions.

### Out-of-scope use cases
Not designed for real-time communication in noisy or visually complex environments.

## Factors

### Relevant factors
Performance may vary with lighting conditions, hand sizes, and skin tones.

### Evaluation factors
Accuracy in diverse real-world conditions.

## Metrics

### Model performance measures
Training set accuracy (97.17%), Validation set accuracy (98.13%).


## Evaluation data

### Datasets
American Sign Language dataset with 87,000 images.

### Motivation
To cover a wide range of hand signs in ASL.

### Preprocessing
Resizing, augmentations (Random Horizontal Flip, Random Rotation, Colour Jitter)

## Training data

The training data comprised 87,000 images, evenly distributed across 29 distinct ASL sign classes.

## Quantitative analyses

### Unitary results
High accuracy in detecting individual signs.


## Ethical considerations

### Data
The dataset might not represent all variations of hand signs equally.

### Human life
Enhances communication for deaf and hard-of-hearing individuals.

### Mitigations
Future versions could include more diverse datasets.

### Risks and harms
Limited by the 2D nature of the training data, potentially affecting real-time performance.

### Use cases
Intended for educational and assistive technology use.

## Caveats and recommendations

### Further Development
Consider implementing 3D CNN and leveraging video data for improved real-time performance.

### Limitations
Current model may not perform optimally in real-time due to training on 2D images.

## Code

### Description

Python code using PyTorch for model training and evaluation.

### Github Repo

https://github.com/chinmaydk99/ee541_final_project_group_24


