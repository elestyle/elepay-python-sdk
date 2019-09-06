# elepay-api
elepay APIはRESTをベースに構成された決済APIです。支払い処理、返金処理など、決済に関わる運用における様々なことができます。 

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/elestyle/elepay-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/elestyle/elepay-python-sdk.git`)

Then import the package:
```python
import elepay_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import elepay_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import elepay_api
from elepay_api.rest import ApiException
from pprint import pprint

configuration = elepay_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.elepay.io
configuration.host = "https://api.elepay.io"
# Create an instance of the API class
api_instance = elepay_api.ChargeApi(elepay_api.ApiClient(configuration))
charge = elepay_api.ChargeReq() # ChargeReq | 支払リクエスト

try:
    # Create charge
    api_response = api_instance.create_charge(charge)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargeApi->create_charge: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.elepay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChargeApi* | [**create_charge**](docs/ChargeApi.md#create_charge) | **POST** /charges | Create charge
*ChargeApi* | [**list_charges**](docs/ChargeApi.md#list_charges) | **GET** /charges | List charges
*ChargeApi* | [**retrieve_charge**](docs/ChargeApi.md#retrieve_charge) | **GET** /charges/{id} | Retrieve charge
*ChargeApi* | [**revoke_charge**](docs/ChargeApi.md#revoke_charge) | **DELETE** /charges/{id} | revoke charge
*RefundApi* | [**create_refund**](docs/RefundApi.md#create_refund) | **POST** /charges/{id}/refunds | Create refund
*RefundApi* | [**list_charges_refunds**](docs/RefundApi.md#list_charges_refunds) | **GET** /charges/{id}/refunds | List refunds
*RefundApi* | [**list_refunds**](docs/RefundApi.md#list_refunds) | **GET** /refunds | List refunds
*RefundApi* | [**retrieve_charge_refund**](docs/RefundApi.md#retrieve_charge_refund) | **GET** /charges/{id}/refunds/{refundId} | Retrieve refund
*RefundApi* | [**retrieve_refund**](docs/RefundApi.md#retrieve_refund) | **GET** /refunds/{refundId} | Retrieve refund


## Documentation For Models

 - [BadRequestError](docs/BadRequestError.md)
 - [ChargeDateTimeType](docs/ChargeDateTimeType.md)
 - [ChargeDto](docs/ChargeDto.md)
 - [ChargeReq](docs/ChargeReq.md)
 - [ChargesResponse](docs/ChargesResponse.md)
 - [ElepayError](docs/ElepayError.md)
 - [ElepayRestError](docs/ElepayRestError.md)
 - [InternalServerError](docs/InternalServerError.md)
 - [PaymentMethodType](docs/PaymentMethodType.md)
 - [RefundDto](docs/RefundDto.md)
 - [RefundExtDto](docs/RefundExtDto.md)
 - [RefundReq](docs/RefundReq.md)
 - [RefundsResponse](docs/RefundsResponse.md)


## Documentation For Authorization


## BasicAuth

- **Type**: HTTP basic authentication


## Author




