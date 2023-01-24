# elepay.model.code_dto.CodeDto

EasyQRコードオブジェクト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EasyQRコードオブジェクト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | EasyQRコードID | [optional] 
**object** | str,  | str,  | 対象種類の表記 | [optional] if omitted the server will use the default value of "code"
**liveMode** | bool,  | BoolClass,  | 本番モードかどうか - false テストモード - true 本番モード  | [optional] 
**codeUrl** | str,  | str,  | EasyQRコードURL | [optional] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | 支払い金額 | [optional] 
**currency** | str,  | str,  | 通貨コード (ISO_4217) | [optional] if omitted the server will use the default value of "JPY"
**orderNo** | str,  | str,  | お客様システム側のオーダーNo、例えば注文番号、決済IDなど | [optional] 
**description** | str,  | str,  | 支払いオブジェクトの「決済に関する説明」 | [optional] 
**[extra](#extra)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払いエキストラデータ | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払いオブジェクトの「メタデータ」 | [optional] 
**status** | [**CodeStatusType**](CodeStatusType.md) | [**CodeStatusType**](CodeStatusType.md) |  | [optional] 
**charge** | [**ChargeDto**](ChargeDto.md) | [**ChargeDto**](ChargeDto.md) |  | [optional] 
**frontUrl** | str,  | str,  |  | [optional] 
**[items](#items)** | list, tuple,  | tuple,  |  | [optional] 
**expired** | bool,  | BoolClass,  | EasyQRコード有効有無 | [optional] 
**expiryTime** | decimal.Decimal, int,  | decimal.Decimal,  | EasyQRコード有効期限のUTCタイムスタンプ | [optional] value must be a 64 bit integer
**expiryPeriod** | decimal.Decimal, int,  | decimal.Decimal,  | EasyQRコード有効期限までの残りミリ秒数 | [optional] value must be a 64 bit integer
**createTime** | decimal.Decimal, int,  | decimal.Decimal,  | コード新規時間のUTCタイムスタンプ | [optional] value must be a 64 bit integer
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extra

支払いエキストラデータ

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払いエキストラデータ | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anyStringName** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# metadata

支払いオブジェクトの「メタデータ」

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払いオブジェクトの「メタデータ」 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anyStringName** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CodeItem**](CodeItem.md) | [**CodeItem**](CodeItem.md) | [**CodeItem**](CodeItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

