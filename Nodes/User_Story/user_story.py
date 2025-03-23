from Common_Utility.state import SDLCState


class UserStoryGenerator:
    """
    Class to handle user story generation and refinement using an LLM.
    """

    def __init__(self, llm):
        """
        Initializes the UserStoryGenerator.

        Args:
            llm: An instance of the existing LLM module.
        """
        self.llm = llm

    def generate_user_stories(self, state: SDLCState) -> SDLCState:
        """
        Generates a user story based on the requirement in the data.
        """
        print("--GENERATE USER STORY--") 
        prompt = f"Generate a single detailed user story for the following requirement: {state.requirement} and that also also without any additional explanations or parts to it."
        
        response = self.llm.invoke(prompt)
        print(response.content)  
        state.user_stories = response.content  
        
        return state
    
    def refine_user_story(self, state: SDLCState) -> SDLCState:
        """
        Refines the user story based on the feedback provided.
        """
        print("--REFINE USER STORY--")
        prompt = f"""
        You are a software development expert, tasked with refining user stories.
        Here's the current user story:{state.user_stories}.Here is the feedback received:{state.feedback}
        """
        response = self.llm.invoke(prompt)
        print(response.content)
        state.user_stories = response.content
        return state
