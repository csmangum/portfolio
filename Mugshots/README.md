<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/mugfakes_title1.jpg" width="900">
<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/grid_3x2.jpg" width="900">
^Curated images from my final run with StyleGAN

# Overview

### Project Goal
Use Generative Adversarial Networks (GAN) to generate realistic images trained on thousands of actual mugshots.

## Approach
* Create novel image dataset through [web scraping](https://github.com/csmangum/portfolio/blob/master/Mugshots/get_mugshots.ipynb)
* Experiment with the GAN architecture
  * First following the [original](https://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf) framework
  * Then use an awesome PyTorch [implementation](https://github.com/rosinality/style-based-gan-pytorch) of NVIDIA's Tensorflow example ([StyleGAN](https://github.com/NVlabs/stylegan))  

## Data
All images were sourced from two county websites. One for [Maricopa County](https://www.mcso.org/Mugshot) in Arizona and the other for [Osceola County](https://apps.osceola.org/Apps/CorrectionsReports/Report/Daily/) in Florida. I created a webscraper to gather inmate details and download mughsots daily. I considered gathering images from more than two sources but ended up staying with the two. The image quality is similar, but I did initially get better results from the images from Florida.

### Image Processing
I initially performed little image processing but did add a few steps as I experimented more and more. Here are the steps I took to prepare the images for training:

* Filter out images where the face covered more than 50% of the image
* Center cropped on the face
* Resized the image (StyleGAN eventually resized at multiple pixel values)
* Manually deleted images that were:
  * Out-of-focus
  * Defective images (looking down, etc.)
  * Individuals with facemasks (Due to COVID-19 period)
  * Individuals with glasses (on final run)
  
## Learnings
1. I can get decent results from very few mugshots
2. Batch size matters
3. Close-up portraits are more difficult to train
4. It gets to a point where many faces are incredibly similar

# Experimentation
## 1. First Run
With my first attempt at generating mugshots, I went with a relatively simple approach to first understand the architecture of a Generator (**G**) and Discriminator (**D**). I did not achieve great results in this first run and came to a point at about 700 epochs where the gradients between the **D** and **G** continually diverged.  

**Details:**  
* Image size: 32x32
* Image count: 708
* Iterations: 1,000
* Method: DGAN  

<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/fake_samples_epoch_0999.png" width="800">

## 2. Second Run
In this attempt I used only images from the Florida subset since the image quality seemed more uniform and focused. Even after 1,000 iterations the model hit its limit at this resolution. This was the moment I decided to use the StyleGAN approach for more detailed images.

**Details:**  
* Image size: 64x64
* Image count: 703
* Iterations: 1,200
* Method: DGAN  

<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/fake_samples_epoch_1190.png" width="800">

## 3. Third Run
Using only the mugshots from Florida, I ran for more than 400,000 iterations with the StyleGAN architecture getting decent results. There was still some anomalies and a lot of the faces still didn't look realistic. In my next approach I will use mugshots from both state agencies.

**Details:**  
* Image size: 128x128
* Image count: 1,073
* Iterations: 427,000
* Method: StyleGAN  

<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/427100.png" width="800">


## 4. Fourth Run
I augmented my training set by mirroring every image and was able to get the best results yet. The training time did take a couple weeks on a GTX 970 secondary machine I used solely for training. I also started to update the training script to fit my needs to better evaluate training performance.

**Details:**  
* Image size: 256x256
* Image count: 1,309 (2,618 when mirrored)
* Iterations: 362,000
* Method: StyleGAN  

<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/256_362100.png" width="800">  

# Final Attempt

* Image size: 512x512
* Image count: 5,000
* Iterations: 
* Method: StyleGAN  

# Future
1. Train on larger set of mugshots
2. Experiment with SyleGAN2
3. Create a webapp to manipulate image based on "styles" (i.e. beard, age, etc.)

# Additional Analysis

* [Sex - Classification](https://github.com/csmangum/portfolio/blob/master/Mugshots/Gender_Classification.ipynb)  
  * Using Convolutional Neural Networks (CNN) in Keras
  * Achieved reasonable success with a ROC-AUC of 0.96
  * Performed poorly when using non-mugshot images (ROC-AUC: 0.61)
* [Age - Regression](https://github.com/csmangum/portfolio/blob/master/Mugshots/Age_Keras_Regression.ipynb)
  * CNNs in Keras to predict age
  * RMSE on validation at 11.7 years
* [Age - Classification](https://github.com/csmangum/portfolio/blob/master/Mugshots/Age_Keras_Classification.ipynb)
  * CNNs in Keras to predict age
  * Binned ages into 4 buckets
  * Achieved mediocre success with a ROC-AUC ranging from 0.63 to 0.76
  
  # Acknowledgments
  A lot of great resources that helped me get a grasp and better understand GANs and the continually changing landscape. Specific thanks to:
  * [NVIDIA](https://github.com/NVlabs/stylegan)  
  * [rosinality](https://github.com/rosinality/style-based-gan-pytorch)  
  * [sentdex](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ)  
  * [Machine Learning Mastery](https://machinelearningmastery.com/introduction-to-style-generative-adversarial-network-stylegan/)  
