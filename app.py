import streamlit as st
from groq import Groq

# عنوان الصفحة بتصميم أنيق
st.set_page_config(page_title="الشات بوت الخاص بي", page_icon="💬")
st.title("💬 الشات بوت الخاص بي")

# الاتصال بـ Groq API باستخدام مفتاحك
client = Groq(api_key="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")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثات السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال الرسالة من المستخدم
if prompt := st.chat_input("اكتب رسالتك هنا..."):
    # حفظ وعرض رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # الحصول على رد الذكاء الاصطناعي وعرضه
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    
    # حفظ رد الذكاء الاصطناعي في السجل
    st.session_state.messages.append({"role": "assistant", "content": full_response})