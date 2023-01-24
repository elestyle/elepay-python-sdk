# elepay.model.card_info.CardInfo

カード情報やウォレット情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | カード情報やウォレット情報 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**brand** | [**CardBrandType**](CardBrandType.md) | [**CardBrandType**](CardBrandType.md) |  | [optional] 
**last4** | str,  | str,  | カード番号の下四桁 | [optional] 
**expMonth** | decimal.Decimal, int,  | decimal.Decimal,  | 有効期限月 | [optional] 
**expYear** | decimal.Decimal, int,  | decimal.Decimal,  | 有効期限年 | [optional] 
**name** | str,  | str,  | カード保有者名 | [optional] 
**wallet** | str,  | str,  | ウォレット情報 | [optional] 
**threeDSecure** | bool,  | BoolClass,  | 3Dセキュア有無 | [optional] 
**threeDSecureVersion** | str,  | str,  | 3Dセキュアバージョン | [optional] 
**anyStringName** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

