from typing import Optional, Dict
from importlib import metadata
from toml import load


class Util:
    """A collection of utility functions for PyMap."""
    
    @staticmethod
    def get_project_metadata() -> Optional[Dict[str, str]]:
        """Returns the metadata of the project."""
        
        try:
            with open("pyproject.toml", "r") as file:
                return metadata.metadata(load(file)["tool"]["poetry"]["name"]).json
        except Exception:
            return None

    @staticmethod
    def get_project_name() -> Optional[str]:
        """Returns the name of the project."""
        
        metadata = Util.get_project_metadata()
        return metadata["name"] if metadata else None

    @staticmethod
    def get_project_version() -> Optional[str]:
        """Returns the version of the project."""
        
        metadata = Util.get_project_metadata()
        return metadata["version"] if metadata else None
