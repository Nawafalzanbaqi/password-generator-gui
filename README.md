# 🔐 Python CLI Password Generator

## 🌟 Project Overview

This repository hosts a simple, yet robust **Command-Line Interface (CLI) Password Generator** built using **Python**. The project was developed as part of the **Tuwaiq Academy** program, focusing on fundamental programming concepts and practical utility creation.

The tool is designed to quickly generate secure, random passwords of a specified length directly from the terminal, making it a fast and lightweight solution for developers and users.

## ✨ Key Features

- **CLI-Based:** Operates entirely through the command line, ensuring speed and minimal resource usage.
- **Customizable Length:** Requires a single mandatory argument to define the desired length of the password.
- **Character Set:** Generates passwords using a combination of uppercase letters, lowercase letters, and digits (A-Z, a-z, 0-9).
- **Lightweight:** Minimal dependencies, making it easy to run on any system with Python installed.
- **Educational Focus:** A clear example of basic Python scripting, argument parsing, and random data generation.

## 🛠️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Core Language** | Python 3 | Used for the entire scripting logic. |
| **Libraries** | `random`, `string`, `sys` | Used for generating random choices, defining character sets, and handling command-line arguments. |

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+** is required to run the script.

### Usage

The script requires one argument: the desired password length (as a positive integer).

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Nawafalzanbaqi/Python-CLI-Password-Generator.git
    cd Python-CLI-Password-Generator
    ```

2.  **Run the Script:**
    ```bash
    python password_generator_gui.py <length>
    ```

**Examples:**

| Command | Output (Example ) |
| :--- | :--- |
| `python password_generator_gui.py 12` | `aG9Fkd83LmP0Z` |
| `python password_generator_gui.py 20` | `XyZ1pQ2rS3tU4vW5xY6z` |

**Note:** Running the script without an argument will display the usage instructions.

## 🤝 Contributing

This project is a foundational piece from the Tuwaiq Academy. While it is primarily for educational purposes, suggestions for improvements or feature additions (such as adding special characters) are welcome via Pull Requests.

## 📄 License

[Specify License, e.g., This project is open-source and available under the MIT License.]

