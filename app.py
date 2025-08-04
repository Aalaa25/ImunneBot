import streamlit as st
from RAG_Immune_system import answer_question
from collections import deque

# Initialize conversation memory
conversation_memory = deque(maxlen=7)

# Custom CSS for centered title and responsive design
st.markdown("""
<style>
    /* Centered title container */
    .centered {
        text-align: center;
        margin-bottom: 1.5rem;
    }
    
    /* Title style */
    .title {
        color: #1a237e;
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    /* Subtitle style */
    .subtitle {
        color: #455a64;
        font-size: 1.1rem;
    }
    
    /* Chat messages */
    .stChatMessage {
        border-radius: 12px;
        padding: 12px 16px;
        margin: 8px 0;
        max-width: 80%;
    }
    
    /* User messages */
    [data-testid="stChatMessage"][aria-label="user"] {
        background-color: #e3f2fd;
        margin-left: auto;
    }
    
    /* Assistant messages */
    [data-testid="stChatMessage"][aria-label="assistant"] {
        background-color: #ffffff;
        margin-right: auto;
    }
</style>
""", unsafe_allow_html=True)

# Centered title and subtitle
st.markdown("""
<div class="centered">
    <h1 class="title">🧬 ImmuneBot</h1>
    <p class="subtitle">Ask me about immune system and autoimmune diseases!</p>
</div>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Your question"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    response = answer_question(prompt)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)