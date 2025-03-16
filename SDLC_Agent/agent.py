import streamlit as st
from SDLC_Agent.Common_Utility.LLM import GroqLLM
from SDLC_Agent.Graph.builder import GraphBuilder
from SDLC_Agent.UI.display_result import DisplayResultStreamlit

# MAIN Function START
def load_sdlc_agent():
    """
    Loads and runs the SDLC Agent application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected SDLC phase, and displays the output 
    while implementing exception handling for robustness.
    """

    st.title("SDLC Agent")

    # User Input Section
    groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    selected_groq_model = st.selectbox("Select Groq Model:", ["mixtral-8x7b", "llama3-8b", "llama3-70b"])
    selected_usecase = st.selectbox(
        "Select SDLC Phase:",
        ["Requirement Gathering", "Design", "Development", "Testing", "Deployment", "Maintenance"]
    )

    if not groq_api_key or not selected_groq_model:
        st.warning("Please enter the Groq API key and select a model.")
        return

    # Text input for user message
    user_message = st.chat_input("Enter your input:")

    if user_message:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM({
                "GROQ_API_KEY": groq_api_key,
                "selected_groq_model": selected_groq_model
            })
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return

            # Initialize and set up the graph based on use case
            if not selected_usecase:
                st.error("Error: No SDLC phase selected.")
                return

            # Build Graph
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(selected_usecase)
                DisplayResultStreamlit(selected_usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return

        except Exception as e:
            st.error(f"An error occurred: {e}")
