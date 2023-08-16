# Dog and Cat Image Classification with Streamlit

This repository contains code and resources for intel image classification project using Streamlit. The project includes a notebook for experimentation, trained model for classification, and a Streamlit app for interactive visualization.
I have downloaded the data on [Kaggle.com](https://www.kaggle.com/).


You can get the trained model [here](https://drive.google.com/file/d/10TJ6VN_e22rMI6jc9asWGBvGxNd3bW13/view?usp=drive_link)
## Project Structure

The repository is organized as follows:

- `notebook`: This directory contains the Jupyter notebook where the initial data exploration, preprocessing, and model experimentation were carried out.
- `app.py`: This file contains the Streamlit code for the interactive web application. Users can upload images of dogs and cats to the app and get real-time predictions using the trained models.
- `model`: I've used the [https://tfhub.dev/google/imagenet/resnet_v1_101/classification/5](resnet_v1) pre-trained model and I've reached an accuracy close tp 90%.
- `requirements.txt`: This file contains all packages that need to be installed for the app to work.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/sniperezbuckets/intel_image_classification_with_streamlit

2. Navigate to the repository's directory:

   ```bash
   cd intel_image_classification_with_streamlit
   
3. Install the required dependencies. It's recommended to create a virtual environment before installing the dependencies:

   ```bash
   pip install -r requirements.txt

4. Run the Streamlit app:

    ```bash
    streamlit run app.py

