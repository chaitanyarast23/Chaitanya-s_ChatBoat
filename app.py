import streamlit as st
from src.chat_engine import ask, mock_interview

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Chaitanya AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------
# SIDEBAR
# -----------------------------------
with st.sidebar:

    st.title("👨‍💻 Chaitanya Rastogi")

    try:
        st.image("assets/profile.jpeg", width=220)
    except:
        pass

    st.markdown("---")

    mode = st.selectbox(
        "Select Mode",
        [
            "Career Assistant",
            "Mock Interview"
        ]
    )

    # Mode Change Detection
    if "previous_mode" not in st.session_state:
        st.session_state.previous_mode = mode

    if st.session_state.previous_mode != mode:

        st.session_state.messages = []

        st.session_state.previous_mode = mode

        st.rerun()

    st.markdown("---")

    if mode == "Career Assistant":

        st.markdown("""
### 🤖 Career Assistant

Ask me about:

- Skills
- Projects
- Experience
- Education
- Certifications
- Technologies
- Career Journey
""")

    else:

        st.markdown("""
### 🎯 Mock Interview Mode

Practice interviews for:

- Python
- SQL
- Data Science
- Machine Learning
- Generative AI

Type:

**start interview**

to begin.
""")

    st.markdown("---")

    st.markdown("### 🔗 Connect With Me")

    st.markdown(
        "[💼 LinkedIn](https://www.linkedin.com/in/rastogichaitanya)"
    )

    st.markdown(
        "[💻 GitHub](https://github.com/chaitanyarast23)"
    )

    st.markdown(
        "[📧 Email](mailto:chaitanyarastogi23@gmail.com)"
    )

    st.markdown("---")

    try:

        with open(
            "assets/resume.pdf",
            "rb"
        ) as file:

            st.download_button(
                label="📄 Download Resume",
                data=file,
                file_name="Chaitanya_Rastogi_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    except FileNotFoundError:

        st.info(
            "Add assets/resume.pdf to enable resume download."
        )

# -----------------------------------
# HEADER
# -----------------------------------
header_col1, header_col2 = st.columns([8, 1])

with header_col1:

    if mode == "Career Assistant":

        st.title("🤖 Chaitanya AI Career Assistant")

    else:

        st.title("🎯 Chaitanya AI Mock Interview")

with header_col2:

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

st.markdown("---")



# -----------------------------------
# INITIAL WELCOME MESSAGE
# -----------------------------------
if (
    "messages" not in st.session_state
    or len(st.session_state.messages) == 0
):

    if mode == "Career Assistant":

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """
# 👋 Welcome

I'm **Chaitanya AI Career Assistant**.

How can I help you today?


"""
            }
        ]

    else:

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """
# 🎯 Mock Interview Mode

Welcome!

I can conduct interviews on:

- Python
- SQL
- Data Science
- Machine Learning
- Generative AI

Type:

**start interview**

to begin your interview.
"""
            }
        ]


# -----------------------------------
# DISPLAY CHAT HISTORY
# -----------------------------------
for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# -----------------------------------
# CHAT INPUT
# -----------------------------------
user_input = st.chat_input(
    "Type your message here..."
)

# -----------------------------------
# PROCESS USER INPUT
# -----------------------------------
if user_input:

    # Display User Message
    with st.chat_message("user"):

        st.markdown(user_input)

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Assistant Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            if mode == "Career Assistant":

                answer = ask(user_input)

            else:

                answer = mock_interview(
                    user_input
                )

            st.markdown(answer)

    # Save Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )