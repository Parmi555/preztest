from django.test import TestCase
from prezola.models import Items, Orders

class EndpointTest(TestCase):
    def test_home_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_report_endpoint(self):
        response = self.client.get('/report')
        self.assertEqual(response.status_code, 200)


class ItemPurchaseTest_ReduceQuantity(TestCase):
    def test_item_purchase(self):
        item = Items.objects.create(name="test item", brand="Lovely", price="2.00GBP", in_stock_quantity=4)
        item.save()

        url = '/order/' + str(item.id)
        self.client.post(url, {'item_id' : item.id, 'quantity' : '1', 'buyer_name' : 'someone', 'address' : 'Flat 8, London'})

        item.refresh_from_db()

        self.assertEqual(item.in_stock_quantity, 3)
