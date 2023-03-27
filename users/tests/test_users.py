from fastapi.testclient import TestClient
from main import app
from queries.users import UserQueries
from models import UserIn, UserOut
from authenticator import authenticator

client = TestClient(app)

# Arrange - create request / expected response objects
expected_user = UserOut(
    id=1,
    email="email@email.com",
    pickup_name="pickup_name",
    phone_number="phone_number",
    venmo="venmo",
    hashed_password="hashed_password"
)

cookies = {authenticator.cookie_name: "some_token"}

# Mock the UserQueries class
class MockUserQueries:
    def get(self, email: str) -> UserOut:
        return expected_user

    def get_all(self) -> list[UserOut]:
        return [expected_user]

# Act and Assert
def test_get_users():
    app.dependency_overrides[UserQueries] = MockUserQueries
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.json() == [expected_user.dict()]
    # Cleanup
    app.dependency_overrides = {}

def test_get_token():
    app.dependency_overrides[
        authenticator.try_get_current_account_data
    ] = lambda: expected_user
    response = client.get("/token", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {
        "access_token": cookies[authenticator.cookie_name],
        "token_type": "Bearer",
        "user": expected_user.dict()
    }
    # Cleanup
    app.dependency_overrides = {}
