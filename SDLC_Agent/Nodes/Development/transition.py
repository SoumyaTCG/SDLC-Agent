
from SDLC_Agent.Common_Utility.LLM import LLM
from SDLC_Agent.Common_Utility.state import SDLCState

class WriteCode:
    """
    Transition to generate code based on the design document.

    Args:
        state (SDLCState): The current state of the SDLC process.

    Updates:
        state.code (str): Generated code.
    """
    def execute(self, state: SDLCState):
        prompt = f"Write code based on the following design document:\n{state.design_docs}\n\nGenerated Code:"
        state.code = LLM.get_llm_model(prompt)

class CodeReview:
    """
    Transition to review and refine code based on feedback.

    Args:
        state (SDLCState): The current state of the SDLC process.

    Updates:
        state.code (str): Updated code after review.
    """
    def execute(self, state: SDLCState):
        if state.code_feedback.strip():
            prompt = f"Review the code based on the following feedback:\n{state.code_feedback}\n\nUpdated Code:"
            state.code = LLM.get_llm_model(prompt)
