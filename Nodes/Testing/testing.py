from Common_Utility.LLM import GroqLLM
from Common_Utility.state import SDLCState

class GenerateTestCases:
    """
    Handles test case generation and refinement using the LLM.
    """

    def __init__(self, llm):
        """
        Initializes the GenerateTestCases class.

        Args:
            llm: An instance of the existing LLM module.
        """
        self.llm = llm

    def generate_test_cases(self, state: SDLCState) -> SDLCState:
        """
        Generates initial test cases based on the generated code.

        Args:
            state (SDLCState): The current state of the SDLC process.

        Returns:
            SDLCState: The updated SDLCState with the generated test cases.
        """
        print("--GENERATE TEST CASES--")

        prompt = f"""Generate a comprehensive set of test cases, including:
        
        - Unit Tests covering individual functions and methods
        - Integration Tests ensuring components interact correctly
        - Security Tests checking for vulnerabilities
        
        Ensure the tests follow best practices, use a structured framework, and include assertions.
        
        Code for Testing:  
        {state.code}
        """

        response = self.llm.invoke(prompt)
        print(response.content)
        state.test_cases = response.content
        return state

    def refine_test_cases(self, state: SDLCState) -> SDLCState:
        """
        Refines the generated test cases for better coverage, efficiency, and best practices.

        Args:
            state (SDLCState): The current state of the SDLC process.

        Returns:
            SDLCState: The updated SDLCState with refined test cases.
        """
        print("--REFINING TEST CASES--")

        refine_prompt = f"""Improve the following test cases by:
        
        - Enhancing coverage for edge cases and boundary conditions
        - Ensuring clear, well-structured assertions
        - Avoiding redundant or unnecessary tests
        - Optimizing test execution time
        
        Current Test Cases:  
        {state.test_cases}
        """

        response = self.llm.invoke(refine_prompt)
        state.refined_test_cases = response.content
        return state
