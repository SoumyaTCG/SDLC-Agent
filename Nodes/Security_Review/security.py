from Common_Utility.LLM import GroqLLM

class SecurityReview:
    """
    Handles security analysis and enhancement of the generated code using the LLM.
    """
    def __init__(self, llm):
        self.llm = llm

    def analyze_security(self, code):
        """
        Analyzes the security of the given code and identifies potential vulnerabilities.

        Args:
            code (str): The generated code.

        Returns:
            str: Security analysis report.
        """
        prompt = (
            "Perform a security analysis of the following code. Identify vulnerabilities, "
            "potential security risks, and suggest mitigations. Ensure best security practices are followed.\n\n"
            f"Code:\n{code}\n\n"
            "Provide a structured security report:"
        )
        security_report = self.llm.call_llm(prompt)
        return security_report.strip() if security_report else "No security risks detected."


        return secure_code.strip() if secure_code else code
