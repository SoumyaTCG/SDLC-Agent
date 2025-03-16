from SDLC_Agent.Common_Utility.LLM import LLM
from SDLC_Agent.Common_Utility.state import SDLCState




class GenerateUserStories:
    """
    Transition to generate user stories based on the requirement.

    Args:
        state (SDLCState): The current state of the SDLC process.

    Updates:
        state.user_stories (list): Generated user stories.
    """
    def execute(self, state: SDLCState):
        if state.requirement.strip():
            prompt = f"Generate user stories based on the following requirement:\n{state.requirement}\n\nUser Stories:"
            state.user_stories = LLM.get_llm_model(prompt).split("\n")

class RefineUserStories:
    """
    Transition to refine user stories based on user feedback.

    Args:
        state (SDLCState): The current state of the SDLC process.

    Updates:
        state.user_stories (list): Refined user stories.
    """
    def execute(self, state: SDLCState):
        if state.user_story_feedback.strip():
            prompt = f"Refine user stories based on feedback:\n{state.user_story_feedback}\n\nRefined User Stories:"
            state.user_stories = LLM.get_llm_model(prompt).split("\n")
