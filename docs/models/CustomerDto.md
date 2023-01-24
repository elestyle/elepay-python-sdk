# elepay.model.customer_dto.CustomerDto

カスタマオブジェクト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | カスタマオブジェクト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Customer ID | [optional] 
**object** | str,  | str,  | 対象種類の表記 | [optional] if omitted the server will use the default value of "customer"
**liveMode** | bool,  | BoolClass,  | 本番モードかどうか - false テストモード - true 本番モード  | [optional] 
**defaultSource** | str,  | str,  | デフォルトカスタマソースID | [optional] 
**name** | str,  | str,  | 名前 | [optional] 
**description** | str,  | str,  | カスタマに関する説明 | [optional] 
**email** | str,  | str,  | メールアドレス | [optional] 
**phone** | str,  | str,  | 電話番号 | [optional] 
**remark** | str,  | str,  | 備考 | [optional] 
**operator** | str,  | str,  | 操作者 | [optional] 
**status** | [**CustomerStatusType**](CustomerStatusType.md) | [**CustomerStatusType**](CustomerStatusType.md) |  | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ | [optional] 
**updateTime** | decimal.Decimal, int,  | decimal.Decimal,  | update time | [optional] value must be a 64 bit integer
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

