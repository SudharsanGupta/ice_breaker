import os

import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """ scrapes LinkedIn profile,
    Manually scrapes the information from LinkedIn profile"""
    if mock:
        linkedin_profile_url = 'https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json'
        response = requests.get(linkedin_profile_url, timeout=5)
    else:
        request_end_url = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers = {'Authorization': 'Bearer ' + os.getenv('PROXYCURL_API_KEY')}
        response = requests.get(request_end_url, params= { "url": linkedin_profile_url}, headers=headers, timeout=5)

    data = response.json()
    return data


if __name__ == '__main__':
    print(scrape_linkedin_profile(linkedin_profile_url="www.linkedin.com/in/sudharsan-kakaraparthy"))