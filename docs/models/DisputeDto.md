# elepay.model.dispute_dto.DisputeDto

不審請求オブジェクト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 不審請求オブジェクト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Dispute ID | [optional] 
**object** | str,  | str,  | 対象種類の表記 | [optional] if omitted the server will use the default value of "dispute"
**chargeId** | str,  | str,  | Charge ID | [optional] 
**liveMode** | bool,  | BoolClass,  | 本番モードかどうか - false テストモード - true 本番モード  | [optional] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | 不審請求金額 | [optional] 
**currency** | str,  | str,  | 通貨コード (ISO_4217) | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ | [optional] 
**reason** | str,  | str,  | 不審請求理由 | [optional] 
**status** | [**DisputeStatusType**](DisputeStatusType.md) | [**DisputeStatusType**](DisputeStatusType.md) |  | [optional] 
**resolvedTime** | decimal.Decimal, int,  | decimal.Decimal,  | 対応時間のUTCタイムスタンプ | [optional] value must be a 64 bit integer
**createTime** | decimal.Decimal, int,  | decimal.Decimal,  | 発生時間のUTCタイムスタンプ。 | [optional] value must be a 64 bit integer
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

