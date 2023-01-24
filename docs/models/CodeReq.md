# elepay.model.code_req.CodeReq

EasyQRコードリクエスト

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EasyQRコードリクエスト | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | 金額 | 
**orderNo** | str,  | str,  | お客様側のシステムオーダーNo（例：注文番号、決済IDなど） 最大桁数は50桁です。  | 
**currency** | str,  | str,  | 通貨コード (ISO_4217) | [optional] if omitted the server will use the default value of "JPY"
**description** | str,  | str,  | 支払いオブジェクトの「決済に関する説明」 | [optional] 
**[extra](#extra)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 決済に関する追加情報がある場合に利用します。具体的設定情報は「開発ガイド-&gt;決済Extra情報設定」を参照してください。 決済オブジェクトを作成する時、こちら設定したextra情報を優先利用します。  | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 支払いオブジェクトの「メタデータ」 | [optional] 
**expiryDuration** | decimal.Decimal, int,  | decimal.Decimal,  | EasyQRコード有効期限(分) 最小:3分、最大:30分、デフォルト:10分  | [optional] 
**frontUrl** | str,  | str,  | EasyCheckout決済が完了したあとの、戻り先ページのURL | [optional] 
**[items](#items)** | list, tuple,  | tuple,  | 商品に関する情報 | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extra

決済に関する追加情報がある場合に利用します。具体的設定情報は「開発ガイド->決済Extra情報設定」を参照してください。 決済オブジェクトを作成する時、こちら設定したextra情報を優先利用します。 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 決済に関する追加情報がある場合に利用します。具体的設定情報は「開発ガイド-&gt;決済Extra情報設定」を参照してください。 決済オブジェクトを作成する時、こちら設定したextra情報を優先利用します。  | 

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

商品に関する情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 商品に関する情報 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CodeItem**](CodeItem.md) | [**CodeItem**](CodeItem.md) | [**CodeItem**](CodeItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

