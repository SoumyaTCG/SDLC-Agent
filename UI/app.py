import streamlit as st
from Common_Utility.LLM import GroqLLM
from Graph.builder import GraphBuilder
from UI.load_ui import LoadStreamlitUI
from UI.display_results import DisplayResultStreamlit

# Initialize session state variables if not set
if "IsFetchButtonClicked" not in st.session_state:
    st.session_state["IsFetchButtonClicked"] = False

# Set dark theme and custom styling
st.set_page_config(
    page_title="💡 SDLC Agent",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for Glassmorphism and modern styling
st.markdown("""
    <style>
        /* Background gradient and font setup */
        body {
            background: linear-gradient(145deg, #141e30, #243b55);
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        /* Input Fields and Select Box */
        .stTextInput, .stSelectbox, .stTextArea {
            border-radius: 14px;
            padding: 14px;
            background: rgba(255, 255, 255, 0.08);
            box-shadow: inset 6px 6px 12px rgba(0, 0, 0, 0.3), inset -6px -6px 12px rgba(255, 255, 255, 0.1);
            border: none;
            color: #ffffff;
            transition: all 0.3s ease;
            font-size: 16px;
        }

        /* Focus effect on inputs */
        .stTextInput:focus, .stSelectbox:focus, .stTextArea:focus {
            outline: none;
            background: rgba(255, 255, 255, 0.15);
            box-shadow: 0 0 16px rgba(31, 119, 180, 0.6);
        }

        /* Button Styling */
        .stButton button {
            background: linear-gradient(145deg, #1f77b4, #2a9df4);
            color: #ffffff;
            border: none;
            padding: 14px 32px;
            border-radius: 16px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.4), -4px -4px 12px rgba(255, 255, 255, 0.1);
            letter-spacing: 0.5px;
        }

        /* Button Hover Effect */
        .stButton button:hover {
            background: linear-gradient(145deg, #2a9df4, #1f77b4);
            transform: translateY(-3px);
            box-shadow: 6px 6px 16px rgba(0, 0, 0, 0.5), -6px -6px 16px rgba(255, 255, 255, 0.2);
        }

        /* Result Box Styling */
        .result-box {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 16px;
            box-shadow: 6px 6px 20px rgba(0, 0, 0, 0.4), -6px -6px 20px rgba(255, 255, 255, 0.1);
            border: none;
            color: #ffffff;
            margin-top: 16px;
            transition: all 0.3s ease;
        }

        /* Result Box Hover Effect */
        .result-box:hover {
            transform: translateY(-5px);
            box-shadow: 8px 8px 24px rgba(0, 0, 0, 0.5), -8px -8px 24px rgba(255, 255, 255, 0.2);
        }

        /* Divider Styling */
        .divider {
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            margin-top: 20px;
            margin-bottom: 20px;
        }

        /* Header Styling */
        h1, h2, h3, h4, h5 {
            color: #ffffff;
            font-weight: 700;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
        }

        /* Hover Scaling Effect */
        .hover-effect {
            transition: transform 0.3s ease;
        }

        .hover-effect:hover {
            transform: scale(1.03);
            filter: brightness(1.1);
        }

        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #1c1c1c;
        }

        ::-webkit-scrollbar-thumb {
            background: #2a9df4;
            border-radius: 12px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #1f77b4;
        }
    </style>
""", unsafe_allow_html=True)

def load_langgraph_agenticai_app():
    st.markdown("<h1 style='text-align: center;'>🚀 SDLC Agent</h1>", unsafe_allow_html=True)

    # Sidebar for Configurations
    st.sidebar.markdown("## ⚙️ Configuration")

    # Load UI components from LoadStreamlitUI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.sidebar.error("⚠️ Failed to load user input from the UI.")
        return

    # Divider for separation
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # User input box
    st.markdown("### 💬 Your Input:")
    user_message = st.text_area(
        "Enter your input:",
        height=150,
        placeholder="Describe the requirement, ask for suggestions...",
        key="user_message"
    )

    # ✅ Centered Button for Better UX
    st.markdown("<div style='display: flex; justify-content: center; margin-top: 20px;'>", unsafe_allow_html=True)
    if st.button("🚀 Generate", key="generate_button"):
        st.session_state["IsFetchButtonClicked"] = True
    st.markdown("</div>", unsafe_allow_html=True)

    if user_message:
        try:
            st.markdown("### 🧠 Configuring LLM...")
            llm_config = GroqLLM(user_controls_input=user_input)
            model = llm_config.get_llm_model()

            if not model:
                st.error("❌ LLM model could not be initialized.")
                return

            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("❌ No SDLC phase selected.")
                return

            st.markdown("### 🌐 Setting up Graph...")
            graph_builder = GraphBuilder(model)
            graph = graph_builder.setup_graph(usecase)

            # Display Results inside a stylish box
            st.markdown("### 📈 **Results:**")
            st.markdown('<div class="result-box hover-effect">', unsafe_allow_html=True)
            DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {e}")

# MAIN EXECUTION
if __name__ == "__main__":
    load_langgraph_agenticai_app()
