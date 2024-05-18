# QCI_Task_WebAutomation

This project is a web automation task for QCI (Quality Code Inspection). It aims to automate the testing of a web application using Python and pytest.

## Functionality

The QCI_Task_WebAutomation project provides automated tests for the eBay website. It covers various scenarios to ensure the functionality of the website is working as expected. The tests include searching for products, adding items to the cart, and checking out.

## How to Run

To run the tests, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command in the project directory:
   ```
   pip install -r requirements.txt
   ```
3. Execute the following command to run the tests:
   ```
   pytest -v -s tests/test_ebay.py --alluredir=allure-results
   ```

## Viewing Reports

After running the tests, you can view the reports using Allure. Follow these steps:

1. Install Allure command-line tool by referring to the official documentation.
2. Navigate to the project directory.
3. Execute the following command to serve the Allure report:
   ```
   allure serve allure-results
   ```

This will open a web browser with the generated report, allowing you to view the test results, including detailed information about test cases, steps, and any failures encountered.

Please note that you may need to customize the commands based on your specific environment and setup.

For any further assistance, feel free to ask.
