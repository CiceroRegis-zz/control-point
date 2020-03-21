from django.db.models import Sum, Avg, Max, Count
import unittest
from appointment.models import Appointment


class ShowtotalPrice(unittest.TestCase):

    def test_show_total_price(self):
        appointments_price_total = Appointment.objects.values('type_appointment__price').annotate(
            Count('type_appointment__price')).annotate(total=Sum('type_appointment__price'))
        for app in appointments_price_total:
            print("preço total: ", app)
        return
