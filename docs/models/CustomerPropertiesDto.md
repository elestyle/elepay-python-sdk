# elepay.model.customer_properties_dto.CustomerPropertiesDto

決済方法カスタマ関する情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 決済方法カスタマ関する情報 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**isSupportCustomer** | bool,  | BoolClass,  | カスタマ機能 true 利用可能 false カスタマ利用不可 | [optional] 
**isSupportMultipleSource** | bool,  | BoolClass,  | 複数ソース true バインディング可能 false バインディング不可 | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

