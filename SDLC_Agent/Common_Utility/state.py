from pydantic import BaseModel, Field
from typing import List

class SDLCState(BaseModel):
    """
    Represents the state for the entire SDLC process using Pydantic BaseModel.
    """
    requirement: str = Field(default="", description="Requirements for the project.")
    feedback: str = Field(default="", description="User feedback for refining user stories.")
    user_stories: List[str] = Field(default_factory=list, description="List of generated user stories.")
    design_specification: str = Field(default="", description="Generated design specification.")
    code: str = Field(default="", description="Generated code.")
    test_results: str = Field(default="", description="Results from testing.")
    deployment_status: str = Field(default="", description="Deployment status.")

