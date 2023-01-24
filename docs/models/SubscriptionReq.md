# elepay.model.subscription_req.SubscriptionReq

定期課金作成リクエスト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 定期課金作成リクエスト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**customerId** | str,  | str,  | カスタマID | 
**name** | str,  | str,  | 定期課金名 | [optional] 
**currency** | str,  | str,  | 通貨コード (ISO_4217) | [optional] if omitted the server will use the default value of "JPY"
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | 每期課金金額 | [optional] 
**interval** | [**SubscriptionIntervalType**](SubscriptionIntervalType.md) | [**SubscriptionIntervalType**](SubscriptionIntervalType.md) |  | [optional] 
**initialAmount** | decimal.Decimal, int,  | decimal.Decimal,  | 初回支払い前の固定支払額 | [optional] 
**firstChargeTime** | decimal.Decimal, int,  | decimal.Decimal,  | 初回支払いUTCタイムスタンプ | [optional] value must be a 64 bit integer
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ | [optional] 
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

