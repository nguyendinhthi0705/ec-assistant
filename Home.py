import streamlit as st
import sys
sys.path.append("./image_background")
sys.path.append("./image_extension")
sys.path.append("./image_insertion")
sys.path.append("./image_masking")
sys.path.append("./image_prompts")
sys.path.append("./image_replacement")
sys.path.append("./image_search")
sys.path.append("./image_to_image")
sys.path.append("./image_understanding")
sys.path.append("./image_variation")


from image_background_app import image_background 
from image_extension_app import image_extension 
from image_insertion_app import image_insertion 
from image_masking_app import image_masking 
from image_prompts_app import image_prompts 
from image_replacement_app import image_replacement 
from image_search_app import image_search 
from image_to_image_app import image_to_image 
from image_understanding_app import image_understanding 
from image_variation_app import image_variation 


st.set_page_config(layout="wide", page_title="Image Background")

st.sidebar.success("Select a a tool below.")

page_names_to_funcs = {
    "Remove Background": image_background,
    "Image Extension": image_extension,
    "Image Insertion": image_insertion,
    "Image Masking": image_masking,
    "Image Prompts": image_prompts,
    "Image Replacement": image_replacement,
    "Image Search": image_search,
    "Image To Image": image_to_image,
    "Image Understanding": image_understanding,
    "Image Variation": image_variation,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()