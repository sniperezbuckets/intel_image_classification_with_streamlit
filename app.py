import streamlit as st
import PIL
from PIL import Image
import validators
import requests
from io import BytesIO
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np


info = """
1. Upload an image an image from your computer or enter an image link.
2. Click on the `predict` button.
3. Wait for the prediction to happen.
4. Reapeat the process if needed.
"""

warning = """
To avoid inacurate results, you **MUST** only provide image from the following categories:
* forest
* building
* glacier
* street
* mountain
* see
"""


def resize_and_display_img(img, shape=(800, 400)):
    return st.image(img.resize(shape))


def preprocess_img(img):
    img = tf.constant(img)
    img = tf.image.resize(img, size=[224, 224])
    img = img/255.

    return tf.expand_dims(img, axis=0)


@st.cache_resource
def load_model():
    custom_object = {'KerasLayer': hub.KerasLayer}
    model = tf.keras.models.load_model(
        'model/resnet_v1.h5', custom_objects=custom_object)
    return model


def predict(img):
    classnames = ['buildings', 'forest',
                  'glacier', 'mountain', 'sea', 'street']
    resnet_v1 = load_model()
    pred_probs = resnet_v1.predict(img)
    pred = classnames[tf.argmax(pred_probs, axis=1).numpy()[0]]
    return pred, format(np.max(pred_probs, axis=1)[0], '.2f')


def upload_img(upload_type):
    if upload_type == 'Image':
        img = st.file_uploader('Upload an image', type=[
            'png', 'jpg', 'jpeg', 'webp'])
        if img:
            img = Image.open(img)
            resize_and_display_img(img=img)
            return img

    if upload_type == 'Url':
        url = st.text_input('Enter url')

        if url and not validators.url(url):
            st.error('Not a valid url, please enter a valid one')

        elif url and validators.url(url):
            response = requests.get(url)
            try:
                img = Image.open(BytesIO(response.content))
                resize_and_display_img(img=img)
                return img
            except PIL.UnidentifiedImageError:
                st.error(
                    'Ooooops, an unexpected error occured, please try again or use a different url')


def main():
    st.title('Intel Image Classification')
    wallpaper = Image.open('images/wallpaper.jpeg')
    st.subheader(
        'Classify **sea**, **forest**, **building**, **street**, **glacier**, **mountain** images.')
    st.image(wallpaper)

    with st.expander('How it works ?'):
        st.info(info)
        st.warning(warning)

    st.markdown('---')

    upload_choice = st.radio('Upload options', options=['Image', 'Url'])

    img = upload_img(upload_type=upload_choice)

    if img:
        prep_img = preprocess_img(img=img)
        if st.button('Predict'):
            preds = predict(prep_img)
            classname = preds[0]
            confidence = preds[1]

            st.success(
                f'I see a **{classname}** with a confidence of **{confidence}**%.')


if __name__ == '__main__':
    main()
