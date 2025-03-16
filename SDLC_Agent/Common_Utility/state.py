from langggraph import State

class SDLCState(State):
    # Requirement Gathering Phase
    requirement: str = ""
    feedback: str = ""
    
    # User Story Phase
    user_stories: list = []
    user_story_feedback: str = ""
    
    # Design Phase
    design_docs: str = ""
    design_feedback: str = ""
    
    # Development Phase
    code: str = ""
    code_feedback: str = ""
    
    # Testing Phase
    test_cases: list = []
    test_results: list = []
    test_feedback: str = ""
    
    # Deployment Phase
    deployment_status: str = ""
    deployment_feedback: str = ""
    
    # Maintenance Phase
    maintenance_logs: list = []
    maintenance_feedback: str = ""
