# ✈️ PlanWise – Smart Travel Packing Assistant

PlanWise is a smart travel planning application that helps users generate optimized packing lists based on travel duration, destination, season, airline baggage limits, and personal preferences.

---

## 🚀 Features

### 🧠 Smart Packing Logic
- Duration-based planning (Days / Weeks / Months / Years)
- Real-world packing logic (caps clothing to ~7 days)
- Seasonal adjustments based on travel month
- Purpose-based recommendations (Vacation, Business, Study)

### ✈️ Airline-Aware Packing
- Baggage limits based on airline and class
- Weight estimation
- Overweight warnings

### 🎯 Personalized Inputs
- From & Destination cities
- Gender-specific packing
- Custom inputs (Other categories)
- Travel month selection

### 🖥️ Modern UI (CustomTkinter)
- Clean dashboard layout
- Split view (Inputs + Results)
- Scrollable panels
- Progress bar for baggage usage
- Color-coded feedback (within limit / overweight)

---

## 🧱 Project Structure
Planwise/
│
├── main.py
│
├── ui/
│ ├── app.py
│ └── components.py
│
├── core/
│ └── packing_engine.py
│
├── services/
│ ├── data_loader.py
│ └── weather.py
│
├── data/
│ ├── packing_items.json
│ └── cities.json


## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/your-username/planwise.git
cd planwise
2. Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install customtkinter requests
▶️ Run the Application
python main.py

🧠 How It Works
User inputs travel details
Duration is normalized into days
Season is derived from travel month
Packing logic:
Clothing capped to realistic usage (~7 days)
Essentials always included
Purpose-based additions
Weight is estimated
Compared with airline baggage limits
UI displays:
Packing list
Weight progress bar
Status (within limit / overweight)

📊 Example Output
From: Delhi → Berlin
Month: June (Summer)

Carry-On:
• Passport
• Tickets
• Phone

Checked:
• T-Shirts x7
• Jeans x3
• Underwear x7

Summary:
• Estimated Weight: 15 kg
• Airline Limit: 25 kg
• ✅ Within baggage limit

🔮 Future Scope
🌍 Smart Integrations
Real-time city autocomplete (API-based)
Live weather integration
Real airline baggage API
🧠 AI Enhancements
AI-based packing suggestions
Context-aware recommendations (destination-specific)
📄 Export Features
Export packing list as PDF
Shareable travel plan
🎨 UI Improvements
Card-based layout instead of textbox
Icons & visual categories
Light/Dark mode toggle
📱 Platform Expansion
Web version (React / Flask)
Mobile app (React Native / Flutter)

💡 Key Learnings
Modular architecture design
Separation of concerns (UI / Core / Services)
Real-world UX design principles
Constraint-based problem solving
GUI development using CustomTkinter

📌 Author
Tushar Pareek
