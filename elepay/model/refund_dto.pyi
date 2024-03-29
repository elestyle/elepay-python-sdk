# coding: utf-8

"""
    elepay API リファレンス

    elepay APIはRESTをベースに構成された決済APIです。支払い処理、返金処理など、決済に関わる運用における様々なことができます。  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: support@elestyle.jp
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from elepay import schemas  # noqa: F401


class RefundDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    返金オブジェクト
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            object = schemas.StrSchema
            chargeId = schemas.StrSchema
            liveMode = schemas.BoolSchema
            amount = schemas.IntSchema
            currency = schemas.StrSchema
            
            
            class metadata(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'metadata':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            reason = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['RefundStatusType']:
                return RefundStatusType
            refundedTime = schemas.Int64Schema
            createTime = schemas.Int64Schema
            __annotations__ = {
                "id": id,
                "object": object,
                "chargeId": chargeId,
                "liveMode": liveMode,
                "amount": amount,
                "currency": currency,
                "metadata": metadata,
                "reason": reason,
                "status": status,
                "refundedTime": refundedTime,
                "createTime": createTime,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeId"]) -> MetaOapg.properties.chargeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["liveMode"]) -> MetaOapg.properties.liveMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'RefundStatusType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refundedTime"]) -> MetaOapg.properties.refundedTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createTime"]) -> MetaOapg.properties.createTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "object", "chargeId", "liveMode", "amount", "currency", "metadata", "reason", "status", "refundedTime", "createTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeId"]) -> typing.Union[MetaOapg.properties.chargeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["liveMode"]) -> typing.Union[MetaOapg.properties.liveMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['RefundStatusType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refundedTime"]) -> typing.Union[MetaOapg.properties.refundedTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createTime"]) -> typing.Union[MetaOapg.properties.createTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "object", "chargeId", "liveMode", "amount", "currency", "metadata", "reason", "status", "refundedTime", "createTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        chargeId: typing.Union[MetaOapg.properties.chargeId, str, schemas.Unset] = schemas.unset,
        liveMode: typing.Union[MetaOapg.properties.liveMode, bool, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        status: typing.Union['RefundStatusType', schemas.Unset] = schemas.unset,
        refundedTime: typing.Union[MetaOapg.properties.refundedTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createTime: typing.Union[MetaOapg.properties.createTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RefundDto':
        return super().__new__(
            cls,
            *args,
            id=id,
            object=object,
            chargeId=chargeId,
            liveMode=liveMode,
            amount=amount,
            currency=currency,
            metadata=metadata,
            reason=reason,
            status=status,
            refundedTime=refundedTime,
            createTime=createTime,
            _configuration=_configuration,
            **kwargs,
        )

from elepay.model.refund_status_type import RefundStatusType
