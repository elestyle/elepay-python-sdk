# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from elepay.paths.code_setting_payment_methods import Api

from elepay.paths import PathValues

path = PathValues.CODESETTING_PAYMENTMETHODS