import streamlit as st
from Common_Utility.LLM import GroqLLM
from Graph.builder import GraphBuilder
from UI.load_ui import LoadStreamlitUI
from UI.display_results import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the SDLC AgenticAI application using Streamlit UI.
    Handles user input, configures the LLM, sets up the graph, and displays output.
    """

    # Load UI to capture user input
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    # Capture user message input
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Configure LLM
            llm_config = GroqLLM(user_controls_input=user_input)
            model = llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return

            # Initialize GraphBuilder and create graph based on selected SDLC phase
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("Error: No use case selected.")
                return

            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                # Display Results on UI
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return

        except Exception as e:
            st.error(f"Error Occurred: {e}")

# MAIN EXECUTION
if __name__ == "__main__":
    st.title("💡 SDLC Agent")
    load_langgraph_agenticai_app()
