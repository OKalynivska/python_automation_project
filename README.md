# python_automation_project
The main goal of this project is learning python for writing different tests

# **Getting Started**

## Prerequisites

Python 3.13+

pip

## Installation

### Install dependencies:

pip install -r requirements.txt

### Run all tests from one class

pytest tests/test_login.py::TestLogin

### Run with report generation
 pytest web/tests --alluredir=allure-results

### See the report
allure serve allure-results

