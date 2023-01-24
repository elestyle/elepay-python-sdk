<a name="__pageTop"></a>
# elepay.apis.tags.payment_method_api.PaymentMethodApi

All URIs are relative to *https://api.elepay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_payment_methods**](#list_payment_methods) | **get** /payment-methods | List supported payment methods

# **list_payment_methods**
<a name="list_payment_methods"></a>
> PaymentMethodResponse list_payment_methods()

List supported payment methods

利用できる決済方法を取得します。

### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_payment_methods.ApiResponseFor200) | OK

#### list_payment_methods.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**PaymentMethodResponse**](../../models/PaymentMethodResponse.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

