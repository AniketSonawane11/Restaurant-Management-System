# Restaurant Management System

## Overview
The **Restaurant Management System** is a GUI-based application developed using Python and Tkinter. It helps manage restaurant operations by handling food orders, calculating costs, generating receipts, and even sending bills via SMS.

## Features
- User-friendly graphical interface using **Tkinter**.
- Categorized sections for **food, drinks, and cakes**.
- **Cost Calculation**: Automatically calculates food costs, taxes, and total bill.
- **Receipt Generation**: Displays and saves receipts.
- **Built-in Calculator**: Enables quick cost calculations.
- **Save Bill**: Option to save the bill for record-keeping.
- **Send Bill via SMS**: Send bill details directly to the customer's mobile phone.
- **Reset Functionality**: Clears all inputs and resets the system.

## Technologies Used
- **Python** (Core Programming Language)
- **Tkinter** (For GUI Development)
- **time** (For time-related functions)
- **filedialogue** (For file selection and saving receipts)
- **messagebox** (For alert and confirmation dialogs)
- **requests** (For sending bill via SMS)

## Application Structure
The application is structured into different frames:
1. **Title Frame**: Displays the project title.
2. **Category Frame**: Holds the different menu sections:
   - **Food Section**
   - **Drinks Section**
   - **Cakes Section**
3. **Billing & Calculation Frame**: Handles:
   - Tax calculation
   - Total cost calculation
   - Cost of food, drinks, and cakes
4. **Bill Area & Calculator Frame**: Includes:
   - Display area for generated bills
   - A built-in calculator
   - Buttons for key actions (Total, Receipt, Save Bill, Send Bill via SMS, Reset)

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/restaurant-management-system.git
   ```
2. Install dependencies:
   ```sh
   pip install requests
   ```
3. Run the application:
   ```sh
   python restaurant_management.py
   ```

## Contribution
Feel free to contribute to the project by submitting pull requests or reporting issues.

## License
This project is licensed under the MIT License.

