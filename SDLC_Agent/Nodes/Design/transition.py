
from SDLC_Agent.Common_Utility.LLM import LLM
from SDLC_Agent.Common_Utility.state import SDLCState

class CreateDesignDocs :
    """
    Transition to create design documents based on user stories.

    Args:
        state (SDLCState): The current state of the SDLC process.

    Updates:
        state.design_docs (str): Generated design document.
    """
    def execute(self, state: SDLCState):
        prompt = f"Create a design document based on the following user stories:\n{state.user_stories}\n\nDesign Document:"
        state.design_docs = LLM.get_llm_model(prompt)

class ReviewDesignDocs:
    """
    Transition to review and refine design documents based on feedback.

    Args:
        state (SDLCState): The current state of the SDLC process.

    Updates:
        state.design_docs (str): Updated design document.
    """
    def execute(self, state: SDLCState):
        if state.design_feedback.strip():
            prompt = f"Review the design document based on the following feedback:\n{state.design_feedback}\n\nUpdated Design Document:"
            state.design_docs = LLM.get_llm_model(prompt)
