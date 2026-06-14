import os
from datetime import datetime
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

notion = Client(auth=NOTION_TOKEN)


def safe_text(value):

    if value is None:
        return ""

    if isinstance(value, list):
        return ", ".join(str(x) for x in value)

    return str(value)


def create_company(data):

    company = safe_text(
        data.get("company")
    ) or "Unknown"

    role = safe_text(
        data.get("role")
    )

    internship = safe_text(
        data.get("internship")
    )

    ctc = safe_text(
        data.get("ctc")
    )

    location = safe_text(
        data.get("location")
    )

    deadline = safe_text(
        data.get("deadline")
    )

    eligibility = safe_text(
        data.get("eligibility")
    )

    category = safe_text(
        data.get("category")
    )

    stage = safe_text(
        data.get("stage")
    )

    summary = safe_text(
        data.get("summary")
    )

    apply_link = data.get(
        "apply_link"
    ) or ""

    response = notion.pages.create(

        parent={
            "database_id": DATABASE_ID
        },

        properties={

            "title": {
                "title": [
                    {
                        "text": {
                            "content": company
                        }
                    }
                ]
            },

            "Company name": {
                "rich_text": [
                    {
                        "text": {
                            "content": company
                        }
                    }
                ]
            },

            "Role": {
                "rich_text": [
                    {
                        "text": {
                            "content": role
                        }
                    }
                ]
            },

            "Internship": {
                "rich_text": [
                    {
                        "text": {
                            "content": internship
                        }
                    }
                ]
            },

            "CTC": {
                "rich_text": [
                    {
                        "text": {
                            "content": ctc
                        }
                    }
                ]
            },

            "Location": {
                "rich_text": [
                    {
                        "text": {
                            "content": location
                        }
                    }
                ]
            },

            "DeadLine": {
                "rich_text": [
                    {
                        "text": {
                            "content": deadline
                        }
                    }
                ]
            },

            "Eligibilty": {
                "rich_text": [
                    {
                        "text": {
                            "content": eligibility
                        }
                    }
                ]
            },

            "Category": {
                "multi_select": [
                    {
                        "name": category
                    }
                ] if category else []
            },

            "Stage": {
                "rich_text": [
                    {
                        "text": {
                            "content": stage
                        }
                    }
                ]
            },

            "Latest Updat": {
                "rich_text": [
                    {
                        "text": {
                            "content": stage
                        }
                    }
                ]
            },

            "Summary": {
                "rich_text": [
                    {
                        "text": {
                            "content": summary[:1900]
                        }
                    }
                ]
            },

            "Note": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}]\n{summary}"
                        }
                    }
                ]
            },

            "Mail Count": {
                "number": 1
            },

            "Status": {
                "multi_select": [
                    {
                        "name": "New"
                    }
                ]
            },

            "Apply Link": {
                "url": apply_link if apply_link else None
            },

            "Mail received": {
                "date": {
                    "start": datetime.now().isoformat()
                }
            }
        }
    )

    print(
        f"Created company: {company}"
    )

    return response