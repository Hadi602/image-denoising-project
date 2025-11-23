# image-denoising-project
Denoising images using Median and Mean filters with Python
# Image Denoising Project Using Mean and Median Filters

# Project Overview
This project applies basic image-processing techniques to denoise three images (143.jpeg, 184.jpeg, and 250.jpeg). The objective is to remove noise while preserving the essential structural features of each image. Python and Google Colab were used for implementation.

## Methodology

### 1. Noise Identification
Histograms were generated for each image to analyze noise characteristics:
- Salt-and-pepper noise shows extreme intensity spikes.
- Gaussian noise exhibits a bell-shaped intensity distribution.

### 2. Denoising Methods
- **Median Filter**  
  Applied to *143.jpeg* and *184.jpeg* to remove salt-and-pepper noise.  
  This filter effectively eliminates impulse noise while maintaining edge sharpness.

 **Mean Filter**  
  Applied to *250.jpeg* to reduce Gaussian noise.  
  This filter smooths intensity variations consistent with Gaussian distributions.

---

## Experimental Results

### Image 1: 143.jpeg
- **Noise Type:** Salt-and-pepper  
- **Denoising Method:** Median Filter  
- **Outcome:** Noise effectively reduced with preserved edges.

### Image 2: 184.jpeg
- **Noise Type:** Salt-and-pepper  
- **Denoising Method:** Median Filter  
- **Outcome:** Significant reduction of impulse noise and retention of fine structures.

### Image 3: 250.jpeg
- **Noise Type:** Gaussian  
- **Denoising Method:** Mean Filter  
- **Outcome:** Smoother intensity distribution aligned with Gaussian denoising behavior.

---

## Tools and Libraries
- Python  
- Google Colab  
- OpenCV  
- NumPy  
- Matplotlib  

---

## Learning Outcomes
This project strengthened core skills in:
- Noise detection through histogram analysis  
- Application of Median and Mean filters  
- Python-based image-processing workflows  
- Research-oriented experimentation and documentation  

---

## How to Run
1. Open the notebook in Google Colab.  
2. Upload the three images into the runtime environment.  
3. Execute the cells step-by-step to visualize noise removal results.  

---

## Repository Structure

## Author
Muhammad Rashid 
