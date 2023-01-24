<a name="__pageTop"></a>
# elepay.apis.tags.code_setting_api.CodeSettingApi

All URIs are relative to *https://api.elepay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_code_payment_methods**](#list_code_payment_methods) | **get** /code-setting/payment-methods | List all enabled EasyQR payment methods

# **list_code_payment_methods**
<a name="list_code_payment_methods"></a>
> CodePaymentMethodResponse list_code_payment_methods()

List all enabled EasyQR payment methods

EasyQR利用できる決済方法を取得します。

### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_code_payment_methods.ApiResponseFor200) | EasyQR利用できる決済方法リスト

#### list_code_payment_methods.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**CodePaymentMethodResponse**](../../models/CodePaymentMethodResponse.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

