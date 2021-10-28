# New York City Guide - Django Project

## Create group project repository with the project source code
The following steps can be carried out by one member of the team:
1. Download the project source code in this repository as a zipped folder
<img width="904" alt="Screen Shot 2021-10-28 at 4 59 26 PM" src="https://user-images.githubusercontent.com/7483633/139334764-49f52bc5-4293-45da-a677-736ddfcfd8ce.png">
2. Unzip the contents of the zip folder
3. Create a new repository for the group
<img width="801" alt="Screen Shot 2021-10-28 at 4 49 41 PM" src="https://user-images.githubusercontent.com/7483633/139334999-4075825f-e1b7-4462-9b6c-ebd5daa9c0b6.png">
4. Follow the instructions for "or push an existing repoository from the command line" to push up the project source code
<img width="1244" alt="Screen Shot 2021-10-28 at 4 50 20 PM" src="https://user-images.githubusercontent.com/7483633/139335229-2567012c-e79a-41f1-b216-f98ed4af5772.png">
5. Invite your group member(s) to the repository to start collaborating on the repository!

## Setting up your Python web development environment

### 1. Create a virtual environment

At the root folder of the repository run:
```
python3 -m venv venv
```
Make sure to call your virtual environment "venv"

### 2. Run virtual environment
#### On Windows:
Windows Powershell users:
```
venv\Scripts\activate.bat
```
Bash users:
```
source venv/Scripts/activate
```
#### On Unix or MacOS:
```
source venv/bin/activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run Django
```
python manage.py runserver
```
And go to `http://localhost:8000`
