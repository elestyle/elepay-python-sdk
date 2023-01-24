# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from elepay.paths.invoices import Api

from elepay.paths import PathValues

path = PathValues.INVOICES