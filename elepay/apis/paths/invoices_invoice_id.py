from elepay.paths.invoices_invoice_id.get import ApiForget
from elepay.paths.invoices_invoice_id.post import ApiForpost
from elepay.paths.invoices_invoice_id.delete import ApiFordelete


class InvoicesInvoiceId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
