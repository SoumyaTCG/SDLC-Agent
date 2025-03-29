import streamlit as st
from Common_Utility.LLM import GroqLLM
from Common_Utility.state import SDLCState
from Graph.builder import GraphBuilder
from UI.load_ui import LoadStreamlitUI
from UI.display_results import DisplayResultStreamlit

# Initialize session state variables
if "IsFetchButtonClicked" not in st.session_state:
    st.session_state["IsFetchButtonClicked"] = False

# Streamlit Page Configuration
st.set_page_config(
    page_title="💡 SDLC Agent",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS Styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(145deg, #141e30, #243b55);
            color: #ffffff;
            font-family: 'Inter', sans-serif;
        }
        .stTextInput, .stTextArea {
            border-radius: 14px;
            padding: 14px;
            background: rgba(255, 255, 255, 0.08);
            box-shadow: inset 6px 6px 12px rgba(0, 0, 0, 0.3), inset -6px -6px 12px rgba(255, 255, 255, 0.1);
            color: #ffffff;
        }
        .stButton button {
            background: linear-gradient(145deg, #1f77b4, #2a9df4);
            color: #ffffff;
            padding: 14px 32px;
            border-radius: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: linear-gradient(145deg, #2a9df4, #1f77b4);
            transform: translateY(-3px);
        }
        .result-box {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 16px;
            box-shadow: 6px 6px 20px rgba(0, 0, 0, 0.4), -6px -6px 20px rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)



def load_langgraph_agenticai_app():
    """
    Load and run the LangGraph AgenticAI application with Streamlit UI.
    Handles user input, configures LLM, builds a graph, and displays results.
    """
    st.markdown("<h1 style='text-align: center;'>🚀 SDLC Agent</h1>", unsafe_allow_html=True)
    
    # Sidebar Configuration
    st.sidebar.markdown("## ⚙️ Configuration")
    
    # Load UI Components
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    
    if not user_input:
        st.sidebar.error("⚠️ Failed to load user input from the UI.")
        return
    
    # User Input Box
    st.markdown("### 💬 Your Input:")
    user_message = st.text_area(
        "Enter your requirement:",
        height=150,
        placeholder="Describe the requirement, ask for suggestions...",
        key="user_message"
    )
    
    # Generate Button
    if st.button("🚀 Generate", key="generate_button"):
        st.session_state["IsFetchButtonClicked"] = True
    
    if user_message:
        try:
            st.markdown("### 🧠 Configuring LLM...")
            llm_config = GroqLLM(user_controls_input=user_input)
            model = llm_config.get_llm_model()
            
            if not model:
                st.error("❌ LLM model could not be initialized.")
                return
            
            st.markdown("### 🌐 Setting up Graph...")
            graph_builder = GraphBuilder(model, user_message)
            graph = graph_builder.build_sdlc_graph()
            
            if not graph:
                st.error("❌ Failed to generate SDLC Graph.")
                return
            
            
            # Display Results
            st.markdown("### 📈 **Results:**")
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            DisplayResultStreamlit(graph, user_message).display_result_on_ui()
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Run Application
if __name__ == "__main__":
    load_langgraph_agenticai_app()
