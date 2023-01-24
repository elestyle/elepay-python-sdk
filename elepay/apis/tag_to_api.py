import typing_extensions

from elepay.apis.tags import TagValues
from elepay.apis.tags.charge_api import ChargeApi
from elepay.apis.tags.refund_api import RefundApi
from elepay.apis.tags.customer_api import CustomerApi
from elepay.apis.tags.code_api import CodeApi
from elepay.apis.tags.code_setting_api import CodeSettingApi
from elepay.apis.tags.payment_method_api import PaymentMethodApi
from elepay.apis.tags.terminal_api import TerminalApi
from elepay.apis.tags.invoice_api import InvoiceApi
from elepay.apis.tags.dispute_api import DisputeApi
from elepay.apis.tags.subscription_api import SubscriptionApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CHARGE: ChargeApi,
        TagValues.REFUND: RefundApi,
        TagValues.CUSTOMER: CustomerApi,
        TagValues.CODE: CodeApi,
        TagValues.CODE_SETTING: CodeSettingApi,
        TagValues.PAYMENT_METHOD: PaymentMethodApi,
        TagValues.TERMINAL: TerminalApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.DISPUTE: DisputeApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CHARGE: ChargeApi,
        TagValues.REFUND: RefundApi,
        TagValues.CUSTOMER: CustomerApi,
        TagValues.CODE: CodeApi,
        TagValues.CODE_SETTING: CodeSettingApi,
        TagValues.PAYMENT_METHOD: PaymentMethodApi,
        TagValues.TERMINAL: TerminalApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.DISPUTE: DisputeApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
    }
)
