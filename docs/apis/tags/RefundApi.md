<a name="__pageTop"></a>
# elepay.apis.tags.refund_api.RefundApi

All URIs are relative to *https://api.elepay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_refund**](#create_refund) | **post** /charges/{id}/refunds | Create refund
[**list_charges_refunds**](#list_charges_refunds) | **get** /charges/{id}/refunds | List refunds
[**retrieve_charge_refund**](#retrieve_charge_refund) | **get** /charges/{id}/refunds/{refundId} | Retrieve refund

# **create_refund**
<a name="create_refund"></a>
> RefundDto create_refund(idrefund_req)

Create refund

決済の全額あるいは一部の返金処理を行います。

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsoncharsetutf8] | required |
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
[**RefundReq**](../../models/RefundReq.md) |  | 


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
201 | [ApiResponseFor201](#create_refund.ApiResponseFor201) | Created

#### create_refund.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**RefundDto**](../../models/RefundDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_charges_refunds**
<a name="list_charges_refunds"></a>
> RefundsResponse list_charges_refunds(id)

List refunds

返金に関する情報を一覧で取得します。

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
200 | [ApiResponseFor200](#list_charges_refunds.ApiResponseFor200) | OK

#### list_charges_refunds.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**RefundsResponse**](../../models/RefundsResponse.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_charge_refund**
<a name="retrieve_charge_refund"></a>
> RefundDto retrieve_charge_refund(idrefund_id)

Retrieve refund

返金に関する詳細情報を取得します。

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
refundId | RefundIdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RefundIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_charge_refund.ApiResponseFor200) | OK

#### retrieve_charge_refund.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**RefundDto**](../../models/RefundDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

