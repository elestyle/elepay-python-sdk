# elepay.model.charge_req.ChargeReq

支払リクエスト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払リクエスト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | 金額 | 
**orderNo** | str,  | str,  | お客様側のシステムオーダーNo（例：注文番号、決済IDなど） 最大桁数は50桁です。  | 
**paymentMethod** | [**PaymentMethodType**](PaymentMethodType.md) | [**PaymentMethodType**](PaymentMethodType.md) |  | 
**capture** | bool,  | BoolClass,  | 支払い処理を確定するかどうか falseの場合、承認と支払い額の確保のみ行う。デフォルトはtrue  | [optional] if omitted the server will use the default value of True
**currency** | str,  | str,  | 通貨コード (ISO_4217) | [optional] if omitted the server will use the default value of "JPY"
**resource** | [**ResourceType**](ResourceType.md) | [**ResourceType**](ResourceType.md) |  | [optional] 
**description** | str,  | str,  | 決済に関する説明 | [optional] 
**[extra](#extra)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 決済に関する追加情報がある場合に利用します。具体的設定情報は「開発ガイド-&gt;決済Extra情報設定」を参照してください。 | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ キーバリューの任意データ。 キーは20個まで、バリューは255バイト以内の文字列。 「route」、「__」で始まる文字列は予約キー。  | [optional] 
**clientIp** | str,  | str,  | Client IP アドレス | [optional] 
**customerId** | str,  | str,  | カスタマID | [optional] 
**sourceId** | str,  | str,  | カスタマソースID | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extra

決済に関する追加情報がある場合に利用します。具体的設定情報は「開発ガイド->決済Extra情報設定」を参照してください。

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 決済に関する追加情報がある場合に利用します。具体的設定情報は「開発ガイド-&gt;決済Extra情報設定」を参照してください。 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anyStringName** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# metadata

メタデータ キーバリューの任意データ。 キーは20個まで、バリューは255バイト以内の文字列。 「route」、「__」で始まる文字列は予約キー。 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | メタデータ キーバリューの任意データ。 キーは20個まで、バリューは255バイト以内の文字列。 「route」、「__」で始まる文字列は予約キー。  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anyStringName** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

