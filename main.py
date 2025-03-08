from googletrans import Translator
import streamlit as st

st.title("Language Translator")

# Dictionary of language codes and their names
LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "es": "Spanish",
    "fr": "French",
    "de": "German", 
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "ur": "Urdu"
}

user_input = st.text_input("Enter Text To Translate:")

if user_input:
    try:
        translator = Translator()
        
        # Detect input language
        detect_language = translator.detect(user_input).lang
        st.info(f"Detected Language: {LANGUAGES.get(detect_language, detect_language)}")
        
        # Language selection with friendly names
        target_language = st.selectbox(
            'Select Target Language',
            options=list(LANGUAGES.keys()),
            format_func=lambda x: LANGUAGES[x]
        )

        # Translate text
        translated_text = translator.translate(
            user_input,
            src=detect_language,
            dest=target_language
        )
        
        # Display translation
        st.success("Translation:")
        st.write(translated_text.text)
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please enter text to translate")

# with open('language.txt', 'a', encoding='utf-8') as f:
#     f.write('\n')
#     f.write(user_input)
#     f.write('\n')
#     f.write(translated_text)