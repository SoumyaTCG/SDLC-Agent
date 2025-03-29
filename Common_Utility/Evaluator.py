from Common_Utility.state import SDLCState
from Common_Utility.LLM import GroqLLM

class FeedbackEvaluator:
    """
    Evaluates user feedback and determines the next step in the workflow.
    """

    def __init__(self, llm: GroqLLM):
        """
        Initializes the FeedbackEvaluator with the LLM model.

        Args:
            llm (GroqLLM): The language model used for processing feedback.
        """
        self.llm = llm


    def evaluate(self, state: SDLCState, current_phase: str,user_feedback:str) -> str:
        """
        Evaluates feedback for the current phase and determines whether to proceed or refine.

        Args:
            state (SDLCState): The shared state object.
            current_phase (str): The current phase of the SDLC process.

        Returns:
            str: "Good" or "Bad" based on the evaluation.
        """

        # Define prompt for AI evaluation
        prompt = f"""
        You are an AI assistant evaluating feedback on a software development lifecycle (SDLC) phase.

        **Phase:** {current_phase}  
        **Feedback Received:** "{user_feedback}"  

        #### **Guidelines:**
        - If the feedback suggests improvement, missing details, or refinement, classify as `"Bad"`.  
        - If the feedback is neutral, unclear, or positive, classify as `"Good"`.  
        - Respond **ONLY** with `"Good"` or `"Bad"`, nothing else.

        Answer:
        """

        try:
            # Call LLM for evaluation
            response = self.llm.invoke(prompt).content.strip()

            # Ensure response is valid
            response = "Good" if response not in {"Good", "Bad"} else response

            # Store evaluation in state
            state.evaluation[current_phase] = response
            print(f"Evaluation for '{current_phase}': {response}")

            return response

        except Exception as e:
            # Handle errors and default to "Good" for smooth flow
            state.evaluation[current_phase] = "Good"
            print(f"Error during feedback evaluation: {e}")
            return "Good"
