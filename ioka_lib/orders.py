from dotenv import load_dotenv
from base import BaseAPI
load_dotenv()

class Orders(BaseAPI):

    def get_orders(self):
        return self._send_request("GET", "orders")

    def get_order(self, order_id):
        return self._send_request("GET", f"orders/{order_id}")

    def get_order_events(self, order_id):
        return self._send_request("GET", f"orders/{order_id}/events")

    def get_refunds(self, order_id):
        return self._send_request("GET", f"orders/{order_id}/refunds")

    def get_refund_by_id(self, order_id, refund_id):
        return self._send_request("GET", f"orders/{order_id}/refunds/{refund_id}")

    def create_order(self, amount, currency, capture_method):
        if not isinstance(amount, (int, float)) or amount < 100:
            raise ValueError("Amount must be >= 100")
        if not isinstance(currency, str) or len(currency) != 3:
            raise ValueError("Currency must be a 3-letter string")
        if capture_method not in ['AUTO', 'MANUAL']:
            raise ValueError("Capture method must be 'manual' or 'automatic'")

        order_data = {
            "amount": amount,
            "currency": currency,
            "capture_method": capture_method
        }
        return self._send_request("POST", "orders", data=order_data)

    def capture_order(self, order_id, amount):
        if not isinstance(amount, (int, float)) or amount < 100:
            raise ValueError("Amount must be >= 100")
        order_data = {
            "amount": amount,

        }
        return self._send_request("POST", f"orders/{order_id}/capture", data=order_data)

    def refund_order(self, order_id, amount):
        if not isinstance(amount, (int, float)) or amount < 100:
            raise ValueError("Amount must be >= 100")
        order_data = {
            "amount": amount
        }
        return self._send_request("POST", f"orders/{order_id}/refunds", data=order_data)

    def cancel_order(self, order_id, reason):
        if not isinstance(reason, str) or len(reason) > 255:
            raise ValueError("Reason must be a string of 255 characters or less")

        data = {
            "reason": reason
        }
        return self._send_request("POST", f"orders/{order_id}/cancel", data=data)

