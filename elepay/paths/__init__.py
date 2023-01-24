# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from elepay.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CHARGES = "/charges"
    CHARGES_ID = "/charges/{id}"
    CHARGES_ID_REVOKE = "/charges/{id}/revoke"
    CHARGES_ID_CAPTURE = "/charges/{id}/capture"
    CHARGES_ID_STATUS = "/charges/{id}/status"
    CHARGES_ID_REFUNDS = "/charges/{id}/refunds"
    CHARGES_ID_REFUNDS_REFUND_ID = "/charges/{id}/refunds/{refundId}"
    CUSTOMERS = "/customers"
    CUSTOMERS_CUSTOMER_ID = "/customers/{customerId}"
    CUSTOMERS_CUSTOMER_ID_SOURCES = "/customers/{customerId}/sources"
    CUSTOMERS_CUSTOMER_ID_SOURCES_SOURCE_ID = "/customers/{customerId}/sources/{sourceId}"
    SOURCES_SOURCE_ID_STATUS = "/sources/{sourceId}/status"
    PAYMENTMETHODS = "/payment-methods"
    CODES = "/codes"
    CODES_CODE_ID = "/codes/{codeId}"
    CODESETTING_PAYMENTMETHODS = "/code-setting/payment-methods"
    INVOICES = "/invoices"
    INVOICES_INVOICE_ID = "/invoices/{invoiceId}"
    INVOICES_INVOICE_ID_CANCEL = "/invoices/{invoiceId}/cancel"
    INVOICES_INVOICE_ID_SUBMIT = "/invoices/{invoiceId}/submit"
    INVOICES_INVOICE_ID_SEND = "/invoices/{invoiceId}/send"
    TERMINAL_LOCATIONS = "/terminal/locations"
    TERMINAL_READERS = "/terminal/readers"
    TERMINAL_READERS_READER_ID = "/terminal/readers/{readerId}"
    DISPUTES = "/disputes"
    DISPUTES_ID = "/disputes/{id}"
    SUBSCRIPTIONS = "/subscriptions"
    SUBSCRIPTIONS_SUBSCRIPTION_ID = "/subscriptions/{subscriptionId}"
    SUBSCRIPTIONS_SUBSCRIPTION_ID_START = "/subscriptions/{subscriptionId}/start"
    SUBSCRIPTIONS_SUBSCRIPTION_ID_RESUME = "/subscriptions/{subscriptionId}/resume"
    SUBSCRIPTIONS_SUBSCRIPTION_ID_CANCEL = "/subscriptions/{subscriptionId}/cancel"
    SUBSCRIPTIONS_SUBSCRIPTION_ID_PERIODS = "/subscriptions/{subscriptionId}/periods"
