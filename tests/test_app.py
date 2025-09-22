import os
import sys
from urllib.parse import quote

# Ensure src is importable
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_unregister():
    activity = "Chess Club"
    email = "test_student@example.com"

    # Ensure the student is not already signed up
    if email in client.get("/activities").json()[activity]["participants"]:
        client.delete(f"/activities/{quote(activity)}/unregister", params={"email": email})

    # Sign up the student
    signup = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})
    assert signup.status_code == 200
    assert "Signed up" in signup.json().get("message", "")

    # Attempt duplicate signup -> should fail
    dup = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})
    assert dup.status_code == 400

    # Unregister the student
    unregister = client.delete(f"/activities/{quote(activity)}/unregister", params={"email": email})
    assert unregister.status_code == 200
    assert "Unregistered" in unregister.json().get("message", "")
