# ui/app.py

import customtkinter as ctk
from core.packing_engine import generate_packing_list
from services.data_loader import load_cities

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PlanWiseApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("PlanWise ✈️")
        self.geometry("1200x700")

        self.cities = load_cities()

        self.build_layout()

    # ---------------- LAYOUT ---------------- #
    def build_layout(self):

        title = ctk.CTkLabel(
            self,
            text="✈️ PlanWise",
            font=("Arial", 26, "bold")
        )
        title.pack(pady=15)

        container = ctk.CTkFrame(self)
        container.pack(expand=True, fill="both", padx=20, pady=10)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=2)

        self.build_input(container)
        self.build_output(container)

    # ---------------- INPUT ---------------- #
    def build_input(self, parent):

        frame = ctk.CTkScrollableFrame(parent, corner_radius=20)
        frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(frame, text="Travel Details", font=("Arial", 18, "bold")).pack(pady=15)

        # -------- FROM CITY (SEARCHABLE) -------- #
        ctk.CTkLabel(frame, text="From City").pack(anchor="w", padx=20)

        self.from_city = ctk.CTkEntry(frame, placeholder_text="Type city...")
        self.from_city.pack(pady=5, padx=20, fill="x")

        # -------- DESTINATION -------- #
        ctk.CTkLabel(frame, text="Destination City").pack(anchor="w", padx=20)

        self.city = ctk.CTkEntry(frame, placeholder_text="Type city...")
        self.city.pack(pady=5, padx=20, fill="x")

        # -------- DURATION -------- #
        ctk.CTkLabel(frame, text="Duration").pack(anchor="w", padx=20)

        duration_frame = ctk.CTkFrame(frame)
        duration_frame.pack(pady=5, padx=20, fill="x")

        self.duration = ctk.CTkEntry(duration_frame, placeholder_text="Number", width=120)
        self.duration.pack(side="left", padx=5)

        self.duration_unit = ctk.CTkOptionMenu(
            duration_frame,
            values=["Days", "Weeks", "Months", "Years"]
        )
        self.duration_unit.pack(side="left", padx=5)

        # -------- MONTH -------- #
        ctk.CTkLabel(frame, text="Travel Month").pack(anchor="w", padx=20)

        self.month = ctk.CTkOptionMenu(
            frame,
            values=[
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ]
        )
        self.month.pack(pady=5, padx=20, fill="x")

        # -------- GENDER -------- #
        ctk.CTkLabel(frame, text="Gender").pack(anchor="w", padx=20)

        self.gender = ctk.CTkOptionMenu(
            frame,
            values=["Male", "Female", "Other"]
        )
        self.gender.pack(pady=5, padx=20, fill="x")

        # -------- PURPOSE -------- #
        ctk.CTkLabel(frame, text="Purpose").pack(anchor="w", padx=20)

        self.purpose = ctk.CTkOptionMenu(
            frame,
            values=["Vacation", "Business", "Study", "Other"],
            command=self.toggle_purpose_input
        )
        self.purpose.pack(pady=5, padx=20, fill="x")

        self.purpose_entry = ctk.CTkEntry(frame, placeholder_text="Enter custom purpose")
        self.purpose_entry.pack(pady=5, padx=20, fill="x")
        self.purpose_entry.pack_forget()

        # -------- AIRLINE -------- #
        ctk.CTkLabel(frame, text="Airline").pack(anchor="w", padx=20)

        airlines = [
            "Lufthansa", "Emirates", "Qatar Airways", "Air India",
            "Delta Air Lines", "American Airlines", "United Airlines",
            "British Airways", "Air France", "KLM", "Singapore Airlines",
            "Etihad Airways", "Turkish Airlines", "Qantas", "Other"
        ]

        self.airline = ctk.CTkOptionMenu(
            frame,
            values=airlines,
            command=self.toggle_airline_input
        )
        self.airline.pack(pady=5, padx=20, fill="x")

        self.airline_entry = ctk.CTkEntry(frame, placeholder_text="Enter airline")
        self.airline_entry.pack(pady=5, padx=20, fill="x")
        self.airline_entry.pack_forget()

        # -------- CLASS -------- #
        ctk.CTkLabel(frame, text="Travel Class").pack(anchor="w", padx=20)

        self.travel_class = ctk.CTkOptionMenu(
            frame,
            values=["Economy", "Business", "First", "Other"],
            command=self.toggle_class_input
        )
        self.travel_class.pack(pady=5, padx=20, fill="x")

        self.class_entry = ctk.CTkEntry(frame, placeholder_text="Enter class")
        self.class_entry.pack(pady=5, padx=20, fill="x")
        self.class_entry.pack_forget()

        # -------- BUTTON -------- #
        ctk.CTkButton(
            frame,
            text="Generate Packing List",
            command=self.generate
        ).pack(pady=20)

    # ---------------- OUTPUT ---------------- #
    def build_output(self, parent):

        frame = ctk.CTkFrame(parent, corner_radius=20)
        frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Allow expansion
        frame.grid_rowconfigure(4, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Title
        ctk.CTkLabel(
            frame,
            text="Packing Overview",
            font=("Arial", 20, "bold")
        ).grid(row=0, column=0, pady=10)

        # Info
        self.info_label = ctk.CTkLabel(
            frame,
            text="",
            justify="left",
            anchor="w"
        )
        self.info_label.grid(row=1, column=0, sticky="ew", padx=15, pady=5)

        # Progress bar
        self.progress = ctk.CTkProgressBar(frame, height=15)
        self.progress.grid(row=2, column=0, sticky="ew", padx=15, pady=10)

        # Status
        self.status_label = ctk.CTkLabel(frame, text="")
        self.status_label.grid(row=3, column=0, sticky="w", padx=15, pady=5)

        # TEXTBOX (handles its own scrolling)
        self.output = ctk.CTkTextbox(frame)
        self.output.grid(row=4, column=0, sticky="nsew", padx=15, pady=10)

    # ---------------- TOGGLES ---------------- #
    def toggle_purpose_input(self, value):
        if value == "Other":
            self.purpose_entry.pack(pady=5)
        else:
            self.purpose_entry.pack_forget()

    def toggle_airline_input(self, value):
        if value == "Other":
            self.airline_entry.pack(pady=5)
        else:
            self.airline_entry.pack_forget()

    def toggle_class_input(self, value):
        if value == "Other":
            self.class_entry.pack(pady=5)
        else:
            self.class_entry.pack_forget()

    # ---------------- LOGIC ---------------- #
    def generate(self):

        from_city = self.from_city.get()
        city = self.city.get()
        duration = self.duration.get()
        unit = self.duration_unit.get()
        gender = self.gender.get()
        month = self.month.get()

        purpose = self.purpose_entry.get() if self.purpose.get() == "Other" else self.purpose.get()
        airline = self.airline_entry.get() if self.airline.get() == "Other" else self.airline.get()
        t_class = self.class_entry.get() if self.travel_class.get() == "Other" else self.travel_class.get()

        if not from_city or not city or not duration:
            self.output.insert("end", "⚠️ Fill all fields\n")
            return

        inputs = {
            "from_city": from_city,
            "duration": duration,
            "unit": unit,
            "gender": gender,
            "airline": airline,
            "class": t_class,
            "purpose": purpose,
            "month": month
        }

        result, season = generate_packing_list(inputs)

        # Clear output
        self.output.delete("0.0", "end")

        # Extract summary data
        summary = result.get("Summary", [])

        estimated_weight = 0
        airline_limit = 0

        for item in summary:
            if "Estimated Weight" in item:
                estimated_weight = float(item.split(":")[1].strip().split()[0])
            if "Airline Limit" in item:
                airline_limit = float(item.split(":")[1].strip().split()[0])

        # Header Info
        self.info_label.configure(
            text=f"🛫 {from_city} → {city}\n📅 {month} ({season})"
        )

        # Progress Calculation
        if airline_limit > 0:
            ratio = min(estimated_weight / airline_limit, 1)
            self.progress.set(ratio)

        # Status Color
        if estimated_weight > airline_limit:
            self.status_label.configure(
                text="⚠️ Overweight - Reduce items",
                text_color="red"
            )
        else:
            self.status_label.configure(
                text="✅ Within baggage limit",
                text_color="green"
            )

        # Display Packing List
        for category, items in result.items():

            if category == "Summary":
                continue

            self.output.insert("end", f"\n📂 {category}\n")

            for item in items:
                self.output.insert("end", f"  • {item}\n")

        # Show summary at bottom
        self.output.insert("end", "\n--- SUMMARY ---\n")
        for item in summary:
            self.output.insert("end", f"{item}\n")