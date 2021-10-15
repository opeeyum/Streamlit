import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import matplotlib.pyplot as plt

st.title("Image Processing and Streamlit")

image = Image.open("Capture.PNG") 

def main():
    page = st.sidebar.selectbox(
        "Pages",
        ["Home Page", "Rotation",
        "Thumbnail", "Crop Image",
        "Merge Images", "Filters",
        ]
    )
    if page == "Home Page":
        homepage()
    
    elif page == "Rotation":
        option = st.selectbox("",
        ["Rotate", "Flip"])

        if option == "Rotate":
            rotate_image()
        else:
            flip_image()
    
    elif page == "Thumbnail":
        thumbnail()

    elif page == "Crop Image":
        crop_image()
    
    elif page == "Merge Images":
        merge_images()
    
    elif page == "Filters":
        option = st.selectbox("Select Filter",
        ["Black and White", "Contour", "Emboss", "Edge Enhance", "Contrast"])

        if option == "Black and White":
            blackAndWhite()
        
        elif option == "Contour":
            contour()

        elif option == "Emboss":
            emboss()

        elif option == "Edge Enhance":
            edge_enhance()
        
        else:
            contrast()


def homepage():    
    fig = plt.figure()
    plt.imshow(image)
    plt.axis("off")
    st.pyplot(fig)

def rotate_image():
    #Number of degree's
    rotated_img = image.rotate(180) 
    fig = plt.figure()
    plt.imshow(rotated_img)
    plt.axis("off")
    st.pyplot(fig)

def flip_image():
    fig = plt.figure()
    #First Image
    image_one = image.transpose(Image.FLIP_LEFT_RIGHT)
    plt.subplot(1, 2, 1)
    plt.imshow(image_one)
    #Second Image
    image_two = image.transpose(Image.FLIP_TOP_BOTTOM)
    plt.subplot(1, 2, 2)
    plt.imshow(image_two)
    st.pyplot(fig)

def thumbnail():
    #Heigth and width
    size = (100, 100)
    image.thumbnail(size)
    fig = plt.figure()
    plt.imshow(image)
    plt.axis("off")
    st.pyplot(fig)

def crop_image():
    #Coordinates
    left = 100
    top = 150
    right = 500
    bottom = 400 
    img = image.crop((left, top, right, bottom))
    fig = plt.figure()
    plt.imshow(img)
    plt.axis("off")
    st.pyplot(fig)

def merge_images():
    #First Image
    image_one = Image.open("Capture.PNG") 
    #Second Image
    image_two = Image.open("github.PNG")
    Image.Image.paste(image_one, image_two, (400, 100))
    fig = plt.figure()
    plt.imshow(image_one)
    plt.axis("off")
    st.pyplot(fig)

def blackAndWhite():
    fig = plt.figure()
    img = image.convert("1")
    plt.imshow(img)
    st.pyplot(fig)

def contour():
    fig = plt.figure()
    con = image.filter(ImageFilter.CONTOUR)
    plt.imshow(con)
    st.pyplot(fig)

def emboss():
    fig = plt.figure()
    emb = image.filter(ImageFilter.EMBOSS)
    plt.imshow(emb)
    st.pyplot(fig)

def edge_enhance():
    fig = plt.figure()
    enh = image.filter(ImageFilter.EDGE_ENHANCE)
    plt.imshow(enh)
    st.pyplot(fig)

def contrast():
    fig = plt.figure()
    contrast = ImageEnhance.Contrast(image).enhance(12)
    plt.imshow(contrast)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
