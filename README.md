# CS 476 - Project Prototype (Online Mentoring Service)

An app for users to teach or to learn.

## Description

This prototype aims to create an online synchronous learning service. “Mentors” create a course where they can assign scheduled tasks for “Students” who are enrolled in the course to complete on time. Mentors can provide direct-feedback and monitor Student progress. The domain of this service is general/broad, to allow different areas of expertise to be taught/learned, not confined to academics. The goal is to provide a closely guided and self-accountable learning tool compared to other similar platforms.

## Getting Started

### Dependencies and recommended tools

* Python3 _preferably 3.13_ (includes the following):
  - pip
  - venv (virtual environment)
* MongoDB
* Git
* __Recommended tools:__
  * mongosh OR MongoDB Compass (preferred)
  * VS Code
    * [Python extention](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    * [Jinja](https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja)
  * GitHub Desktop

### Setup

1. Make sure the dependencies from above are installed
2. Clone this repository
  * In your terminal, cd to the folder you want to store the local repo
  * Enter ```git clone https://github.com/yourname/project.git```
3. Open folder in VS Code
4. Open the bash terminal and enter the following:
```
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
5. Add the .env file provided in the root folder

### How to run the site locally

1. Make sure env is running:
    * If you are unsure, just enter ```"venv/Scripts/activate"``` while in the main directory.
2. Enter ```python app.py```
3. Enter ```flask run```
4. The site should be running locally, test at http://localhost:5000/

## Authors

Mark Justin Luansing - [GitHub](https://github.com/oralei)

## Version History

* 0.1
    * Initial Release - Includes functioning Flask, MongoDB, and Cloudinary

## License

## Acknowledgments
