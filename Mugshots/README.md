
<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/mugfakes_title1.jpg" width="800">  
<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/mug_grid.jpg" width="800">  
*^Curated images from my final run with StyleGAN.*  

*^^The image on the portfolio main page was compiled from a mosiac of real mugshots*  


# Overview
  
***This is an ongoing project***  
  
The purpose of this project was to first find a novel data source and then work to generate realistic fake mugshots folowwing some of the major advancments in Generative Adversarial Networks (GAN) over the past few years. I first needed to find real mugshot images online. There are some websites where you can purchase access to mugshots but I wanted to gather the images myself to have more control over the quality and type.

## Data
All images were sourced from two county websites. One for Maricopa County in Arizona and the other for Osceola County in Florida. I created webscrapers to gather inmate details and download mughsots, on a daily basis. I considered gathering images from more than two sources but ended up staying with the two. The image quality is similar but I did initially get better results from the images from Florida.

## Image Processing

# Attempts

## First Run
With my first attempt at generating mugshots, I went with a relatively simple approach to first understand the architecture of a Generator (**G**) and Discriminator (**D**). I used PyTorch to match the original design in the introductory paper that described the novel approach. I did not achieve great results in this first run and came to a point at about 700 epochs where the gradients between the **D** and **G** continually diverged.

**Details:**  
* Image size: 64x64
* Batch size: 64
* Learning Rate: 0.0002
* Epochs: 1,000
* Method: DGAN  

<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/fake_samples_epoch_0999.png" width="800">

## Second Run


**Details:**  
* Image size: 64
* Batch size: 128
* Learning Rate: **D**=0.0001 **G**=0.001
* Iterations: 1,000
* Method: DGAN  

<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/fake_samples_epoch_1190.png" width="800">

## Third Run


**Details:**  
* Image size: Varies  
* Batch size: Varies  
* Learning Rate: .001
* Iterations: 427,000
* Method: StyleGAN  

<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/427100.png" width="800">


## Fourth Run


**Details:**  
* Image size: Varies  
* Batch size: Varies  
* Learning Rate: .001
* Iterations: 362,000
* Method: StyleGAN  

<img src="https://github.com/csmangum/portfolio/blob/master/Mugshots/img/256_362100.png" width="800">
