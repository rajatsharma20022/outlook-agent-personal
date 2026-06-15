import time

from email_reader import (
    get_unread_emails,
    mark_as_read
)

from ai_parser import extract_placement_info
from notion_writer import create_company
from find_company import find_company
from update_company import update_company
from placement_filter import is_placement_email


INVALID_COMPANIES = [
    "Dear",
    "Dear Students",
    "Student",
    "Students",
    "Unknown",
    "Team",
    "Placement Team",
    "Regards",
    "Thanks"
]


def process_emails():

    emails = get_unread_emails()

    if not emails:

        print("No unread emails found.")

        return

    for email in emails:

        email_id = email["id"]
        email_text = email["body"]

        print("\n==========================")
        print("EMAIL:")
        print(email_text[:500])

        if not is_placement_email(email_text):

            print("Skipped: Not a placement email")

            mark_as_read(email_id)

            continue

        try:

            data = extract_placement_info(email_text)

            print("\nPARSED:")
            print(data)

            # Handle multiple jobs
            if isinstance(data, list):

                print("Multiple jobs found")

                for job in data:

                    company = job.get("company")

                    if not company:
                        continue

                    if company in INVALID_COMPANIES:

                        print(
                            f"Skipping invalid company: {company}"
                        )

                        continue

                    if len(company) > 30:

                        print(
                            f"Skipping suspicious company: {company}"
                        )

                        continue

                    page_id = find_company(company)

                    if page_id:

                        print(f"Updating {company}")

                        update_company(
                            page_id,
                            job
                        )

                    else:

                        print(f"Creating {company}")

                        create_company(job)

                mark_as_read(email_id)

                print("Marked as read")
                print("Done")

                continue

            # No company found
            if not data.get("company"):

                print("No company found")

                mark_as_read(email_id)

                continue

            company = data["company"].strip()

            # Invalid company names
            if company in INVALID_COMPANIES:

                print(
                    f"Invalid company name: {company}"
                )

                mark_as_read(email_id)

                continue

            # Very long company names
            if len(company) > 30:

                print(
                    f"Suspicious company name: {company}"
                )

                mark_as_read(email_id)

                continue

            # Promotional emails
            if data.get("category") == "Product Promotion":

                print(
                    "Skipped: Promotional email"
                )

                mark_as_read(email_id)

                continue

            page_id = find_company(company)

            if page_id:

                print(
                    "Company already exists"
                )

                print(
                    "Updating record..."
                )

                update_company(
                    page_id,
                    data
                )

            else:

                print(
                    "New company found"
                )

                print(
                    "Creating record..."
                )

                create_company(data)

            mark_as_read(email_id)

            print("Marked as read")
            print("Done")

        except Exception as e:

            print("ERROR:")

            print(str(e))


if __name__ == "__main__":

    print("\n====================================")

    print("Checking Gmail for new emails...")

    process_emails()

    print("Done")