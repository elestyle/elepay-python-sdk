# elepay.model.invoice_dto.InvoiceDto

インボイスオブジェクト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | インボイスオブジェクト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Invoice ID | [optional] 
**object** | str,  | str,  | 対象種類の表記 | [optional] if omitted the server will use the default value of "invoice"
**liveMode** | bool,  | BoolClass,  | 本番モードかどうか - false テストモード - true 本番モード  | [optional] 
**customer** | [**CustomerDto**](CustomerDto.md) | [**CustomerDto**](CustomerDto.md) |  | [optional] 
**invoiceNo** | str,  | str,  | Invoice Number | [optional] 
**name** | str,  | str,  |  | [optional] 
**memo** | str,  | str,  |  | [optional] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | payment amount | [optional] 
**currency** | str,  | str,  | currency code | [optional] if omitted the server will use the default value of "JPY"
**status** | [**InvoiceStatusType**](InvoiceStatusType.md) | [**InvoiceStatusType**](InvoiceStatusType.md) |  | [optional] 
**operator** | str,  | str,  | 操作者 | [optional] 
**sendTime** | decimal.Decimal, int,  | decimal.Decimal,  | create time | [optional] value must be a 64 bit integer
**paidTime** | decimal.Decimal, int,  | decimal.Decimal,  | paid time | [optional] value must be a 64 bit integer
**expiryTime** | decimal.Decimal, int,  | decimal.Decimal,  | expiry time | [optional] value must be a 64 bit integer
**createTime** | decimal.Decimal, int,  | decimal.Decimal,  | create time | [optional] value must be a 64 bit integer
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

