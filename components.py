# ui/components.py

import customtkinter as ctk


def create_card(parent, title):
    frame = ctk.CTkFrame(parent, corner_radius=15)

    label = ctk.CTkLabel(
        frame,
        text=title,
        font=("Arial", 16, "bold")
    )
    label.pack(pady=10)

    return frame