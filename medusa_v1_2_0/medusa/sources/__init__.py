"""
medusa/sources — free public API source modules

Each module exposes a single function:
    fetch() -> list[dict]

Each dict is a partial MedusaRecord (no case_id, lat/lng yet).
scanner.py normalizes and geocodes after collection.
"""
