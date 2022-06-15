import pytest
from django.urls import reverse
from .models import Ticket
from .serializers import TicketListSerializer


@pytest.mark.simple_db
def test_ticket(client):
    url = reverse('list_ticket')
    response = client.get(url)

    ticket = Ticket.objects.all()
    expected_data = TicketListSerializer(ticket, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data


def test_authorization(self):
    self.client.login(username="adsad", password="adsda")
    response = self.client.get(self.url)
    self.assertEqual(403, response.status_code)
