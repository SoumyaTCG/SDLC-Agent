import streamlit as st
from Common_Utility.LLM import GroqLLM
from Graph.builder import GraphBuilder
from UI.display_results import DisplayResultStreamlit

def initialize_ui():
    """
    Initializes the Streamlit UI components.
    
    Returns:
        tuple: Groq API key, selected model, and uploaded file.
    """
    st.title("SDLC Agent")
    groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    selected_groq_model = st.selectbox("Select Groq Model:", ["mixtral-8x7b", "llama3-8b", "llama3-70b"])
    uploaded_file = st.file_uploader("Upload your SDLC file:", type=["txt", "md", "json", "py", "java", "yaml"])
    return groq_api_key, selected_groq_model, uploaded_file

def configure_llm(groq_api_key, selected_groq_model):
    """
    Configures the LLM model using the provided API key and model selection.
    
    Args:
        groq_api_key (str): The API key for Groq.
        selected_groq_model (str): The selected Groq model.
    
    Returns:
        object: The initialized LLM model or None if initialization fails.
    """
    try:
        obj_llm_config = GroqLLM({
            "GROQ_API_KEY": groq_api_key,
            "selected_groq_model": selected_groq_model
        })
        return obj_llm_config.get_llm_model()
    except Exception as e:
        st.error(f"Error: Failed to configure LLM - {e}")
        return None

def process_uploaded_file(uploaded_file):
    """
    Processes the uploaded file and returns its content.
    
    Args:
        uploaded_file: The uploaded file object.
    
    Returns:
        str: The content of the uploaded file.
    """
    try:
        return uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error(f"Error: Failed to read uploaded file - {e}")
        return None

def build_and_display_graph(model, file_content):
    """
    Builds the SDLC graph and displays the results on the UI.
    
    Args:
        model: The LLM model.
        file_content (str): The content of the uploaded file.
    """
    try:
        graph_builder = GraphBuilder(model)
        graph = graph_builder.setup_graph("Requirement Gathering")  # Example use case
        DisplayResultStreamlit(graph, file_content).display_result_on_ui()
    except Exception as e:
        st.error(f"Error: Graph setup or display failed - {e}")

def load_sdlc_agent():
    """
    Loads and runs the SDLC Agent application with Streamlit UI.
    """
    groq_api_key, selected_groq_model, uploaded_file = initialize_ui()

    if not groq_api_key or not selected_groq_model:
        st.warning("Please enter the Groq API key and select a model.")
        return

    if uploaded_file:
        file_content = process_uploaded_file(uploaded_file)
        if not file_content:
            return

        model = configure_llm(groq_api_key, selected_groq_model)
        if not model:
            return

        build_and_display_graph(model, file_content)

if __name__ == "__main__":
    load_sdlc_agent()