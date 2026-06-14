import re


def extract_company(subject):

    companies = [
        "Xeno",
        "Adobe",
        "Microsoft",
        "Amazon",
        "TCS",
        "Infosys"
    ]

    for company in companies:
        if company.lower() in subject.lower():
            return company

    return "Unknown"


def extract_role(subject):

    roles = [
        "FDE",
        "SDE",
        "Intern",
        "GET",
        "Analyst"
    ]

    for role in roles:
        if role.lower() in subject.lower():
            return role

    return "Unknown"