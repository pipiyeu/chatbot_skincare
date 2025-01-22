import random
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Simulasi model dan tokenizer
# (Gantilah bagian ini dengan model dan tokenizer yang sudah kamu buat)
class DummyTokenizer:
    def texts_to_sequences(self, texts):
        return [[1, 2, 3]]  # Contoh sequence palsu

    def pad_sequences(self, sequences, maxlen):
        return np.zeros((1, maxlen))

tokenizer = DummyTokenizer()
input_shape = 10  # Sesuaikan dengan panjang input model
responses = {
    "greeting": ["Halo! Ada yang bisa Fifi bantu? 😊", "Hai! Ceritakan kebutuhanmu."],
    "goodbye": ["Sampai jumpa lagi! ✨", "Bye! Jangan lupa jaga kesehatan!"],
}

# Placeholder untuk prediksi (simulasi)
def predict_tag(input_text):
    tags = ["greeting", "goodbye"]
    return random.choice(tags)

# Streamlit UI
st.title("Fifi - Your Skincare Chatbot 🤖💖")
st.write("Selamat datang! Fifi siap membantu menjawab pertanyaanmu tentang skincare.")

# Chatbox
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ketik pesanmu di sini...", placeholder="Contoh: Apa rekomendasi produk untuk kulit kering?")
if st.button("Kirim") and user_input:
    # Proses input pengguna
    texts_p = ''.join([char.lower() for char in user_input if char.isalnum() or char.isspace()])
    texts_p = tokenizer.texts_to_sequences([texts_p])
    prediction_input = np.array(texts_p).reshape(-1)
    prediction_input = pad_sequences([prediction_input], input_shape)

    # Prediksi respons chatbot
    predicted_tag = predict_tag(user_input)
    bot_response = random.choice(responses[predicted_tag])

    # Tambahkan ke riwayat chat
    st.session_state.chat_history.append(("Kamu", user_input))
    st.session_state.chat_history.append(("AskFifi", bot_response))

# Tampilkan riwayat percakapan
for sender, message in st.session_state.chat_history:
    if sender == "Kamu":
        st.markdown(f"**👤 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
