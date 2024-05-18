# eBay QA Automation

This repository contains automated tests for eBay's website using Selenium, pytest, and Allure for reporting.

## Project Description

The eBay QA Automation project aims to automate the testing process for eBay's website. It utilizes Selenium, pytest, and Allure to create robust and reliable automated tests.

## Setup

To run the tests, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/muhit-khan/eBay_QA_Automation.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:

   ```bash
   pytest
   ```

## Allure Report

After running the tests, you can generate and view the Allure report. The Allure report provides detailed information about the test execution and results.

To generate and open the Allure report, follow these steps:

1. Generate the Allure report locally:

   ```bash
   allure serve ./reports/allure
   ```

2. Or, Open the Live Allure report in your browser:

   The Allure report is hosted on the following link: [Live Allure Report](https://6648ab3811b525d9576c1028--inspiring-parfait-767564.netlify.app/)

This will open a web browser with the generated report, allowing you to view the test results, including detailed information about test cases, steps, and any failures encountered.
