from django.test import TestCase
from core.views import create_order_and_items
from core.models import Order, OrderItem

class TransactionTestCase(TestCase):
    
    def test_create_order_and_items_success(self):
        order_data = {'customer_name': 'John Doe','total_price': 200.00}
        items_data = [
            {'product': 'Product 1', 'price': 100.00},
            {'product': 'Product 2', 'price': 50.00},
        ]
        create_order_and_items(order_data, items_data)
        
        # Check if order and items were created
        order = Order.objects.get(customer_name='John Doe')
        self.assertEqual(OrderItem.objects.filter(order=order).count(), 3)
    
    def test_create_order_and_items_failure(self):
        order_data = {'customer_name': 'Jane Doe', 'total_price': 250.00}
        items_data = [
            {'product': 'Product 1', 'price': 100.00},
            {'product': 'Product 2', 'price': 50.00},
        ]
        
        with self.assertRaises(Exception):
            create_order_and_items(order_data, items_data)
        
        # Check if no order or items were created
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(OrderItem.objects.count(), 0)
