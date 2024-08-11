import pytest
from unittest.mock import patch, MagicMock
from http import HTTPStatus

from flask import Flask

from ugc_service.api.tracking import api
from ugc_service.services.tracking import EventService


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/tracking')
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def mock_event_service():
    return MagicMock(spec=EventService)


@pytest.mark.parametrize("event_data", [
    {
        "event_type": "click",
        "timestamp": "2024-08-11T12:00:00Z",
        "data": {"button_id": "submit"},
        "source": "web"
    },
    {
        "event_type": "page_view",
        "timestamp": "2024-08-11T12:05:00Z",
        "data": {"page_url": "/home"},
        "source": "web"
    }
])
def test_external_track_event_success(client, mock_event_service, event_data):
    with patch('services.tracking.get_event_service', return_value=mock_event_service):
        mock_event_service.track_event.return_value = {
            "user_id": "test_user_id",
            "event_type": event_data["event_type"],
            "timestamp": event_data["timestamp"],
            "data": event_data["data"],
            "source": event_data["source"]
        }

        headers = {
            'Authorization': 'Bearer test_jwt_token'
        }

        response = client.post('/tracking/external_track_event/', json=event_data, headers=headers)

        assert response.status_code == HTTPStatus.OK
        data = response.get_json()
        assert data['event_type'] == event_data["event_type"]
        assert data['timestamp'] == event_data["timestamp"]
        assert data['data'] == event_data["data"]
        assert data['source'] == event_data["source"]
