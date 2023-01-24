# elepay.model.refund_dto.RefundDto

返金オブジェクト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 返金オブジェクト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Refund ID | [optional] 
**object** | str,  | str,  | 対象種類の表記 | [optional] if omitted the server will use the default value of "refund"
**chargeId** | str,  | str,  | Charge ID | [optional] 
**liveMode** | bool,  | BoolClass,  | 本番モードかどうか - false テストモード - true 本番モード  | [optional] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | 返金金額。全額返金、及び amount を指定することで金額の部分返金を行うことができます。 | [optional] 
**currency** | str,  | str,  | 通貨コード (ISO_4217) | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 返金メタデータ | [optional] 
**reason** | str,  | str,  | 返金理由 | [optional] 
**status** | [**RefundStatusType**](RefundStatusType.md) | [**RefundStatusType**](RefundStatusType.md) |  | [optional] 
**refundedTime** | decimal.Decimal, int,  | decimal.Decimal,  | 返金を行う時間のUTCタイムスタンプ。 | [optional] value must be a 64 bit integer
**createTime** | decimal.Decimal, int,  | decimal.Decimal,  | 返金新規時間のUTCタイムスタンプ。 | [optional] value must be a 64 bit integer
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

返金メタデータ

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 返金メタデータ | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anyStringName** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

