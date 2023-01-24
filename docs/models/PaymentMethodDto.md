# elepay.model.payment_method_dto.PaymentMethodDto

決済方法詳細情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 決済方法詳細情報 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**paymentMethod** | [**PaymentMethodType**](PaymentMethodType.md) | [**PaymentMethodType**](PaymentMethodType.md) |  | [optional] 
**[resources](#resources)** | list, tuple,  | tuple,  |  | [optional] 
**[brand](#brand)** | list, tuple,  | tuple,  | クレジットカードの場合、利用できるクレジットカードブランド | [optional] 
**ua** | str,  | str,  | 利用できるブラウザのUserAgent | [optional] 
**channelProperties** | [**ChannelPropertiesDto**](ChannelPropertiesDto.md) | [**ChannelPropertiesDto**](ChannelPropertiesDto.md) |  | [optional] 
**customerProperties** | [**CustomerPropertiesDto**](CustomerPropertiesDto.md) | [**CustomerPropertiesDto**](CustomerPropertiesDto.md) |  | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# resources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceType**](ResourceType.md) | [**ResourceType**](ResourceType.md) | [**ResourceType**](ResourceType.md) |  | 

# brand

クレジットカードの場合、利用できるクレジットカードブランド

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | クレジットカードの場合、利用できるクレジットカードブランド | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | クレジットカードブランド | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

