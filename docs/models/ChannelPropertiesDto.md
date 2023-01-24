# elepay.model.channel_properties_dto.ChannelPropertiesDto

決済方法関する情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 決済方法関する情報 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**isSupportRefund** | bool,  | BoolClass,  | 返金 true 利用可能 false 利用不可 | [optional] 
**isSupportPartialRefund** | bool,  | BoolClass,  | 一部返金 true 利用可能 false 利用不可 | [optional] 
**isSupportMultipleRefund** | bool,  | BoolClass,  | 複数回返金 true 利用可能 false 一回のみ | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

