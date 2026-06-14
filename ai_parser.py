import os
import json
import time
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_placement_info(email_text):

    prompt = f"""
Extract placement information from this email.

Return ONLY valid JSON.

Fields:

company
role
internship
ctc
location
deadline
eligibility
category
stage
summary
apply_link

IMPORTANT RULES:

1. If internship stipend is present:
   internship = stipend amount

Example:
Internship Stipend: ₹70,000 per month

Return:
"internship": "₹70,000 per month"

2. If full-time package is present:
   ctc = full-time package

Example:
Full-Time Conversion Package: ₹10 LPA

Return:
"ctc": "₹10 LPA"

3. NEVER return:
"internship": "Yes"

4. NEVER combine stipend and CTC into one field.

BAD:

"internship": "Yes"
"ctc": "Internship Stipend ₹70,000/month, Full-Time Package ₹10 LPA"

GOOD:

"internship": "₹70,000 per month"
"ctc": "₹10 LPA"

Stage must be one of:

Registration Open
Reminder
OA Scheduled
OA Completed
OA Cleared
Interview Scheduled
HR Round
Selected
Offer Released
Rejected
Closed

Examples:

"This is a reminder regarding..."
=> Reminder

"Online Assessment scheduled..."
=> OA Scheduled

"Interview scheduled..."
=> Interview Scheduled

"Congratulations..."
=> Selected

"Offer letter released..."
=> Offer Released

Return format:

{{
  "company": "",
  "role": "",
  "internship": "",
  "ctc": "",
  "location": "",
  "deadline": "",
  "eligibility": "",
  "category": "",
  "stage": "",
  "summary": "",
  "apply_link": ""
}}

Email:

{email_text}
"""

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            text = (
                response.text
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

            data = json.loads(text)

            # Safety cleanup for bad Gemini outputs

            internship = str(
                data.get("internship", "")
            )

            ctc = str(
                data.get("ctc", "")
            )

            if internship.lower() == "yes":

                stipend_match = re.search(
                    r'₹[\d,]+\s*per\s*month',
                    ctc,
                    re.IGNORECASE
                )

                lpa_match = re.search(
                    r'₹?\s*[\d,.]+\s*LPA',
                    ctc,
                    re.IGNORECASE
                )

                if stipend_match:
                    data["internship"] = (
                        stipend_match.group()
                    )

                if lpa_match:
                    data["ctc"] = (
                        lpa_match.group()
                    )

            return data

        except Exception as e:

            print(
                f"Gemini attempt {attempt + 1} failed"
            )

            print(str(e))

            time.sleep(2)

    raise Exception(
        "Gemini failed after 3 attempts"
    )