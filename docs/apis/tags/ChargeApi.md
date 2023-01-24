<a name="__pageTop"></a>
# elepay.apis.tags.charge_api.ChargeApi

All URIs are relative to *https://api.elepay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capture_charge**](#capture_charge) | **post** /charges/{id}/capture | Capture charge
[**create_charge**](#create_charge) | **post** /charges | Create charge
[**list_charges**](#list_charges) | **get** /charges | List charges
[**retrieve_charge**](#retrieve_charge) | **get** /charges/{id} | Retrieve charge
[**retrieve_charge_status**](#retrieve_charge_status) | **get** /charges/{id}/status | Retrieve charge&#x27;s status
[**revoke_charge**](#revoke_charge) | **post** /charges/{id}/revoke | Revoke charge

# **capture_charge**
<a name="capture_charge"></a>
> ChargeDto capture_charge(id)

Capture charge

決済を確定します。

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsoncharsetutf8, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json;charset&#x3D;utf-8' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeCaptureReq**](../../models/ChargeCaptureReq.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#capture_charge.ApiResponseFor200) | OK

#### capture_charge.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeDto**](../../models/ChargeDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_charge**
<a name="create_charge"></a>
> ChargeDto create_charge(charge_req)

Create charge

決済処理を行います。

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsoncharsetutf8] | required |
content_type | str | optional, default is 'application/json;charset&#x3D;utf-8' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeReq**](../../models/ChargeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_charge.ApiResponseFor201) | Created

#### create_charge.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeDto**](../../models/ChargeDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_charges**
<a name="list_charges"></a>
> ChargesResponse list_charges()

List charges

決済に関する情報を一覧で取得します。

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
paymentMethod | PaymentMethodSchema | | optional
from | ModelFromSchema | | optional
to | ToSchema | | optional
dateField | DateFieldSchema | | optional
status | StatusSchema | | optional
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
sort | SortSchema | | optional
order | OrderSchema | | optional


# PaymentMethodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentMethodType**]({{complexTypePrefix}}PaymentMethodType.md) | [**PaymentMethodType**]({{complexTypePrefix}}PaymentMethodType.md) | [**PaymentMethodType**]({{complexTypePrefix}}PaymentMethodType.md) |  | 

# ModelFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# ToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# DateFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeDateTimeType**](../../models/ChargeDateTimeType.md) |  | 


# StatusSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeStatusType**](../../models/ChargeStatusType.md) |  | 


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# SortSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeDateTimeType**](../../models/ChargeDateTimeType.md) |  | 


# OrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**SortOrderType**](../../models/SortOrderType.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_charges.ApiResponseFor200) | OK

#### list_charges.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargesResponse**](../../models/ChargesResponse.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_charge**
<a name="retrieve_charge"></a>
> ChargeDto retrieve_charge(id)

Retrieve charge

決済に関する詳細情報を取得します。

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_charge.ApiResponseFor200) | OK

#### retrieve_charge.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeDto**](../../models/ChargeDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_charge_status**
<a name="retrieve_charge_status"></a>
> ChargeStatusDto retrieve_charge_status(id)

Retrieve charge's status

決済のステータスに関する詳細情報を取得します。

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_charge_status.ApiResponseFor200) | OK

#### retrieve_charge_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeStatusDto**](../../models/ChargeStatusDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **revoke_charge**
<a name="revoke_charge"></a>
> ChargeDto revoke_charge(id)

Revoke charge

決済を取消します。

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#revoke_charge.ApiResponseFor200) | OK

#### revoke_charge.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**ChargeDto**](../../models/ChargeDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

