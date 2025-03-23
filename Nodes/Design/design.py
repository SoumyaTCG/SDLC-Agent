from Common_Utility.LLM import GroqLLM
from Common_Utility.state import SDLCState

class DesignSpecificationGenerator:
    """
    Class to handle design specification generation using an LLM.
    """

    def __init__(self, llm):
        """
        Initializes the DesignSpecificationGenerator.

        Args:
            llm: An instance of the existing LLM module.
        """
        self.llm = llm

    def generate_design_specification(self, state: SDLCState) -> SDLCState:
        """
        Generates a design specification based on user stories and requirements.
        """
        print("--GENERATE DESIGN SPECIFICATION--")
        prompt = f"""Generate a detailed design specification based on these user stories and requirements:\nUser Stories: {state.user_stories}\nRequirements: {state.requirement}.Based on the above, generate a comprehensive design specification that includes:

        * **System Architecture:** High-level overview of the system's components and their interactions.
        * **Data Model:** Description of the data entities, attributes, and relationships.
        * **User Interface:** Wireframes or mockups of the user interface.
        * **API Design:** Specification of the APIs used for communication between components.
        * **Security Considerations:** Measures to ensure data security and privacy.
        * **Performance Requirements:** Expected response times and system throughput.

        Please provide a well-structured and detailed design specification to guide the development process."""  
        response = self.llm.invoke(prompt)
        print(response.content)
        state.design_specification = response.content
        return state

    def refine_design_specification(self, state: SDLCState) -> SDLCState:
        """
        Refines the design specification based on the feedback provided.
        """
        print("--REFINE DESIGN SPECIFICATION--")
        prompt = f"""
        You are a software development expert, tasked with refining design specifications.
        Here's the current design specification:{state.design_specification}.Here is the feedback received:{state.feedback}
        """
        response = self.llm.invoke(prompt)
        print(response.content)
        state.design_specification = response.content
        return state