# elepay.model.charge_dto.ChargeDto

支払いオブジェクト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払いオブジェクト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Charge ID | [optional] 
**appId** | str,  | str,  | App ID | [optional] 
**object** | str,  | str,  | 対象種類の表記 | [optional] if omitted the server will use the default value of "charge"
**liveMode** | bool,  | BoolClass,  | 本番モードかどうか - false テストモード - true 本番モード  | [optional] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | 支払い金額 | [optional] 
**authorizeAmount** | decimal.Decimal, int,  | decimal.Decimal,  | 事前承認金額 | [optional] 
**currency** | str,  | str,  | 通貨コード (ISO_4217) | [optional] if omitted the server will use the default value of "JPY"
**authorize** | bool,  | BoolClass,  | 事前承認フラグ | [optional] 
**paymentMethod** | [**PaymentMethodType**](PaymentMethodType.md) | [**PaymentMethodType**](PaymentMethodType.md) |  | [optional] 
**resource** | [**ResourceType**](ResourceType.md) | [**ResourceType**](ResourceType.md) |  | [optional] 
**orderNo** | str,  | str,  | お客様システム側のオーダーNo、例えば注文番号、決済IDなど | [optional] 
**description** | str,  | str,  | 支払い説明文 | [optional] 
**[extra](#extra)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払いエキストラデータ | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払いメタデータ | [optional] 
**cardInfo** | [**CardInfo**](CardInfo.md) | [**CardInfo**](CardInfo.md) |  | [optional] 
**voucherNo** | str,  | str,  | プロバイダー決済伝票番号 | [optional] 
**clientIp** | str,  | str,  | Client IP アドレス | [optional] 
**paid** | bool,  | BoolClass,  | 支払い済みフラグ | [optional] 
**refunded** | bool,  | BoolClass,  | 返金済みフラグ | [optional] 
**disputed** | bool,  | BoolClass,  | 不審請求フラグ | [optional] 
**refunds** | [**RefundsDto**](RefundsDto.md) | [**RefundsDto**](RefundsDto.md) |  | [optional] 
**status** | [**ChargeStatusType**](ChargeStatusType.md) | [**ChargeStatusType**](ChargeStatusType.md) |  | [optional] 
**codeContent** | str,  | str,  | 店舗側提示型QRコード(リソースはmpm場合のみ) | [optional] 
**credential** | str,  | str,  | Client SDKの認証情報 | [optional] 
**paidTime** | decimal.Decimal, int,  | decimal.Decimal,  | 支払い時間のUTCタイムスタンプ | [optional] value must be a 64 bit integer
**refundTime** | decimal.Decimal, int,  | decimal.Decimal,  | 返金時間のUTCタイムスタンプ | [optional] value must be a 64 bit integer
**expiryTime** | decimal.Decimal, int,  | decimal.Decimal,  | 支払い請求有効時間のUTCタイムスタンプ | [optional] value must be a 64 bit integer
**settleTime** | decimal.Decimal, int,  | decimal.Decimal,  | 支払い締め時間のUTCタイムスタンプ | [optional] value must be a 64 bit integer
**createTime** | decimal.Decimal, int,  | decimal.Decimal,  | 支払い新規時間のUTCタイムスタンプ | [optional] value must be a 64 bit integer
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

支払いメタデータ

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払いメタデータ | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anyStringName** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

