# Micro Java Language Lexical Analyzer

This repository contains the code for a Lexical Analyzer designed specifically for the Micro Java language. The Lexical Analyzer parses input code written in Micro Java and generates tokens as output, which are then stored in an output file.

## Instructions

To execute the code:

1. **Clone** this repository to your local machine.
   
2. **Open** the `code.txt` file and paste the Micro Java code you want to analyze.

3. **Run** the main file using `python main.py`.

4. The output of the Lexical Analyzer will be stored in the `output.txt` file within the repository.

## Usage

The Lexical Analyzer is designed to process Micro Java code and identify tokens including keywords, identifiers, operators, symbols, and literals, among others. It performs lexical analysis to break down the code into tokens for further processing.

## Example

For example, consider the following Micro Java code:

```java
// Sample Micro Java code
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
````


After running the Lexical Analyzer, the output.txt file might contain tokens identified from the code, such as:
```java
Lexeme: class
Row Number: 0
Column Number: 1
Token Type: keyword
-------------------------------
Lexeme: HelloWorld
Row Number: 0
Column Number: 7
Token Type: identifier
-------------------------------
Lexeme: {
Row Number: 0
Column Number: 17
Token Type: operator
-------------------------------
Lexeme: public
Row Number: 1
Column Number: 5
Token Type: identifier
-------------------------------
Lexeme: static
Row Number: 1
Column Number: 12
Token Type: identifier
-------------------------------
Lexeme: void
Row Number: 1
Column Number: 19
Token Type: keyword
-------------------------------
Lexeme: main
Row Number: 1
Column Number: 24
Token Type: identifier
-------------------------------
Lexeme: (
Row Number: 1
Column Number: 27
Token Type: operator
-------------------------------
Lexeme: String
Row Number: 1
Column Number: 29
Token Type: identifier
-------------------------------
Lexeme: [
Row Number: 1
Column Number: 34
Token Type: operator
-------------------------------
Lexeme: ]
Row Number: 1
Column Number: 35
Token Type: operator
-------------------------------
Lexeme: args
Row Number: 1
Column Number: 38
Token Type: identifier
-------------------------------
Lexeme: )
Row Number: 1
Column Number: 41
Token Type: operator
-------------------------------
Lexeme: {
Row Number: 1
Column Number: 43
Token Type: operator
-------------------------------
Lexeme: System
Row Number: 2
Column Number: 9
Token Type: identifier
-------------------------------
Lexeme: .
Row Number: 2
Column Number: 14
Token Type: operator
-------------------------------
Lexeme: out
Row Number: 2
Column Number: 16
Token Type: identifier
-------------------------------
Lexeme: .
Row Number: 2
Column Number: 18
Token Type: operator
-------------------------------
Lexeme: println
Row Number: 2
Column Number: 20
Token Type: identifier
-------------------------------
Lexeme: (
Row Number: 2
Column Number: 26
Token Type: operator
-------------------------------
Lexeme: "Hello, World
Row Number: 2
Column Number: 28
Token Type: Unknown Token
-------------------------------
Lexeme: !
Row Number: 2
Column Number: 40
Token Type: Unknown Token
-------------------------------
Lexeme: "Hello, World"
Row Number: 2
Column Number: 29
Token Type: Unknown Token
-------------------------------
Lexeme: )
Row Number: 2
Column Number: 42
Token Type: operator
-------------------------------
Lexeme: }
Row Number: 3
Column Number: 4
Token Type: operator
-------------------------------
Lexeme: }
Row Number: 4
Column Number: 0
Token Type: operator
-------------------------------
````


## Contributing
If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

## Contact
For any inquiries or suggestions, please contact me via email at: umairahmedpaki7@gmail.com 
