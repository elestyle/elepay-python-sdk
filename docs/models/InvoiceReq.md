# elepay.model.invoice_req.InvoiceReq

インボイスリクエスト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | インボイスリクエスト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**memo** | str,  | str,  |  | [optional] 
**customerId** | str,  | str,  | カスタマID | [optional] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | payment amount | [optional] 
**currency** | str,  | str,  | currency code | [optional] if omitted the server will use the default value of "JPY"
**expiryTime** | decimal.Decimal, int,  | decimal.Decimal,  | expiry time | [optional] value must be a 64 bit integer
**[items](#items)** | list, tuple,  | tuple,  |  | [optional] 
**remark** | str,  | str,  | 備考 | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InvoiceItem**](InvoiceItem.md) | [**InvoiceItem**](InvoiceItem.md) | [**InvoiceItem**](InvoiceItem.md) |  | 

# metadata

メタデータ

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anyStringName** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

