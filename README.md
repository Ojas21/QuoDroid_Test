# QuoDroid_Test
Certainly! Here's an improved and more elaborate version of the README.md file:

---

# Automated Test Execution with Python, Django, and Robot Framework

## Overview

Welcome to our innovative solution for automated test execution using Python, Django, and Robot Framework. This project was developed as a response to a recruitment challenge, demonstrating our ability to quickly learn and apply new technologies while showcasing problem-solving capabilities.

The core objective of this project is to create an application that accepts a detailed API call, executes the testing steps provided within as a Robot Framework test, and returns the test output.

## Requirements

- Python 3.x
- Django
- Robot Framework
- SeleniumLibrary (a part of Robot Framework)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Django server:

    ```bash
    python manage.py runserver
    ```

2. Make a POST request to the following endpoint:

    - Endpoint: http://127.0.0.1:8000/testai/tests/v1/execute
    - Method: POST
    - Headers: Content-Type: application/json
    - Body:

    ```json
    {
        "tests":[
            {
                "title":"Open google.com",
                "steps":[
                    "Open Browser browser='chrome'",
                    "Go To url='https://google.com'"
                ]
            }
        ]
    }
    ```

3. The system will execute the provided test steps using Robot Framework and return the results.

## Result Example

Upon making a POST request, you will receive a JSON response containing the test execution results. Here's an example of what the result may look like:

```json
{
    "result": "==============================================================================\nTest Suite                                                                    \n==============================================================================\nTest Open google.com                                                  | PASS |\n------------------------------------------------------------------------------\nTest Suite                                                            | PASS |\n1 test, 1 passed, 0 failed\n==============================================================================\n"
}
```

## Project Structure

- `execute_tests` Django view handles the API endpoint for test execution.
- `test_suite.robot` file dynamically generated to define Robot Framework test cases.
- `requirements.txt` lists the project dependencies.

## Demonstration

![Demonstration Image](path/to/demo_image.png)

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README according to your project's specifics. If you need assistance with inserting images or any further customization, let me know!
