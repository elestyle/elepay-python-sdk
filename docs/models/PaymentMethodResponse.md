# elepay.model.payment_method_response.PaymentMethodResponse

利用できる決済方法リスト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 利用できる決済方法リスト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | decimal.Decimal, int,  | decimal.Decimal,  | 件数 | [optional] 
**[paymentMethods](#paymentMethods)** | list, tuple,  | tuple,  | 決済方法詳細情報 | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# paymentMethods

決済方法詳細情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 決済方法詳細情報 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentMethodDto**](PaymentMethodDto.md) | [**PaymentMethodDto**](PaymentMethodDto.md) | [**PaymentMethodDto**](PaymentMethodDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

