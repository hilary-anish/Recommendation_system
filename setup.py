from setuptools import setup


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


## edit below variables as per your requirements -
REPO_NAME = "Books-Recommender-System-ML"
AUTHOR_USER_NAME = "Anish Hilary"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup(
    name = SRC_REPO,
    version = "1.0.0",
    author = AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="anishhilary@gmail.com",
    packages = [SRC_REPO],
    python_requires = ">=3.7",
    install_requires = LIST_OF_REQUIREMENTS,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)