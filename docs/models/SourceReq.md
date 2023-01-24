# elepay.model.source_req.SourceReq

カスタマソースリクエスト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | カスタマソースリクエスト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**paymentMethod** | [**PaymentMethodType**](PaymentMethodType.md) | [**PaymentMethodType**](PaymentMethodType.md) |  | [optional] 
**resource** | [**ResourceType**](ResourceType.md) | [**ResourceType**](ResourceType.md) |  | [optional] 
**description** | str,  | str,  | カスタマソースに関する説明 | [optional] 
**[extra](#extra)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 決済に関する追加情報がある場合に利用します。具体的設定情報は「開発ガイド-&gt;ソースExtra情報設定」を参照してください。 | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extra

決済に関する追加情報がある場合に利用します。具体的設定情報は「開発ガイド->ソースExtra情報設定」を参照してください。

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 決済に関する追加情報がある場合に利用します。具体的設定情報は「開発ガイド-&gt;ソースExtra情報設定」を参照してください。 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anyStringName** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

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

