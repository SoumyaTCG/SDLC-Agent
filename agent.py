import streamlit as st
from Common_Utility.LLM import GroqLLM
from Graph.builder import GraphBuilder
from UI.display_results import DisplayResultStreamlit

def initialize_ui():
    """Initializes the Streamlit UI components."""
    st.title("SDLC Agent")
    groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    selected_groq_model = st.selectbox("Select Groq Model:", ["gemma2-9b-it"])
    user_requirement = st.text_area("Enter software requirement:", height=200)  # Removed file upload
    return groq_api_key, selected_groq_model, user_requirement

def configure_llm(groq_api_key, selected_groq_model):
    """Configures the LLM model."""
    try:
        obj_llm_config = GroqLLM({
            "GROQ_API_KEY": groq_api_key,
            "selected_groq_model": selected_groq_model
        })
        return obj_llm_config.get_llm_model()
    except Exception as e:
        st.error(f"Error: Failed to configure LLM - {e}")
        return None

def build_and_display_graph(model, user_requirement):
    """Builds the SDLC graph and displays results."""
    try:
        graph_builder = GraphBuilder(model, user_requirement)  # Pass user input directly
        graph = graph_builder.build_sdlc_graph()
        DisplayResultStreamlit(graph, user_requirement).display_result_on_ui()
    except Exception as e:
        st.error(f"Error: Graph setup or display failed - {e}")

def load_sdlc_agent():
    """Runs the SDLC Agent Streamlit app."""
    groq_api_key, selected_groq_model, user_requirement = initialize_ui()

    if not groq_api_key.strip():
        st.warning("Groq API Key is required.")
        return

    if not user_requirement.strip():
        st.warning("Software requirement cannot be empty.")
        return

    model = configure_llm(groq_api_key, selected_groq_model)
    if not model:
        return

    build_and_display_graph(model, user_requirement)

if __name__ == "__main__":
    load_sdlc_agent()
