import streamlit as st
from deep_translator import GoogleTranslator, MyMemoryTranslator

# Application title
st.title("🌍 Language Translation Tool")
st.write("Translate text between English, Tamil, and Sinhala.")

# Language codes for Google
languages = {
    "English": "en",
    "Tamil": "ta",
    "Sinhala": "si"
}

# Language codes for MyMemory (region-style)
mymemory_codes = {
    "English": "en-US",
    "Tamil": "ta-IN",
    "Sinhala": "si-LK"
}

# Language selection
source_language = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_language = st.selectbox(
    "Select Target Language",
    list(languages.keys()),
    index=1
)

# Text input
input_text = st.text_area(
    "Enter Text to Translate",
    placeholder="Type your text here..."
)

# Translate button
if st.button("Translate", type="primary"):

    if input_text.strip() == "":
        st.warning("Please enter some text.")

    elif source_language == target_language:
        st.warning("Please select different languages.")

    else:
        translated_text = None

        # Try Google first
        try:
            translated_text = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            ).translate(input_text)

        except Exception:
            # Google failed or is blocked, use MyMemory as backup
            try:
                translated_text = MyMemoryTranslator(
                    source=mymemory_codes[source_language],
                    target=mymemory_codes[target_language]
                ).translate(input_text)

            except Exception as e:
                st.error("Translation failed. Please check your internet connection.")
                st.write("Error details:", e)

        if translated_text:
            st.success("Translation Completed!")
            st.subheader("Translated Text")

            # Display translated text with copy button
            st.code(translated_text, language=None)