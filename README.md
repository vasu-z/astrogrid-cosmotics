# 🚀 AstroGrid – Smart Space Cargo Management System

Official repository for AstroGrid, built by Team Cosmotics.

## 🧠 Problem Solved

Managing cargo in a space station is complex due to limited space, strict priorities, expiry constraints, and obstruction during retrieval. AstroGrid focuses on the decision-making layer of this problem and provides a backend system to manage cargo efficiently and safely.

# AstroGrid addresses:

 Priority-based cargo retrieval
 Expiry-aware cargo monitoring
 Obstruction-aware retrieval planning
 Clear visual signaling of urgency and importance
 Structured logging of cargo operations

## 🛠️ Tech Stack

 FastAPI – Backend APIs and orchestration
 SQLite (via SQLAlchemy) – Persistent storage for the MVP
 Core Python – Priority logic, expiry handling, and retrieval rules
 OpenAPI / Swagger – Live API documentation and testing
 Google Cloud Platform (GCP) – Target deployment and scalability platform
 VS Code – Development environment

## 🧬 Features Breakdown

| Feature                     | Description                                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| Priority-Based Retrieval    | High-priority cargo is always handled first                                 |
| Expiry-Aware Logic          | Items nearing or past expiry are flagged automatically                      |
| Obstruction-Aware Retrieval | Identifies and removes blocking items before accessing a target             |
| Visual Urgency Metadata     | Each item includes color, urgency score, and intensity for UI visualization |
| Cargo Optimization          | Sorts cargo based on priority and weight                                    |
| System Logging              | Tracks all major cargo operations                                           |
| Exportable Layout           | Current cargo state can be exported for analysis                            |

## 📺 Demo Video

🎥 Watch the Final Hackathon Submission Video
[https://drive.google.com/file/d/1hJa9w5Dav_mmzk8xq67xCINA69whJKGu/view?usp=drivesdk](https://drive.google.com/file/d/1hJa9w5Dav_mmzk8xq67xCINA69whJKGu/view?usp=drivesdk)

## 📂 How to Run

git clone [https://github.com/vasu-z/astrogrid-cosmotics.git](https://github.com/vasu-z/astrogrid-cosmotics.git)
cd astrogrid-cosmotics

uvicorn main:app --reload

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to access the API documentation.

## 🔍 Sample API Endpoints

 POST /cargo/ – Add a new cargo item
 GET /cargo/ – View all cargo items
 GET /cargo/sorted – View cargo sorted by priority and weight
 GET /optimize – Run cargo optimization logic
 GET /retrieve/{id} – Retrieve a cargo item with obstruction handling
 GET /visual – Get visual metadata for all cargo
 GET /logs – View system operation logs
 GET /export – Export current cargo layout

