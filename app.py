from utils import (
    get_image,
    get_product_description,
    get_client,
)
import json
import streamlit as st
st.set_page_config(page_title="Automatic product caption generator", layout="wide")


@st.cache_resource
def get_cached_client():
    return get_client()


client = get_cached_client()
prompt = """
You're a fashion content writer. Given this product image, write 3 short e-coomerce like product descriptions 
tailored the following audiences: gen-z, millenials, SEO-optimized. 
Use a tone and language that resonates with them. 
Be creative, engaging, and highlight the product's appeal.

Please respond in JSON format like:
{"gen_z": "...",
 "millennials": "...",
 "seo_optimized": "..."}

Respond with only the JSON. Do not include explanations or extra text.
"""



image_url = st.text_input("Enter image URL:")
image_pil = False
image_valid = False
if image_url:
    image_pil = get_image(image_url)
    if image_pil is not None:
        image_valid = True
    else:
        st.warning("Invalid link or error loading image.")

if (image_valid) and (image_pil):
    with st.spinner("Generating product descriptions..."):
        response = get_product_description(prompt, image_pil, client)
        try:
            captions = json.loads(response.parsed[0].model_dump_json())
        except Exception as e:
            st.error(f"Error parsing model response: {e}")
            st.stop()

col1, col2 = st.columns(2)

if image_valid and image_pil:
    with col1:
        st.image(image_pil, caption="Input Image", use_container_width=True)
    with col2:
        st.subheader("Generated descriptions")
        st.markdown(f"**SEO Optimized**: {captions['seo_optimized']}")
        st.markdown("---")
        st.markdown(f"**Millennials**: {captions['millennials']}")
        st.markdown("---")
        st.markdown(f"**Gen-Z**: {captions['gen_z']}")
