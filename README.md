# 🚀 AstroGrid – Smart Space Cargo Management System

Official repository for AstroGrid, built by Team Cosmotics for the National Space Hackathon 2025 organized by IIT Delhi.

---

## 🧠 Problem Solved

Astronauts face extreme challenges in managing onboard cargo in microgravity. AstroGrid solves:

- 🔴 Priority-Based Retrieval
- 📦 Smart Cargo Placement with Genetic Algorithm
- 🔁 Obstruction-Aware Retrieval Logic
- 🌈 Visual AR Scanner for Real-Time Item Search
- 🧠 Auto Sorting by Gravity and Priority
- ⚠️ Expiry Detection and Alerting System

---

## 🛠️ Tech Stack

- FastAPI – Backend APIs
- PostgreSQL + Redis – Storage + Real-time caching
- Core Python – Custom Genetic Algorithm (GA)
- Figma – UI/UX Design
- Docker – Containerization
- VS Code – Development Environment

---

## 🧬 Features Breakdown

| Feature                     | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| 🧠 Genetic Algorithm (GA)   | Optimized 3D cargo placement based on weight, priority, expiry, size |
| 🧲 Obstruction Logic        | Retrieves items by intelligently removing blockers                   |
| 🔎 Smart Flashlight Scanner | AR Camera + Priority Glow + Expiry Alerts                            |
| ⚙️ Gravity-Based Sorting    | Heavy items sink, light/critical items float on top                  |
| 🟡 Expiry Glow Stickers     | Items glow yellow/red when expired or near expiry                    |
| 📊 Real-Time Grid Tracking  | Volume-based grid visualization of cargo layout                      |
| 🚨 Beep on Expiry Detection | Audible alert when scanning expired or expiring items                |

---

## 📺 Demo Video

🎥 [Watch the Final Hackathon Submission Video](https://drive.google.com/file/d/1hJa9w5Dav_mmzk8xq67xCINA69whJKGu/view?usp=drivesdk)

---


## 📂 How to Run


git clone https://github.com/vasu-z/astrogrid-cosmotics.git
cd astrogrid-cosmotics

# Run Docker containers
docker-compose up --build

# Visit localhost:8000/docs to access API docs

---

## 🔍 Sample API Endpoints

- POST /cargo/ – Add a new item
- GET /optimize – Run Genetic Algorithm
- GET /retrieve/{id} – Retrieve item safely
- GET /logs – View operations log
- GET /export – Export current layout

---

