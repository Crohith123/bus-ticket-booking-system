# 🚌 Real-Time Bus Ticket Booking Management System

A Python-based console application that simulates a bus reservation system with seat management, passenger records, ticket booking/cancellation, booking history, and revenue reporting.

## 📌 Project Overview

This project demonstrates how core Python programming concepts can be combined to build a practical reservation workflow. Bus, route, fare, seat, and passenger information are maintained in memory while users interact with the system through a menu-driven console interface.

## ✨ Features

- View available buses, routes, departure times, fares, and seat counts
- View a visual seat layout for each bus
- Book tickets with passenger details
- Prevent booking of already occupied seats
- Cancel booked tickets
- Search passenger booking details
- View all current bookings
- Generate bus-wise booking and revenue summaries
- Track booking history during the program session
- Generate a formatted ticket after successful booking

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Concepts:** Functions, dictionaries, loops, conditional logic, exception handling
- **Python modules:** `os`, `datetime`
- **Interface:** Command-line / console

## 📂 Project Structure

```text
bus-ticket-booking-system/
├── bus.py       # Main application
└── README.md    # Project documentation
```

## ⚙️ How It Works

```text
Start Application
       ↓
Main Menu
       ↓
Select Operation
       ↓
Bus / Seat Management
       ↓
Passenger & Booking Processing
       ↓
Ticket / Report Output
       ↓
Return to Main Menu
```

## ▶️ How to Run

### 1. Install Python

Install Python 3.x and verify it from a terminal:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone https://github.com/Crohith123/bus-ticket-booking-system.git
cd bus-ticket-booking-system
```

### 3. Run the application

```bash
python bus.py
```

## 🧾 Main Menu

The application provides nine operations:

| Option | Operation |
|---:|---|
| 1 | View Available Buses |
| 2 | View Seat Layout |
| 3 | Book Ticket |
| 4 | Cancel Ticket |
| 5 | Search Passenger |
| 6 | View All Bookings |
| 7 | Bus Summary Report |
| 8 | Booking History |
| 9 | Exit |

## 📊 Sample Business Logic

The system maintains four sample routes with different bus types and fares. Each bus has 20 seats, and the application dynamically calculates available seats, booked seats, and total collection from the current in-memory bookings.

## 🎯 Skills Demonstrated

`Python` · `Problem Solving` · `Data Structures` · `Functions` · `Dictionaries` · `Input Validation` · `Exception Handling` · `Business Logic` · `Console Application Development`

## 🚀 Future Enhancements

- Add SQLite/MySQL database persistence
- Generate unique booking IDs and digital tickets
- Add date-wise and route-wise booking management
- Add stronger passenger input validation
- Add a graphical or web-based interface
- Add automated tests

## 👨‍💻 Author

**C. Rohith Kumar Reddy**

GitHub: [Crohith123](https://github.com/Crohith123)

LinkedIn: [Chaganti Rohith](https://linkedin.com/in/chagantirohith)

## 📄 License

This project is intended for educational and portfolio purposes.
