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


class SubscriptionReq(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    定期課金作成リクエスト
    """


    class MetaOapg:
        required = {
            "customerId",
        }
        
        class properties:
            customerId = schemas.StrSchema
            name = schemas.StrSchema
            currency = schemas.StrSchema
            amount = schemas.IntSchema
        
            @staticmethod
            def interval() -> typing.Type['SubscriptionIntervalType']:
                return SubscriptionIntervalType
            initialAmount = schemas.IntSchema
            firstChargeTime = schemas.Int64Schema
            
            
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
            __annotations__ = {
                "customerId": customerId,
                "name": name,
                "currency": currency,
                "amount": amount,
                "interval": interval,
                "initialAmount": initialAmount,
                "firstChargeTime": firstChargeTime,
                "metadata": metadata,
            }
    
    customerId: MetaOapg.properties.customerId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interval"]) -> 'SubscriptionIntervalType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialAmount"]) -> MetaOapg.properties.initialAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstChargeTime"]) -> MetaOapg.properties.firstChargeTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customerId", "name", "currency", "amount", "interval", "initialAmount", "firstChargeTime", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interval"]) -> typing.Union['SubscriptionIntervalType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialAmount"]) -> typing.Union[MetaOapg.properties.initialAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstChargeTime"]) -> typing.Union[MetaOapg.properties.firstChargeTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customerId", "name", "currency", "amount", "interval", "initialAmount", "firstChargeTime", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        customerId: typing.Union[MetaOapg.properties.customerId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        interval: typing.Union['SubscriptionIntervalType', schemas.Unset] = schemas.unset,
        initialAmount: typing.Union[MetaOapg.properties.initialAmount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        firstChargeTime: typing.Union[MetaOapg.properties.firstChargeTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubscriptionReq':
        return super().__new__(
            cls,
            *args,
            customerId=customerId,
            name=name,
            currency=currency,
            amount=amount,
            interval=interval,
            initialAmount=initialAmount,
            firstChargeTime=firstChargeTime,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from elepay.model.subscription_interval_type import SubscriptionIntervalType
