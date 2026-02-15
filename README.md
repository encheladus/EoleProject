# EoleProject
Flight price analyzer based on a duration not a fix start/end date

# Goal
Creating an API wrapper which will have one purpose: Based on a duration (ex 2weeks), 2 localisation (ex Departure: Paris / Arrival: Seoul) and a range (ex 6 months or 1 year), my code using API flight will calculate all the date combination get the price (round flight first) and submit the cheapest combination. 
The purpose is simple providing a solution to a market where all the price analyser are based on a fix date range (± 3 days for some) -> And allowing people to prepare vacation based on the cheapest flight ticket for their dream destination.
On my end, the goal will be to perform a solo fun agile project while renforcing my programmation skills. Performing a software engineering like project and having fun discovering API coding.
I'm actually planning my MVP as a CLI program first.

The architecture of the python code will follow a Domain Driven Design (DDD) architecture, and POO code:
eole/
│
├── domain/
│   ├── trip.py
│   ├── price.py
│   └── search_policy.py
│
├── application/
│   └── search_use_case.py
│
├── infrastructure/
│   ├── providers/
│   ├── database/
│   └── notifications/
│
└── main.py
