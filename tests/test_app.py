"""
Tests for the High School Management System API
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI application"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities data before each test"""
    # Store original state
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Team": {
            "description": "Join the school soccer team and compete in local tournaments",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["liam@mergington.edu", "noah@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Improve swimming techniques and participate in competitions",
            "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["ava@mergington.edu"]
        },
        "Theater Club": {
            "description": "Develop acting skills and participate in school productions",
            "schedule": "Thursdays, 3:30 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["isabella@mergington.edu", "mia@mergington.edu"]
        },
        "Art Studio": {
            "description": "Explore painting, drawing, and sculpture techniques",
            "schedule": "Wednesdays, 3:00 PM - 4:30 PM",
            "max_participants": 18,
            "participants": ["charlotte@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop critical thinking and public speaking skills through debates",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
        },
        "Science Club": {
            "description": "Conduct experiments and explore scientific concepts",
            "schedule": "Fridays, 3:00 PM - 4:30 PM",
            "max_participants": 15,
            "participants": ["lucas@mergington.edu"]
        }
    }
    
    # Reset activities to original state
    activities.clear()
    activities.update(original_activities)
    
    yield
    
    # Clean up after test
    activities.clear()
    activities.update(original_activities)


class TestRootEndpoint:
    """Tests for the root endpoint"""
    
    def test_root_redirects_to_static_index(self, client):
        """Test that root endpoint redirects to static index.html"""
        response = client.get("/", follow_redirects=False)
        assert response.status_code == 307
        assert response.headers["location"] == "/static/index.html"


class TestGetActivities:
    """Tests for GET /activities endpoint"""
    
    def test_get_all_activities(self, client):
        """Test retrieving all activities"""
        response = client.get("/activities")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) == 9
        assert "Chess Club" in data
        assert "Programming Class" in data
        assert "Soccer Team" in data
    
    def test_activities_have_required_fields(self, client):
        """Test that each activity has required fields"""
        response = client.get("/activities")
        data = response.json()
        
        for activity_name, activity_data in data.items():
            assert "description" in activity_data
            assert "schedule" in activity_data
            assert "max_participants" in activity_data
            assert "participants" in activity_data
            assert isinstance(activity_data["participants"], list)


class TestSignupForActivity:
    """Tests for POST /activities/{activity_name}/signup endpoint"""
    
    def test_signup_new_student_success(self, client):
        """Test successfully signing up a new student"""
        response = client.post(
            "/activities/Chess Club/signup?email=newstudent@mergington.edu"
        )
        assert response.status_code == 200
        assert response.json() == {
            "message": "Signed up newstudent@mergington.edu for Chess Club"
        }
        
        # Verify student was added
        activities_response = client.get("/activities")
        chess_club = activities_response.json()["Chess Club"]
        assert "newstudent@mergington.edu" in chess_club["participants"]
    
    def test_signup_duplicate_student_fails(self, client):
        """Test that signing up the same student twice fails"""
        email = "michael@mergington.edu"  # Already in Chess Club
        
        response = client.post(
            f"/activities/Chess Club/signup?email={email}"
        )
        assert response.status_code == 400
        assert response.json()["detail"] == "Student already signed up for this activity"
    
    def test_signup_nonexistent_activity_fails(self, client):
        """Test that signing up for a non-existent activity fails"""
        response = client.post(
            "/activities/Nonexistent Activity/signup?email=student@mergington.edu"
        )
        assert response.status_code == 404
        assert response.json()["detail"] == "Activity not found"
    
    def test_signup_multiple_students_to_same_activity(self, client):
        """Test signing up multiple students to the same activity"""
        emails = [
            "student1@mergington.edu",
            "student2@mergington.edu",
            "student3@mergington.edu"
        ]
        
        for email in emails:
            response = client.post(
                f"/activities/Art Studio/signup?email={email}"
            )
            assert response.status_code == 200
        
        # Verify all students were added
        activities_response = client.get("/activities")
        art_studio = activities_response.json()["Art Studio"]
        for email in emails:
            assert email in art_studio["participants"]


class TestCancelSignup:
    """Tests for DELETE /activities/{activity_name}/cancel endpoint"""
    
    def test_cancel_existing_signup_success(self, client):
        """Test successfully canceling an existing signup"""
        email = "michael@mergington.edu"  # Already in Chess Club
        
        response = client.delete(
            f"/activities/Chess Club/cancel?email={email}"
        )
        assert response.status_code == 200
        assert response.json() == {
            "message": f"Cancelled signup for {email} from Chess Club"
        }
        
        # Verify student was removed
        activities_response = client.get("/activities")
        chess_club = activities_response.json()["Chess Club"]
        assert email not in chess_club["participants"]
    
    def test_cancel_nonexistent_signup_fails(self, client):
        """Test that canceling a non-existent signup fails"""
        email = "nonexistent@mergington.edu"
        
        response = client.delete(
            f"/activities/Chess Club/cancel?email={email}"
        )
        assert response.status_code == 400
        assert response.json()["detail"] == "Student is not signed up for this activity"
    
    def test_cancel_from_nonexistent_activity_fails(self, client):
        """Test that canceling from a non-existent activity fails"""
        response = client.delete(
            "/activities/Nonexistent Activity/cancel?email=student@mergington.edu"
        )
        assert response.status_code == 404
        assert response.json()["detail"] == "Activity not found"
    
    def test_cancel_and_resign_up(self, client):
        """Test canceling and then signing up again"""
        email = "michael@mergington.edu"
        activity = "Chess Club"
        
        # Cancel signup
        cancel_response = client.delete(
            f"/activities/{activity}/cancel?email={email}"
        )
        assert cancel_response.status_code == 200
        
        # Sign up again
        signup_response = client.post(
            f"/activities/{activity}/signup?email={email}"
        )
        assert signup_response.status_code == 200
        
        # Verify student is signed up
        activities_response = client.get("/activities")
        chess_club = activities_response.json()[activity]
        assert email in chess_club["participants"]


class TestIntegrationScenarios:
    """Integration tests for complete user scenarios"""
    
    def test_student_joins_multiple_activities(self, client):
        """Test a student joining multiple activities"""
        email = "newstudent@mergington.edu"
        activities_to_join = ["Chess Club", "Programming Class", "Science Club"]
        
        for activity in activities_to_join:
            response = client.post(
                f"/activities/{activity}/signup?email={email}"
            )
            assert response.status_code == 200
        
        # Verify student is in all activities
        activities_response = client.get("/activities")
        all_activities = activities_response.json()
        
        for activity in activities_to_join:
            assert email in all_activities[activity]["participants"]
    
    def test_full_activity_lifecycle(self, client):
        """Test complete lifecycle: view activities, signup, cancel"""
        email = "lifecycle@mergington.edu"
        activity = "Swimming Club"
        
        # 1. View all activities
        view_response = client.get("/activities")
        assert view_response.status_code == 200
        assert activity in view_response.json()
        
        # 2. Sign up for activity
        signup_response = client.post(
            f"/activities/{activity}/signup?email={email}"
        )
        assert signup_response.status_code == 200
        
        # 3. Verify signup
        verify_response = client.get("/activities")
        assert email in verify_response.json()[activity]["participants"]
        
        # 4. Cancel signup
        cancel_response = client.delete(
            f"/activities/{activity}/cancel?email={email}"
        )
        assert cancel_response.status_code == 200
        
        # 5. Verify cancellation
        final_response = client.get("/activities")
        assert email not in final_response.json()[activity]["participants"]
