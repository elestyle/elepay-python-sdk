# elepay.model.refunds_dto.RefundsDto

返金のサマリー。複数回返金された場合、返金内容をサマリーして返します。

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 返金のサマリー。複数回返金された場合、返金内容をサマリーして返します。 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | 返金総額 | [optional] 
**totalCount** | decimal.Decimal, int,  | decimal.Decimal,  | 返金回数 | [optional] 
**[data](#data)** | list, tuple,  | tuple,  | 返金詳細情報 | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

返金詳細情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 返金詳細情報 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RefundDto**](RefundDto.md) | [**RefundDto**](RefundDto.md) | [**RefundDto**](RefundDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

