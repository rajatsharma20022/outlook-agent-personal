import json
import os

FILE_NAME = "processed_companies.json"


def load_companies():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_companies(companies):
    with open(FILE_NAME, "w") as f:
        json.dump(companies, f, indent=2)


def company_exists(company_name):

    companies = load_companies()

    return company_name.lower() in [
        c.lower() for c in companies
    ]


def add_company(company_name):

    companies = load_companies()

    if company_name not in companies:
        companies.append(company_name)

    save_companies(companies)