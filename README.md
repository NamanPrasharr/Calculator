Simple Text-to-Speech Calculator
Overview
This project is a basic command-line calculator built in Python. It takes two numbers and an operation as input from the user, performs the calculation, and provides the result both as printed output and spoken output using text-to-speech functionality.

Features
Accepts two numeric inputs (floating-point numbers).
Supports four operations: multiplication, division, addition, and subtraction.
Outputs the result to the console.
Uses text-to-speech to audibly announce the result or an error message.
Handles invalid operation inputs gracefully with a spoken and printed error message.
Prerequisites
To run this program, you need:

Python 3.x installed on your system.
The pyttsx3 library for text-to-speech functionality.
Installation
Install Python from python.org if you don’t have it.
Install the pyttsx3 library using pip:
bash

Collapse

Wrap

Copy
pip install pyttsx3
How to Use
Clone this repository to your local machine:
bash

Collapse

Wrap

Copy
git clone <repository-url>
Navigate to the project directory:
bash

Collapse

Wrap

Copy
cd <repository-folder>
Run the script:
bash

Collapse

Wrap

Copy
python calculator.py
Follow the prompts:
Enter the first number.
Enter the second number.
Choose an operation (mult, div, add, or sub).
The program will display the result on the screen and speak it aloud.
Operations
mult: Multiplies the two numbers.
div: Divides the first number by the second.
add: Adds the two numbers.
sub: Subtracts the second number from the first.
Notes
Ensure your system has speakers or headphones enabled to hear the text-to-speech output.
If an invalid operation is entered, the program will notify you both visually and audibly.
Future Improvements
Add support for more complex operations (e.g., exponentiation, modulus).
Include input validation for non-numeric entries.
Allow continuous calculations in a loop until the user chooses to exit.
Contributing
Feel free to fork this repository, make improvements, and submit a pull request! Suggestions and bug reports are welcome via the Issues tab.

License
This project is licensed under the MIT License. See the  file for details.# Calculator
