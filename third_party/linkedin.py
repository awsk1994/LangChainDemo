import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from Linkedin profiles,
    Manually scrape the ifnromation from the Linkedin profile
    """
    # TODO: actually call proxycurl to get LinkedIn data from online

    url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    response = requests.get(url)

    if response.status_code == 200:  # check if the request was successful
        data = response.json()
        data = {
            k:v
            for k,v in data.items()
            if v not in ([], "", "", None)
                and k not in ["people_also_viewed", "certifications"] 
        }
        if data.get("groups"):
            for group_dict in data.get("groups"):
                    group_dict.pop("profile_pic_url")
        return data
    else:
        print("Error fetching data")
        return None
