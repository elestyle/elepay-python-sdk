from elepay.paths.customers_customer_id.get import ApiForget
from elepay.paths.customers_customer_id.post import ApiForpost
from elepay.paths.customers_customer_id.delete import ApiFordelete


class CustomersCustomerId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
