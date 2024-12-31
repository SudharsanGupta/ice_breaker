from langchain_community.tools import TavilySearchResults


def get_profile_url_tavily(name:str):
    """Search for Linkedin profile page"""
    search = TavilySearchResults()
    res = search.run(f'{name}')
    return res
    