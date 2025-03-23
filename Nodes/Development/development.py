from Common_Utility.LLM import GroqLLM
from Common_Utility.state import SDLCState

class CodeGenerator:
    """
    Class to handle code generation using an LLM.
    """

    def __init__(self, llm):
        """
        Initializes the CodeGenerator.

        Args:
            llm: An instance of the existing LLM module.
        """
        self.llm = llm

    def generate_code(self, state: SDLCState) -> SDLCState:
        """
        Generates code based on the design specification and requirements.
        """
        print("--GENERATE CODE--")

        prompt = f"""Generate high-quality, production-ready code based on the following details:
        
        **Design Specification:**  
        {state.design_specification}
        
        **Requirements:**  
        {state.requirement}

        The generated code should adhere to best practices, be modular, well-documented, and optimized for performance. 
        Ensure it includes necessary error handling, security considerations, and follows coding standards relevant to the technology stack inferred from the specification.
        """

        response = self.llm.invoke(prompt)
        state.code = response.content
        return state