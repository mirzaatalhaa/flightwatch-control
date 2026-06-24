# ✈️ FlightWatch Ground Control

> Internal operations console for the FlightWatch aviation spotting platform.

FlightWatch Ground Control is a Python-based command-line dashboard that gives operators real-time visibility into the health, activity, and analytics of the FlightWatch production infrastructure — all from a single interface communicating directly with the backend via secured REST APIs.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Dashboard Modules](#dashboard-modules)
- [Authentication](#authentication)
- [Roadmap](#roadmap)

---

## Overview

While FlightWatch provides the user-facing experience for logging and managing aircraft sightings, Ground Control is the operational backbone — a dedicated tool for platform operators to monitor system health, inspect live analytics, and understand platform activity without needing to query the database directly.

It integrates with the live FlightWatch infrastructure and retrieves real-time data from a production PostgreSQL database through a Node.js/Express backend.

---

## Features

| Capability | Description |
|---|---|
| 🟢 Production Health Monitoring | Check the status of all backend services in real time |
| 🗄️ Database Connectivity Verification | Confirm live connectivity to the production PostgreSQL instance |
| 🔐 JWT-Based Operator Authentication | Secure login flow using JSON Web Tokens |
| 📊 Live Analytics Dashboard | Real-time overview of platform-wide activity metrics |
| ✈️ Aircraft Statistics Reporting | Aggregated stats on logged aircraft by type, registration, and frequency |
| 🛫 Airline Statistics Reporting | Airline-level sighting summaries and activity breakdowns |
| 🏢 Airport Statistics Reporting | Airport traffic analysis based on logged sighting data |
| 🖥️ System & Network Information Monitoring | Local system and network diagnostics for the operator environment |

---

## Tech Stack

**Console**
- Python

**Backend**
- Node.js & Express
- PostgreSQL (Amazon RDS)

**Infrastructure**
- AWS EC2
- Docker
- Nginx
- Terraform

**CI/CD**
- GitHub Actions

**Security**
- JWT Authentication
- REST APIs over HTTPS

---

## Prerequisites

- Python 3.8+
- Access credentials for the FlightWatch operator account
- Network access to the FlightWatch production API

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/flightwatch-ground-control.git
cd flightwatch-ground-control

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root based on the provided template:

```bash
cp .env.example .env
```

Then fill in your environment values:

```env
FLIGHTWATCH_API_BASE_URL=https://api.flightwatch.example.com
FLIGHTWATCH_OPERATOR_USERNAME=your_username
FLIGHTWATCH_OPERATOR_PASSWORD=your_password
JWT_SECRET=your_jwt_secret
```

> **Note:** Never commit `.env` to version control. It is included in `.gitignore` by default.

---

## Usage

```bash
# Launch the Ground Control console
python main.py
```

On startup, the console will:

1. Authenticate the operator via JWT
2. Verify database connectivity
3. Run an initial health check against all backend services
4. Present the main dashboard menu

---

## Dashboard Modules

### Health Monitor
Polls the production backend and displays the status of all registered services. Highlights any degraded or unreachable endpoints.

### Database Verifier
Confirms live connectivity to the Amazon RDS PostgreSQL instance and reports connection latency.

### Analytics Dashboard
Displays a real-time snapshot of platform-wide activity, including total sightings, active users, and recent event counts.

### Aircraft Statistics
Reports aggregated data on logged aircraft — broken down by type, registration, and sighting frequency.

### Airline Statistics
Summarises sighting data at the airline level, showing which carriers appear most frequently across all user logs.

### Airport Statistics
Analyses platform data by airport, surfacing traffic patterns based on reported departure and arrival information.

### System & Network Info
Displays local diagnostics for the operator's machine, including CPU, memory, network interfaces, and connectivity status.

---

## Authentication

Ground Control uses JWT-based authentication to interact with the FlightWatch backend. On launch, the console exchanges operator credentials for a signed token, which is then attached to all subsequent API requests. Tokens are managed in-session and not persisted to disk.

---

## Roadmap

- [ ] Enhanced operational dashboards with richer visualisations
- [ ] Advanced analytics and custom reporting
- [ ] Sighting activity monitoring and alerting
- [ ] Deployment and infrastructure insights
- [ ] Role-based access controls for multi-operator teams
- [ ] Log streaming and audit trail viewer

---

## Contributing

This is an internal operations tool. If you have access to this repository and want to contribute, please open a pull request with a clear description of the change and reference any relevant issue numbers.

---

## License

Internal use only. Not licensed for public distribution.
