import os
from datetime import datetime
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

notion = Client(
    auth=os.getenv("NOTION_TOKEN")
)


def get_text(prop):

    try:
        if prop["rich_text"]:
            return prop["rich_text"][0]["plain_text"]
    except:
        pass

    return ""


def safe_text(value):

    if value is None:
        return ""

    if isinstance(value, list):
        return ", ".join(
            str(x) for x in value
        )

    return str(value)


def update_company(page_id, data):

    page = notion.pages.retrieve(
        page_id=page_id
    )

    props = page["properties"]

    current_role = get_text(
        props["Role"]
    )

    current_location = get_text(
        props["Location"]
    )

    current_eligibility = get_text(
        props["Eligibilty"]
    )

    current_ctc = get_text(
        props["CTC"]
    )

    current_internship = get_text(
        props["Internship"]
    )

    current_summary = get_text(
        props["Summary"]
    )

    current_note = get_text(
        props["Note"]
    )

    current_deadline = get_text(
        props["DeadLine"]
    )

    current_stage = get_text(
        props["Stage"]
    )

    mail_count = props[
        "Mail Count"
    ]["number"]

    if mail_count is None:
        mail_count = 0

    mail_count += 1

    summary_text = safe_text(
        data.get("summary")
    )

    stage_text = safe_text(
        data.get("stage")
    )

    note_entry = (
        f"\n\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}]\n"
        f"Stage: {stage_text}\n"
        f"{summary_text}"
    )

    updated_note = (
        current_note + note_entry
    )

    notion.pages.update(

        page_id=page_id,

        properties={

            "Role": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                safe_text(
                                    data.get("role")
                                )
                                or current_role
                        }
                    }
                ]
            },

            "Internship": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                safe_text(
                                    data.get(
                                        "internship"
                                    )
                                )
                                or current_internship
                        }
                    }
                ]
            },

            "CTC": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                safe_text(
                                    data.get("ctc")
                                )
                                or current_ctc
                        }
                    }
                ]
            },

            "Location": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                safe_text(
                                    data.get(
                                        "location"
                                    )
                                )
                                or current_location
                        }
                    }
                ]
            },

            "DeadLine": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                safe_text(
                                    data.get(
                                        "deadline"
                                    )
                                )
                                or current_deadline
                        }
                    }
                ]
            },

            "Eligibilty": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                safe_text(
                                    data.get(
                                        "eligibility"
                                    )
                                )
                                or current_eligibility
                        }
                    }
                ]
            },

            "Summary": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                summary_text[:1900]
                                or current_summary
                        }
                    }
                ]
            },

            "Stage": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                stage_text
                                or current_stage
                        }
                    }
                ]
            },

            "Latest Updat": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                stage_text
                        }
                    }
                ]
            },

            "Apply Link": {
                "url":
                    data.get(
                        "apply_link"
                    )
                    or props[
                        "Apply Link"
                    ]["url"]
            },

            "Note": {
                "rich_text": [
                    {
                        "text": {
                            "content":
                                updated_note[:1900]
                        }
                    }
                ]
            },

            "Mail Count": {
                "number": mail_count
            },

            "Mail received": {
                "date": {
                    "start":
                        datetime.now().isoformat()
                }
            }
        }
    )

    print(
        f"Company updated | Mail Count = {mail_count}"
    )