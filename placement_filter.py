def is_placement_email(email_text):

    text = email_text.lower()

    keywords = [
        "hiring",
        "placement",
        "intern",
        "internship",
        "full time",
        "full-time",
        "recruitment",
        "job opening",
        "apply",
        "ctc",
        "package",
        "eligibility",
        "campus drive",
        "online assessment",
        "oa",
        "interview"
    ]

    for keyword in keywords:
        if keyword in text:
            return True

    return False