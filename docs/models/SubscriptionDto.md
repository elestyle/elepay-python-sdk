# elepay.model.subscription_dto.SubscriptionDto

定期課金オブジェクト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 定期課金オブジェクト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Subscription ID | [optional] 
**appId** | str,  | str,  | App ID | [optional] 
**object** | str,  | str,  | 対象種類の表記 | [optional] if omitted the server will use the default value of "subscription"
**liveMode** | bool,  | BoolClass,  | 本番モードかどうか - false テストモード - true 本番モード  | [optional] 
**customerId** | str,  | str,  | Customer ID | [optional] 
**customer** | [**CustomerDto**](CustomerDto.md) | [**CustomerDto**](CustomerDto.md) |  | [optional] 
**nextChargeTime** | decimal.Decimal, int,  | decimal.Decimal,  | 次定期課金周期開始UTCタイムスタンプ | [optional] value must be a 64 bit integer
**isCharging** | bool,  | BoolClass,  | 処理中かどうか | [optional] 
**chargedPeriods** | decimal.Decimal, int,  | decimal.Decimal,  | 成功した定期課金回数 | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ | [optional] 
**status** | [**SubscriptionStatusType**](SubscriptionStatusType.md) | [**SubscriptionStatusType**](SubscriptionStatusType.md) |  | [optional] 
**createTime** | decimal.Decimal, int,  | decimal.Decimal,  | 作成UTCタイムスタンプ | [optional] value must be a 64 bit integer
**updateTime** | decimal.Decimal, int,  | decimal.Decimal,  | 更新UTCタイムスタンプ | [optional] value must be a 64 bit integer
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

