# Restful Booker Platform

Automated tests for verifying the functionality of the Restful Booker Platform website. These tests are implemented using Python and Selenium WebDriver.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)

## Introduction

This repository contains automated test cases to validate the functionality of the Restful Booker Platform.

## Prerequisites

Make sure you have the following installed:

    - Python 3.x
    - Selenium WebDriver
    - Webdriver-manager
    - Web browser driver (e.g., ChromeDriver for Google Chrome)
    - `pathlib` - library for working with file paths
    - `os` - library for interacting with the operating system
    - `logging` - library for generating log messages
    - `random` - library for random data generation
    - `Faker` - for generating fake data
    - `unittest-xml-reporting` - for generating XML report files
    - `HtmlTestReport` - for generating HTML report files
    - `requests` - to interact with API

## Installation

1.Clone the repository to your local machine:

    git clone [repository_url]

2.Install the required Python packages:

    pip install -r requirements.txt

## Running the Tests

1.Set the path to your web browser driver in the test scripts.

2.Run the tests using a test runner or directly via Python.

    python -m unittest discover tests
