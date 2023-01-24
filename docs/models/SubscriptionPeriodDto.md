# elepay.model.subscription_period_dto.SubscriptionPeriodDto

定期課金周期情報オブジェクト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 定期課金周期情報オブジェクト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Subscription Period ID | [optional] 
**object** | str,  | str,  | 対象種類の表記 | [optional] if omitted the server will use the default value of "subscription_period"
**startTime** | decimal.Decimal, int,  | decimal.Decimal,  | 周期開始UTCタイムスタンプ | [optional] value must be a 64 bit integer
**endTime** | decimal.Decimal, int,  | decimal.Decimal,  | 周期終了UTCタイムスタンプ | [optional] value must be a 64 bit integer
**charge** | [**ChargeDto**](ChargeDto.md) | [**ChargeDto**](ChargeDto.md) |  | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

