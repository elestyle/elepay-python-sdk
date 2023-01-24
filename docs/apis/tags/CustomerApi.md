<a name="__pageTop"></a>
# elepay.apis.tags.customer_api.CustomerApi

All URIs are relative to *https://api.elepay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](#create_customer) | **post** /customers | Create customer
[**create_source**](#create_source) | **post** /customers/{customerId}/sources | Create source
[**delete_customer**](#delete_customer) | **delete** /customers/{customerId} | Delete customer
[**delete_source**](#delete_source) | **delete** /customers/{customerId}/sources/{sourceId} | Delete source
[**list_customers**](#list_customers) | **get** /customers | List customers
[**list_sources**](#list_sources) | **get** /customers/{customerId}/sources | List sources by customer ID
[**retrieve_customer**](#retrieve_customer) | **get** /customers/{customerId} | Retrieve customer
[**retrieve_source**](#retrieve_source) | **get** /customers/{customerId}/sources/{sourceId} | Retrieve source
[**retrieve_source_status**](#retrieve_source_status) | **get** /sources/{sourceId}/status | Retrieve source&#x27;s status
[**update_customer**](#update_customer) | **post** /customers/{customerId} | Update customer

# **create_customer**
<a name="create_customer"></a>
> CustomerDto create_customer(customer_req)

Create customer

カスタマを作成します。

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
[**CustomerReq**](../../models/CustomerReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_customer.ApiResponseFor201) | Created

#### create_customer.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomerDto**](../../models/CustomerDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_source**
<a name="create_source"></a>
> SourceDto create_source(customer_idsource_req)

Create source

カスタマソースを作成します。

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
[**SourceReq**](../../models/SourceReq.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_source.ApiResponseFor201) | OK

#### create_source.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDto**](../../models/SourceDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_customer**
<a name="delete_customer"></a>
> delete_customer(customer_id)

Delete customer

カスタマを削除します

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_customer.ApiResponseFor204) | Deleted

#### delete_customer.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_source**
<a name="delete_source"></a>
> delete_source(customer_idsource_id)

Delete source

カスタマソースを削除します。

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 
sourceId | SourceIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_source.ApiResponseFor204) | Deleted

#### delete_source.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_customers**
<a name="list_customers"></a>
> CustomerResponse list_customers()

List customers

カスタマ情報を一覧で取得します。

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
keyword | KeywordSchema | | optional
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_customers.ApiResponseFor200) | OK

#### list_customers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomerResponse**](../../models/CustomerResponse.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_sources**
<a name="list_sources"></a>
> SourceResponse list_sources(customer_id)

List sources by customer ID

カスタマソース情報を一覧で取得します。

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
paymentMethod | PaymentMethodSchema | | optional


# PaymentMethodSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**PaymentMethodType**](../../models/PaymentMethodType.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_sources.ApiResponseFor200) | OK

#### list_sources.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceResponse**](../../models/SourceResponse.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_customer**
<a name="retrieve_customer"></a>
> CustomerDto retrieve_customer(customer_id)

Retrieve customer

カスタマ情報を取得します。

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
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_customer.ApiResponseFor200) | OK

#### retrieve_customer.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomerDto**](../../models/CustomerDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_source**
<a name="retrieve_source"></a>
> SourceDto retrieve_source(customer_idsource_id)

Retrieve source

カスタマ情報を取得します。

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
customerId | CustomerIdSchema | | 
sourceId | SourceIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_source.ApiResponseFor200) | OK

#### retrieve_source.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDto**](../../models/SourceDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_source_status**
<a name="retrieve_source_status"></a>
> SourceStatusDto retrieve_source_status(source_id)

Retrieve source's status

カスタマソースのステータスに関する詳細情報を取得します。

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
sourceId | SourceIdSchema | | 

# SourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_source_status.ApiResponseFor200) | OK

#### retrieve_source_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceStatusDto**](../../models/SourceStatusDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_customer**
<a name="update_customer"></a>
> CustomerDto update_customer(customer_idcustomer_req)

Update customer

カスタマを更新します。

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
[**CustomerReq**](../../models/CustomerReq.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_customer.ApiResponseFor200) | OK

#### update_customer.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomerDto**](../../models/CustomerDto.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

