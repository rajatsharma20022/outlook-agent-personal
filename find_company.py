import os
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
DATA_SOURCE_ID = os.getenv("DATA_SOURCE_ID")


def normalize(text):

    return (
        str(text)
        .lower()
        .strip()
        .replace(" ", "")
    )


def find_company(company_name):

    target = normalize(company_name)

    response = notion.data_sources.query(
        data_source_id=DATA_SOURCE_ID
    )

    for page in response["results"]:

        try:

            company = page["properties"]["Company name"]["rich_text"]

            if not company:
                continue

            company_text = company[0]["plain_text"]

            if normalize(company_text) == target:
                return page["id"]

        except Exception:
            pass

    return None