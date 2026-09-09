from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HousePriceModel:
    """Example ML model wrapper for the project."""

    model_path: str

    def predict(self, features):
        # Replace with actual model loading and prediction logic later.
        return 0.0
