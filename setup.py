import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__vesrion__ = "0.0.0"

REPO_NAME = "TextSummarizerApp"
AUTHOR_USER_NAME = 'anirags'
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "anil.bhallavi.sbg@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__vesrion__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A little python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)