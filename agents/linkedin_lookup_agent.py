import os
from pydoc import describe

from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.tools import get_profile_url_tavily


def lookup(name: str):
    # llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=os.getenv("GOOGLE_API_KEY"))
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0.5, openai_api_key=os.getenv("OPENAI_API_KEY"))

    template = ("Given the full name {name_of_person} I want you to get me link to their linkedin profile,"
                "your answer should contain only the linkedin url")
    prompt_template = PromptTemplate(input_variables=['name_of_person'], template=template)

    tools_for_agents = [Tool(
        name="Crawl Google 4 linkedin profile",
        func=get_profile_url_tavily,
        description="useful when you need to get the linkedin url",
    )]
    react_prompt = hub.pull("hwchase17/react")
    react_agent = create_react_agent(llm=llm, tools=tools_for_agents, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=react_agent, tools=tools_for_agents, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name), })
    response = result["output"]
    return response

if __name__ == "__main__":
    linkedin_url = lookup(name="Eden Marco")
    print(linkedin_url)
