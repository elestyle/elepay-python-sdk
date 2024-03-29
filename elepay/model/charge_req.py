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


class ChargeReq(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    支払リクエスト
    """


    class MetaOapg:
        required = {
            "amount",
            "orderNo",
            "paymentMethod",
        }
        
        class properties:
            amount = schemas.IntSchema
        
            @staticmethod
            def paymentMethod() -> typing.Type['PaymentMethodType']:
                return PaymentMethodType
            orderNo = schemas.StrSchema
            capture = schemas.BoolSchema
            currency = schemas.StrSchema
        
            @staticmethod
            def resource() -> typing.Type['ResourceType']:
                return ResourceType
            description = schemas.StrSchema
            
            
            class extra(
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
                ) -> 'extra':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
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
            clientIp = schemas.StrSchema
            customerId = schemas.StrSchema
            sourceId = schemas.StrSchema
            __annotations__ = {
                "amount": amount,
                "paymentMethod": paymentMethod,
                "orderNo": orderNo,
                "capture": capture,
                "currency": currency,
                "resource": resource,
                "description": description,
                "extra": extra,
                "metadata": metadata,
                "clientIp": clientIp,
                "customerId": customerId,
                "sourceId": sourceId,
            }
    
    amount: MetaOapg.properties.amount
    orderNo: MetaOapg.properties.orderNo
    paymentMethod: 'PaymentMethodType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentMethod"]) -> 'PaymentMethodType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderNo"]) -> MetaOapg.properties.orderNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capture"]) -> MetaOapg.properties.capture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource"]) -> 'ResourceType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra"]) -> MetaOapg.properties.extra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientIp"]) -> MetaOapg.properties.clientIp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceId"]) -> MetaOapg.properties.sourceId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "paymentMethod", "orderNo", "capture", "currency", "resource", "description", "extra", "metadata", "clientIp", "customerId", "sourceId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentMethod"]) -> 'PaymentMethodType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderNo"]) -> MetaOapg.properties.orderNo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capture"]) -> typing.Union[MetaOapg.properties.capture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource"]) -> typing.Union['ResourceType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra"]) -> typing.Union[MetaOapg.properties.extra, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientIp"]) -> typing.Union[MetaOapg.properties.clientIp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> typing.Union[MetaOapg.properties.customerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceId"]) -> typing.Union[MetaOapg.properties.sourceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "paymentMethod", "orderNo", "capture", "currency", "resource", "description", "extra", "metadata", "clientIp", "customerId", "sourceId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        orderNo: typing.Union[MetaOapg.properties.orderNo, str, ],
        paymentMethod: 'PaymentMethodType',
        capture: typing.Union[MetaOapg.properties.capture, bool, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        resource: typing.Union['ResourceType', schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        extra: typing.Union[MetaOapg.properties.extra, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        clientIp: typing.Union[MetaOapg.properties.clientIp, str, schemas.Unset] = schemas.unset,
        customerId: typing.Union[MetaOapg.properties.customerId, str, schemas.Unset] = schemas.unset,
        sourceId: typing.Union[MetaOapg.properties.sourceId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChargeReq':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            orderNo=orderNo,
            paymentMethod=paymentMethod,
            capture=capture,
            currency=currency,
            resource=resource,
            description=description,
            extra=extra,
            metadata=metadata,
            clientIp=clientIp,
            customerId=customerId,
            sourceId=sourceId,
            _configuration=_configuration,
            **kwargs,
        )

from elepay.model.payment_method_type import PaymentMethodType
from elepay.model.resource_type import ResourceType
