### -----Debug Mode Engaged: Flight Booking is Underway!-----

# Flight Booking Project


## Table of Contents

1. Introduction
2. Features
3. Installation
4. Usage
5. Technologies
6. How to Contribute
7. License

## Introduction

Flight Booking is a web application that allows users to search for flights, make bookings, and manage their travel plans conveniently. It provides a user-friendly interface for users to browse available flights and book their desired options hassle-free. The project is built using Django, a powerful Python web framework, along with other technologies to ensure a smooth user experience.

## Features

- **User Registration and Login:** Create an account or log in to access flight booking features.
- **Flight Search:** Search for available flights based on source city, destination city, date, time, and flight number.
- **Booking Management:** View and manage your booked flights in one place.
- **Admin Dashboard:** Admins have a dedicated dashboard to manage flights and view bookings.
- **Responsive Design:** The application is designed to work seamlessly on various devices.

## db schema
![db schema image](https://github.com/adarshmalviy/flight_booking/blob/main/graphviz.svg)

## Architecture

The architecture of the flight booking web application, including its web pages, apps, modules, and database.

**1. Architecture:**
The flight booking web application follows the Model-View-Controller (MVC) architectural pattern. In Django, it's commonly referred to as the Model-View-Template (MVT) pattern. Here's a brief overview of each component:

- **Models:** The models represent the structure and behavior of the data in the application. In this project, you have models for `User`, `Flight`, and `Booking`. Each model is defined in a separate app and maps to a database table.

- **Views:** The views handle the business logic and interact with the models and templates. In this project, views are defined as Python functions or class-based views. They handle user requests, process data, and render the appropriate template.

- **Templates:** The templates define the user interface and presentation of the application. They are written in HTML with embedded template tags. Templates render dynamically based on the data provided by the views.

**2. Apps:**
The flight booking web application is organized into multiple apps to keep the codebase modular and maintainable. Here are the apps and their responsibilities:

- **flight_booking:** This is the main app that contains the homepage template and serves as the entry point to the application. It includes URLs for user login, signup, and admin login.

- **users:** This app manages user-related functionality, including user signup, login, and logout views. It also includes templates for user login and signup pages.

- **flights:** This app handles flight-related functionality, such as searching for flights, booking flights, and viewing booked flights. It includes templates for search_flights, book_flight, view_bookings, and booking_failed pages.

- **admins:** This app is dedicated to admin functionality, such as adding and removing flights and viewing all bookings for a flight. It includes templates for admin login, logout, add_flight, dashboard, remove_flight, and view_all_bookings pages.

**3. Database:**
The flight booking web application uses a relational database to store and manage data. Django supports multiple database backends, but for simplicity, we'll assume the use of SQLite in this project. SQLite is the default database backend in Django, and it's suitable for development and small-scale applications.

In the database, you will have tables for users, flights, and bookings, corresponding to the models defined in each app. Each table will have columns that represent the attributes of the model fields.

**4. Web Pages:**
The web pages are designed using HTML, CSS (Bootstrap), and template tags. The pages are visually appealing and provide a user-friendly interface for the application's functionality. The pages include:

- **Homepage:** The landing page of the application that offers options to login, signup, or access the admin panel.

- **User Signup and Login:** Pages where users can sign up or log in to the application.

- **User Dashboard:** After logging in, users are directed to their dashboard, where they can search for flights, view their bookings, and book flights.

- **Admin Dashboard:** After admin login, admins are directed to their dashboard, where they can add and remove flights, and view all bookings for a flight.

- **Search Flights:** A page where users can search for available flights based on various parameters.

- **Book Flight:** A page where users can book a flight by entering the flight number.

- **View Bookings:** A page where users can view their booked flights.

- **Booking Failed:** A page displayed when a booking fails, along with an option to go back to the dashboard.

- **Add Flight:** A page for admins to add new flights to the database.

- **Remove Flight:** A page for admins to remove a flight by providing the flight ID.

- **View All Bookings:** A page for admins to view all bookings for a specific flight by providing the flight number.


## Installation

1. Clone the repository: `git clone https://github.com/your-username/flight-booking.git`
2. Navigate to the project directory: `cd flight-booking`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Start the development server: `python manage.py runserver`
2. Open your web browser and visit: `http://localhost:8000`

## Technologies

- Django: A high-level Python web framework for rapid development and clean, pragmatic design.
- Django Rest Framework: A toolkit for building Web APIs with Django.
- HTML/CSS: Used for designing and styling web pages.
- Bootstrap: A popular CSS framework for building responsive and attractive user interfaces.
- SQLite: A relational database system.
- DatetimeWidget: A Django widget for convenient datetime input.

## How to Contribute

We encourage students like you to contribute to this open-source project and learn from real-world experiences. If you find any issues or have suggestions for improvement, follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name: `git checkout -b fix-issue-123`
3. Make your changes and commit them: `git commit -m "Fix issue #123"`
4. Push your changes to your forked repository: `git push origin fix-issue-123`
5. Create a pull request from your branch to the main repository.

Happy coding!
