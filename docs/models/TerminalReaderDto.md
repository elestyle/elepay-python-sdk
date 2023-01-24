# elepay.model.terminal_reader_dto.TerminalReaderDto

ターミナルリーダーオブジェクト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ターミナルリーダーオブジェクト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Reader ID | [optional] 
**appId** | str,  | str,  | App ID | [optional] 
**object** | str,  | str,  | 対象種類の表記 | [optional] if omitted the server will use the default value of "terminal.reader"
**liveMode** | bool,  | BoolClass,  | 本番モードかどうか - false テストモード - true 本番モード  | [optional] 
**locationId** | str,  | str,  | Location ID | [optional] 
**serialNumber** | str,  | str,  | シリアルナンバー | [optional] 
**registrationCode** | str,  | str,  | ペアリングコード | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ | [optional] 
**status** | [**ReaderStatusType**](ReaderStatusType.md) | [**ReaderStatusType**](ReaderStatusType.md) |  | [optional] 
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

