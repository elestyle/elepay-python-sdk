# ChargeReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | 金額 | [optional] 
**currency** | **str** | 通貨コード (ISO_4217) | [optional] [default to 'JPY']
**payment_method** | [**PaymentMethodType**](PaymentMethodType.md) |  | [optional] 
**order_no** | **str** | お客様側のシステムオーダーNo（例：注文番号、決済IDなど） | [optional] 
**description** | **str** | 決済に関する説明 | [optional] 
**extra** | **dict(str, object)** | 決済に関する追加情報がある場合に利用します。 | [optional] 
**metadata** | **dict(str, object)** | メタデータ | [optional] 
**client_ip** | **str** | Client IP アドレス | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


