# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from elepay.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CHARGE = "Charge"
    REFUND = "Refund"
    CUSTOMER = "Customer"
    CODE = "Code"
    CODE_SETTING = "CodeSetting"
    PAYMENT_METHOD = "PaymentMethod"
    TERMINAL = "Terminal"
    INVOICE = "Invoice"
    DISPUTE = "Dispute"
    SUBSCRIPTION = "Subscription"
