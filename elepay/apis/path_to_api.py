import typing_extensions

from elepay.paths import PathValues
from elepay.apis.paths.charges import Charges
from elepay.apis.paths.charges_id import ChargesId
from elepay.apis.paths.charges_id_revoke import ChargesIdRevoke
from elepay.apis.paths.charges_id_capture import ChargesIdCapture
from elepay.apis.paths.charges_id_status import ChargesIdStatus
from elepay.apis.paths.charges_id_refunds import ChargesIdRefunds
from elepay.apis.paths.charges_id_refunds_refund_id import ChargesIdRefundsRefundId
from elepay.apis.paths.customers import Customers
from elepay.apis.paths.customers_customer_id import CustomersCustomerId
from elepay.apis.paths.customers_customer_id_sources import CustomersCustomerIdSources
from elepay.apis.paths.customers_customer_id_sources_source_id import CustomersCustomerIdSourcesSourceId
from elepay.apis.paths.sources_source_id_status import SourcesSourceIdStatus
from elepay.apis.paths.payment_methods import PaymentMethods
from elepay.apis.paths.codes import Codes
from elepay.apis.paths.codes_code_id import CodesCodeId
from elepay.apis.paths.code_setting_payment_methods import CodeSettingPaymentMethods
from elepay.apis.paths.invoices import Invoices
from elepay.apis.paths.invoices_invoice_id import InvoicesInvoiceId
from elepay.apis.paths.invoices_invoice_id_cancel import InvoicesInvoiceIdCancel
from elepay.apis.paths.invoices_invoice_id_submit import InvoicesInvoiceIdSubmit
from elepay.apis.paths.invoices_invoice_id_send import InvoicesInvoiceIdSend
from elepay.apis.paths.terminal_locations import TerminalLocations
from elepay.apis.paths.terminal_readers import TerminalReaders
from elepay.apis.paths.terminal_readers_reader_id import TerminalReadersReaderId
from elepay.apis.paths.disputes import Disputes
from elepay.apis.paths.disputes_id import DisputesId
from elepay.apis.paths.subscriptions import Subscriptions
from elepay.apis.paths.subscriptions_subscription_id import SubscriptionsSubscriptionId
from elepay.apis.paths.subscriptions_subscription_id_start import SubscriptionsSubscriptionIdStart
from elepay.apis.paths.subscriptions_subscription_id_resume import SubscriptionsSubscriptionIdResume
from elepay.apis.paths.subscriptions_subscription_id_cancel import SubscriptionsSubscriptionIdCancel
from elepay.apis.paths.subscriptions_subscription_id_periods import SubscriptionsSubscriptionIdPeriods

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CHARGES: Charges,
        PathValues.CHARGES_ID: ChargesId,
        PathValues.CHARGES_ID_REVOKE: ChargesIdRevoke,
        PathValues.CHARGES_ID_CAPTURE: ChargesIdCapture,
        PathValues.CHARGES_ID_STATUS: ChargesIdStatus,
        PathValues.CHARGES_ID_REFUNDS: ChargesIdRefunds,
        PathValues.CHARGES_ID_REFUNDS_REFUND_ID: ChargesIdRefundsRefundId,
        PathValues.CUSTOMERS: Customers,
        PathValues.CUSTOMERS_CUSTOMER_ID: CustomersCustomerId,
        PathValues.CUSTOMERS_CUSTOMER_ID_SOURCES: CustomersCustomerIdSources,
        PathValues.CUSTOMERS_CUSTOMER_ID_SOURCES_SOURCE_ID: CustomersCustomerIdSourcesSourceId,
        PathValues.SOURCES_SOURCE_ID_STATUS: SourcesSourceIdStatus,
        PathValues.PAYMENTMETHODS: PaymentMethods,
        PathValues.CODES: Codes,
        PathValues.CODES_CODE_ID: CodesCodeId,
        PathValues.CODESETTING_PAYMENTMETHODS: CodeSettingPaymentMethods,
        PathValues.INVOICES: Invoices,
        PathValues.INVOICES_INVOICE_ID: InvoicesInvoiceId,
        PathValues.INVOICES_INVOICE_ID_CANCEL: InvoicesInvoiceIdCancel,
        PathValues.INVOICES_INVOICE_ID_SUBMIT: InvoicesInvoiceIdSubmit,
        PathValues.INVOICES_INVOICE_ID_SEND: InvoicesInvoiceIdSend,
        PathValues.TERMINAL_LOCATIONS: TerminalLocations,
        PathValues.TERMINAL_READERS: TerminalReaders,
        PathValues.TERMINAL_READERS_READER_ID: TerminalReadersReaderId,
        PathValues.DISPUTES: Disputes,
        PathValues.DISPUTES_ID: DisputesId,
        PathValues.SUBSCRIPTIONS: Subscriptions,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID: SubscriptionsSubscriptionId,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_START: SubscriptionsSubscriptionIdStart,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_RESUME: SubscriptionsSubscriptionIdResume,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_CANCEL: SubscriptionsSubscriptionIdCancel,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_PERIODS: SubscriptionsSubscriptionIdPeriods,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CHARGES: Charges,
        PathValues.CHARGES_ID: ChargesId,
        PathValues.CHARGES_ID_REVOKE: ChargesIdRevoke,
        PathValues.CHARGES_ID_CAPTURE: ChargesIdCapture,
        PathValues.CHARGES_ID_STATUS: ChargesIdStatus,
        PathValues.CHARGES_ID_REFUNDS: ChargesIdRefunds,
        PathValues.CHARGES_ID_REFUNDS_REFUND_ID: ChargesIdRefundsRefundId,
        PathValues.CUSTOMERS: Customers,
        PathValues.CUSTOMERS_CUSTOMER_ID: CustomersCustomerId,
        PathValues.CUSTOMERS_CUSTOMER_ID_SOURCES: CustomersCustomerIdSources,
        PathValues.CUSTOMERS_CUSTOMER_ID_SOURCES_SOURCE_ID: CustomersCustomerIdSourcesSourceId,
        PathValues.SOURCES_SOURCE_ID_STATUS: SourcesSourceIdStatus,
        PathValues.PAYMENTMETHODS: PaymentMethods,
        PathValues.CODES: Codes,
        PathValues.CODES_CODE_ID: CodesCodeId,
        PathValues.CODESETTING_PAYMENTMETHODS: CodeSettingPaymentMethods,
        PathValues.INVOICES: Invoices,
        PathValues.INVOICES_INVOICE_ID: InvoicesInvoiceId,
        PathValues.INVOICES_INVOICE_ID_CANCEL: InvoicesInvoiceIdCancel,
        PathValues.INVOICES_INVOICE_ID_SUBMIT: InvoicesInvoiceIdSubmit,
        PathValues.INVOICES_INVOICE_ID_SEND: InvoicesInvoiceIdSend,
        PathValues.TERMINAL_LOCATIONS: TerminalLocations,
        PathValues.TERMINAL_READERS: TerminalReaders,
        PathValues.TERMINAL_READERS_READER_ID: TerminalReadersReaderId,
        PathValues.DISPUTES: Disputes,
        PathValues.DISPUTES_ID: DisputesId,
        PathValues.SUBSCRIPTIONS: Subscriptions,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID: SubscriptionsSubscriptionId,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_START: SubscriptionsSubscriptionIdStart,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_RESUME: SubscriptionsSubscriptionIdResume,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_CANCEL: SubscriptionsSubscriptionIdCancel,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_PERIODS: SubscriptionsSubscriptionIdPeriods,
    }
)
