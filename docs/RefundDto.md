# RefundDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Refund ID | [optional] 
**object** | **str** | 対象種類の表記 | [optional] [default to 'refund']
**charge_id** | **str** | Charge ID | [optional] 
**live_mode** | **bool** | 本番モードかどうか - false テストモード - true 本番モード  | [optional] 
**amount** | **int** | 返金金額。全額返金、及び amount を指定することで金額の部分返金を行うことができます。 | [optional] 
**currency** | **str** | 通貨コード (ISO_4217) | [optional] 
**reason** | **str** | 返金理由 | [optional] 
**status** | **str** | 返金状態 | [optional] 
**refunded_time** | **int** | 返金を行う時間のUTCタイムスタンプ。 | [optional] 
**create_time** | **int** | 返金新規時間のUTCタイムスタンプ。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


