from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model

#TestClient
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_order_details(db_session):
    #create order details
    order_details_data = {
        "order_id": "5",
        "sandwich_id": "2",
        "amount": "3"

    }

    order_details_object = model.Order(**order_details_data)

    #Create Function Call

    created_order_details = controller.create(db_session, order_details_object)


    #assertions

    assert created_order_details is not None
    assert created_order_details.order_id == "5"
    assert created_order_details.sandwich_id == "2"
    assert created_order_details.amount == "3"








