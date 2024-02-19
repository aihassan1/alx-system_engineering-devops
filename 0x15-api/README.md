0x15-api
# Project Title

## Description
This project involves interacting with a REST API using Python to retrieve employee data and organize it into different data structures. The main tasks include gathering data from the API, exporting the data to CSV and JSON formats, and organizing the data into dictionaries of lists of dictionaries.

## Concepts Covered
- Understanding of APIs, REST APIs, and microservices
- Python scripting for backend development
- Data formatting in CSV and JSON
- Code organization and style adherence

## Learning Objectives
By completing this project, you will gain knowledge and understanding of the following concepts:
- What Bash scripting should not be used for
- Basics of APIs and REST APIs
- Pythonic coding style and standards (PEP8)
- Data formats: CSV and JSON
- Importance of clean code and code organization

## Requirements
- Python 3.8.5 or higher
- Ubuntu 20.04 LTS
- pycodestyle version 2.8.* for code style adherence
- Libraries: urllib or requests for API interaction
- Text editors: vi, vim, emacs
- Execution environment setup with necessary permissions

## Tasks
1. **Gather data from an API**
   - Retrieve employee TODO list progress using a given employee ID
   - Display progress in a specific format
   - Utilize urllib or requests module for API interaction
   
2. **Export to CSV**
   - Extend the script to export data in CSV format
   - Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
   - Filename: USER_ID.csv
   
3. **Export to JSON**
   - Extend the script to export data in JSON format
   - Format: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
   - Filename: USER_ID.json
   
4. **Dictionary of list of dictionaries**
   - Export all tasks from all employees in JSON format
   - Format: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
   - Filename: todo_all_employees.json

## Usage
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Execute the Python scripts with appropriate parameters as mentioned in each task.

## File Structure
