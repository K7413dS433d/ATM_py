# ATM Machine Project

A Python project that simulates an ATM machine with a simple database implementation using JSON and text files. This project allows users, including administrators, to perform various banking operations such as withdrawals, deposits, and balance inquiries.

## Table of Contents
- [Introduction](#introduction)
- [Authentication](#authentication)
- [Project Structure](#project-structure)
- [Includes Directory](#includes-directory)
- [Files Directory](#files-directory)
- - [Database Directory](#database-directory)
- - [Log Files](#log-files)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The ATM Machine project is designed to provide a basic ATM experience with functionalities such as account management, transaction recording, and user authentication. The project employs a combination of Python scripts and JSON/text files to achieve its objectives.

## Authentication

The project includes predefined user credentials for demonstration purposes:

**Admin:**
- ID: admin
- Password: admin

**Users:**
- ID: khaled, Password: khaled
- ID: zeiad, Password: zeiad
- ID: eslam, Password: eslam

Please note that these credentials are meant for testing and demonstration only.

## Project Structure

The project directory structure is organized as follows:

ATM
├── Includes
│ ├── ATM.py
│ ├── Authentication.py
│ ├── admin_functions.py
│ └── encryption.py
├── README.md
├── files
│ ├── databases
│ │ ├── ZXNsYW0=.json
│ │ ├── a2hhbGVk.json
│ │ └── emVpYWQ=.json
│ ├── log.txt
│ └── users.json
└── main.py


## Includes Directory

The `Includes` directory contains essential scripts that drive the functionality of the ATM machine. Here's a brief overview:

- **encryption.py:** Manages data encryption and decryption for user security.
- **admin_functions.py:** Provides admin-specific functions, such as user management and transactions history.
- **Authentication.py:** Handles user authentication and log recording.
- **ATM.py:** Contains core ATM functions for transactions, balance inquiries, and options printing.

## Files Directory

The `files` directory holds essential data and subdirectories for database and log files. Here's a breakdown:

### Database Directory

This subdirectory (`databases`) contains JSON files corresponding to user accounts.

### Log Files

The `log.txt` file records transaction logs and user actions for auditing purposes.

## Usage

1. Clone this repository using:
    git clone https://github.com/your-username/ATM.git

2. Run the main script:
   python main.py

3. Follow the on-screen instructions to interact with the ATM.

## Contributing

Contributions to this project are welcome! If you find a bug or have an enhancement in mind, please open an issue or submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).




