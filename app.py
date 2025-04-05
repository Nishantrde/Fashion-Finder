import streamlit as st
import requests

# cmd 
# pip install streamlit
# streamlit run cloths_ai.py


# example images
# https://tirupurbrands.com/wp-content/uploads/2021/06/Plain-T-Shirt-Exporters-Tirupur_PRNBIO-min.jpg?
# https://m.media-amazon.com/images/I/71mXiVfHgrL._AC_UY1100_.jpg


st.title("Google Lens Thumbnail Viewer")

# Input field for the image URL
input_url = st.text_input("Enter an image URL:")

if st.button("Search"):
    if input_url:
        api_key = "67da3f559597ea633a563a0e"
        endpoint = "https://api.scrapingdog.com/google_lens"
        params = {
            "api_key": api_key,
            "url": input_url,
            "country": "in"
        }
        
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            data = response.json()
            lens_results = data.get("lens_results", [])
            if lens_results:
                st.subheader("Top 5 Thumbnails")
                # Loop through the first five results
                for i, result in enumerate(lens_results[:5]):
                    thumbnail_url = result.get("thumbnail")
                    link_url = result.get("link")
                    if thumbnail_url and link_url:
                        # Create a clickable image using HTML in markdown.
                        # Clicking the image will open the link in a new tab.
                        st.markdown(
                            f'<a href="{link_url}" target="_blank">'
                            f'<img src="{thumbnail_url}" alt="Thumbnail {i+1}" style="width:200px; margin: 10px;"></a>',
                            unsafe_allow_html=True
                        )
                    else:
                        st.write(f"Result {i+1} does not have a valid thumbnail or link.")
            else:
                st.warning("No lens results found in the API response.")
        else:
            st.error(f"Request failed with status code: {response.status_code}")
    else:
        st.warning("Please enter a valid image URL.")
