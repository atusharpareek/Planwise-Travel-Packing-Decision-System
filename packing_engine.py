# core/packing_engine.py

from services.data_loader import load_items


# ----------- TIME ----------- #
def calculate_days(duration, unit):
    mapping = {
        "Days": 1,
        "Weeks": 7,
        "Months": 30,
        "Years": 365
    }
    return int(duration) * mapping.get(unit, 1)


# ----------- WEIGHT ----------- #
def estimate_weight(days, season):
    weight = 12  # base luggage

    if "Winter" in season:
        weight += 5
    elif "Summer" in season:
        weight += 2

    return weight

# ----------- AIRLINE ----------- #
def get_airline_limits(airline, travel_class):
    rules = {
        "Lufthansa": {"Economy": 23, "Business": 32, "First": 32},
        "Emirates": {"Economy": 23, "Business": 32, "First": 32},
        "Qatar Airways": {"Economy": 30, "Business": 40, "First": 50},
        "Air India": {"Economy": 25, "Business": 35, "First": 40},
    }

    return rules.get(airline, {}).get(travel_class, 23)


# ----------- CLOTHING ----------- #
def get_clothing(days, gender):
    # Cap at 7 days (real-life packing)
    effective_days = min(days, 7)

    if gender == "Male":
        return [
            ("T-Shirts", effective_days),
            ("Jeans", max(2, effective_days // 2)),
            ("Underwear", effective_days)
        ]

    elif gender == "Female":
        return [
            ("Tops", effective_days),
            ("Bottoms", max(2, effective_days // 2)),
            ("Undergarments", effective_days)
        ]

    return [
        ("Comfort Wear", effective_days),
        ("Bottoms", max(2, effective_days // 2))
    ]


# ----------- SEASON ----------- #
def get_seasonal_items(season):
    if "Winter" in season:
        return ["Jacket", "Thermals", "Gloves"]

    elif "Summer" in season:
        return ["Sunglasses", "Cap", "Sunscreen"]

    return ["Light Jacket", "Umbrella"]

def get_season_from_month(month):
    winter = ["December", "January", "February"]
    summer = ["June", "July", "August"]

    if month in winter:
        return "Winter"
    elif month in summer:
        return "Summer"
    else:
        return "Moderate"


# ----------- PURPOSE ----------- #
def get_purpose_items(purpose):
    purpose = purpose.lower()

    if "business" in purpose:
        return ["Formal Clothes", "Laptop", "Documents"]

    elif "vacation" in purpose:
        return ["Camera", "Travel Guide"]

    elif "study" in purpose:
        return ["Books", "Stationery", "Laptop"]

    return []


# ----------- MAIN ENGINE ----------- #
def generate_packing_list(inputs):
    data = load_items()

    days = calculate_days(inputs["duration"], inputs["unit"])
    season = get_season_from_month(inputs["month"])

    weight = estimate_weight(days, season)

    airline_limit = get_airline_limits(
        inputs["airline"],
        inputs["class"]
    )

    base = max(days // 7, 1)

    result = {
        "Carry-On": [],
        "Checked": [],
        "Summary": []
    }

    # -------- Essentials → Carry-On -------- #
    result["Carry-On"].extend(data["essentials"])

    # -------- Clothing → Checked -------- #
    clothing = get_clothing(days, inputs["gender"])
    result["Checked"].extend([f"{n} x{c}" for n, c in clothing])

    # -------- Seasonal -------- #
    result["Checked"].extend(get_seasonal_items(season))

    # -------- Purpose -------- #
    result["Checked"].extend(get_purpose_items(inputs["purpose"]))

    # -------- Summary -------- #
    result["Summary"] = [
        f"Trip Duration: {days} days",
        f"Estimated Weight: {weight} kg",
        f"Airline Limit: {airline_limit} kg"
    ]

    if weight > airline_limit:
        result["Summary"].append("⚠️ Overweight! Reduce items")
    else:
        result["Summary"].append("✅ Within baggage limit")

    # Add smart note
    if days > 7:
        result["Summary"].append("💡 Tip: Laundry can help reduce packing for long trips")

    return result, season