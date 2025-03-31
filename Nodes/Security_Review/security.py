from Common_Utility.LLM import GroqLLM
from Common_Utility.state import SDLCState


class SecurityReviewHandler:
    """
    Handles the security review and refinement of generated code.
    """

    def __init__(self, llm):
        """
        Initializes the SecurityReviewHandler.

        Args:
            llm: An instance of the existing LLM module.
        """
        self.llm = llm

    def perform_security_review(self, state: SDLCState) -> SDLCState:
        """
        Conducts a security review on the generated code.
        """
        print("--PERFORM SECURITY REVIEW--")
        prompt = f"""
        You are a security expert analyzing the following code for vulnerabilities:
        Code:\n{state.code}

        Provide a detailed security assessment, including:
        - **Potential security vulnerabilities** (e.g., SQL injection, XSS, hardcoded credentials).
        - **Mitigation strategies** to resolve the issues.
        - **Security rating**: High Risk, Medium Risk, Low Risk, Secure.
        """
        response = self.llm.invoke(prompt)
        print(response.content)
        state.security_review = response.content
        return state

    def refine_code_based_on_security_review(self, state: SDLCState) -> SDLCState:
        """
        Refines the generated code based on security review feedback.
        """
        print("--REFINE CODE BASED ON SECURITY REVIEW--")
        prompt = f"""
        You are a security-focused software engineer.

        The current code has the following vulnerabilities:
        {state.security_review}

        Please modify the code to resolve the issues while maintaining its original functionality.
        Ensure:
        - Secure input validation
        - Proper authentication & authorization
        - No hardcoded secrets
        - Mitigation of all identified risks

        Here is the original code:
        {state.code}
        """
        response = self.llm.invoke(prompt)
        print(response.content)
        state.code = response.content  # Update with secure code

        return state
