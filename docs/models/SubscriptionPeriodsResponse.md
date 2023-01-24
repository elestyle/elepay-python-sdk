# elepay.model.subscription_periods_response.SubscriptionPeriodsResponse

定期課金周期情報リスト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 定期課金周期情報リスト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | decimal.Decimal, int,  | decimal.Decimal,  | 件数 | [optional] 
**[periods](#periods)** | list, tuple,  | tuple,  | 定期課金周期詳細情報 | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# periods

定期課金周期詳細情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 定期課金周期詳細情報 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SubscriptionPeriodDto**](SubscriptionPeriodDto.md) | [**SubscriptionPeriodDto**](SubscriptionPeriodDto.md) | [**SubscriptionPeriodDto**](SubscriptionPeriodDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

