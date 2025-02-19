from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import json
import logging
from django.views.decorators.csrf import csrf_exempt  # For testing only
from django.views.decorators.csrf import ensure_csrf_cookie  # Helps with CSRF token handling
from .model_loader import model
from .models import Prediction
import pandas as pd

# Set up logging
logger = logging.getLogger(__name__)

@ensure_csrf_cookie
def home(request):
    """ Renders the main prediction page with CSRF token setup. """
    return render(request, "predictor/index.html")

def predict(request):
    """ Handles prediction requests via POST. """
    if request.method == "POST":
        try:
            # Try parsing JSON first
            try:
                data = json.loads(request.body.decode("utf-8"))
            except json.JSONDecodeError:
                data = request.POST  # Fall back to form data if JSON fails

            # Debugging: Print received data
            logger.debug("Received Data: %s", data)

            # Validate received data
            required_fields = ["socioeconomic_score", "sleep_hours", "study_hours", "attendance"]
            for field in required_fields:
                if field not in data or data[field] in [None, ""]:
                    return JsonResponse({"error": f"Missing required field: {field}"}, status=400)

            # Convert values to float safely
            try:
                socioeconomic_score = float(data["socioeconomic_score"])
                sleep_hours = float(data["sleep_hours"])
                study_hours = float(data["study_hours"])
                attendance = float(data["attendance"])
            except ValueError:
                return JsonResponse({"error": "Invalid input: All values must be numeric"}, status=400)

            prediction = model.predict(pd.DataFrame([[socioeconomic_score, sleep_hours, study_hours, attendance]]))[0]

            # Save to database
            pred_instance = Prediction.objects.create(
                socioeconomic_score=socioeconomic_score,
                sleep_hours=sleep_hours,
                study_hours=study_hours,
                attendance=attendance,
                predicted_grade=prediction
            )

            return JsonResponse({"predicted_grade": round(prediction, 2)})

        except Exception as e:
            logger.error("Error in prediction: %s", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

def view_predictions(request):
    """ Retrieves the last 10 predictions from the database. """
    predictions = Prediction.objects.order_by("-created_at")[:10]
    data = [
        {
            "id": p.id,
            "socioeconomic_score": p.socioeconomic_score,
            "sleep_hours": p.sleep_hours,
            "study_hours": p.study_hours,
            "attendance": p.attendance,
            "predicted_grade": p.predicted_grade,
            "created_at": p.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for p in predictions
    ]
    return JsonResponse({"predictions": data})











