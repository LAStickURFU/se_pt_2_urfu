from transformers import pipeline
import streamlit as st


def shorten_text(original_text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    short_text = summarizer(original_text, max_length=8192, min_length=14, do_sample=False)
    return short_text


# Создаем интерфейс с помощью Streamlit
st.title("Text summarization")
input_text = st.text_area("Original text")
if st.button("Summarize"):
    # Показываем спиннер во время обработки данных
    with st.spinner("Text summarization..."):
        short_text = shorten_text(original_text=input_text)
        # Очищаем спиннер и выводим результат
        st.success("Done!")
        st.text_area("Summary text", short_text[0]['summary_text'])
