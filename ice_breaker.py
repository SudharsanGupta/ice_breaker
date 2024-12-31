from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

from agents.linkedin_lookup_agent import lookup
from third_parties.linkedIn import scrape_linkedin_profile


def ice_breaker_with(name: str):
    linkedin_url = lookup(name=name)
    profile = scrape_linkedin_profile(linkedin_url)

    summary_template = """ 
      Given the {information} about a person, I want to create:
      1. A short summary
      2. Two interesting facts about them 
      """

    template = PromptTemplate(input_variables=['information'], template=summary_template)

    # Initialize the Gemini model. Make sure to set GOOGLE_API_KEY in your .env file
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=os.getenv("GOOGLE_API_KEY"))
    # llm = ChatOllama(model="llama3.2")

    chain = template | llm
    res = chain.invoke(input={"information": profile})

    print(res.content)


if __name__ == '__main__':
    print('Hello Ice breaker langchain with Gemini!!')
    load_dotenv()
    ice_breaker_with(name="Eden Marco")
    # summary_template = """
    # Given the {information} about a person, I want to create:
    # 1. A short summary
    # 2. Two interesting facts about them
    # """
    #
    # template = PromptTemplate(input_variables=['information'], template=summary_template)
    #
    # # Initialize the Gemini model. Make sure to set GOOGLE_API_KEY in your .env file
    # llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=os.getenv("GOOGLE_API_KEY"))
    # # llm = ChatOllama(model="llama3.2")
    #
    # chain = template | llm
    #
    # information = "Elon Musk is a South African-born American entrepreneur and business magnate. He is the founder, CEO, and Chief Engineer of SpaceX; early-stage investor, CEO, and Product Architect of Tesla, Inc.; founder of The Boring Company; and co-founder of Neuralink and OpenAI."  # Example information
    # res = chain.invoke(input={"information": information})
    #
    # print(res.content)