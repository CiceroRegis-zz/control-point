from django.db.models import Sum
import unittest
from appointment.models import Appointment


class ShowtotalPrice(unittest.TestCase):

    def test_show_total_price(self):
        appointments_price_total = \
            Appointment.objects.values('type_appointment__price').annotate(
                total=Sum('type_appointment__price'))

        print('precos', appointments_price_total)

        return
