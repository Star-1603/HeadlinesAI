import streamlit as st
import os
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
# function to load Gemini Pro model
model = genai.GenerativeModel('gemini-pro')

def main():
    # page configuration
    st.set_page_config(page_title="Headline Generator", layout="wide")
    # formatting for the header
    st.title("Headlines AI")
    # sidebar formatting
    st.sidebar.subheader("Platform and Content Type")
    platform_options = {
        "YouTube": ["Video Ideas", "Titles", "Descriptions", "Hashtags", "CTAs"],
        "Instagram": ["Photo Ideas", "Captions", "Hashtags", "CTAs"],
        "Blogger": ["Article Ideas", "Titles", "Body Content", "CTAs"],
        "Reddit": ["Post Ideas", "Titles", "Post Content", "CTAs"],
        "Blog": ["Blog Post Ideas", "Titles", "Post Content", "CTAs"]
    }
    selected_platform = st.sidebar.selectbox("Select platform:", list(platform_options.keys()))
    selected_option = st.sidebar.radio("What do you want to generate?", platform_options[selected_platform])

    # get input
    st.subheader("Describe your prompt:")
    content = selected_option.lower()
    prompt = st.text_input("Enter your prompt:")

    st.subheader(f"Generated {selected_option.title()} Content:")

    if st.button("Generate Ideas ༼ つ ◕_◕ ༽つ"):
        try:
         
            # Generate the content using the model (placeholder for actual model call)
            response = model.generate_content(f"Generate a {content} based on the following prompt: {prompt}")

            # Extract the generated text (assuming response.text is the output format)
            generated_text = response.text

            if response.parts:
                    titles = [part.text.strip() for part in response.parts]
                    for i, title in enumerate(titles, start=1):
                        st.write(f"{i}. {title}")
            else:
                st.write("No content generated.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
main()
