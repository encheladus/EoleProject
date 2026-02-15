# 🌬️ Eole

Flight price analyzer based on **trip duration**, not fixed start/end dates.

---

## 🎯 Concept

Most flight search engines require fixed departure and return dates (± 3 days flexibility at best).

Eole takes a different approach:

Instead of choosing *when* to travel,
you choose:

- ✈️ Departure location (e.g. Paris)
- 🌏 Destination (e.g. Seoul)
- ⏳ Trip duration (e.g. 2 weeks)
- 📅 Search window (e.g. next 6 months or 1 year)

The engine calculates all valid date combinations and finds the cheapest round-trip option.

---

## 🚀 Goal

### Product Goal
Provide a smarter way to plan vacations based on the **cheapest available period** rather than fixed dates.

### Personal Goal
- Build a serious solo project using Agile methodology
- Practice Domain Driven Design (DDD)
- Improve OOP skills
- Learn API integration properly
- Deliver a clean CLI MVP first

---

## 🏗️ Architecture

The project follows a simplified Domain Driven Design (DDD) structure.

```text
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
```

---

## 🧪 MVP Scope

Initial version:

- CLI-based program
- Round-trip flights only
- Single provider API
- No database
- No notifications

---

## 🛣️ Roadmap

- [Sprint 1] Date range generator
- [Sprint 2-3] API flight provider integration
- [Sprint 4] Cheapest price selection logic
- [Sprint 5-6] CLI interface
- [Sprint 7] Logging & error handling

---

## 🧠 Tech Stack

- Python 3.x
- OOP
- DDD (light version)
- REST API integration
