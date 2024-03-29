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


class PaymentMethodDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    決済方法詳細情報
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def paymentMethod() -> typing.Type['PaymentMethodType']:
                return PaymentMethodType
            
            
            class resources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ResourceType']:
                        return ResourceType
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ResourceType'], typing.List['ResourceType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'resources':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ResourceType':
                    return super().__getitem__(i)
            
            
            class brand(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'brand':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            ua = schemas.StrSchema
        
            @staticmethod
            def channelProperties() -> typing.Type['ChannelPropertiesDto']:
                return ChannelPropertiesDto
        
            @staticmethod
            def customerProperties() -> typing.Type['CustomerPropertiesDto']:
                return CustomerPropertiesDto
            __annotations__ = {
                "paymentMethod": paymentMethod,
                "resources": resources,
                "brand": brand,
                "ua": ua,
                "channelProperties": channelProperties,
                "customerProperties": customerProperties,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentMethod"]) -> 'PaymentMethodType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> MetaOapg.properties.resources: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brand"]) -> MetaOapg.properties.brand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ua"]) -> MetaOapg.properties.ua: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channelProperties"]) -> 'ChannelPropertiesDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerProperties"]) -> 'CustomerPropertiesDto': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["paymentMethod", "resources", "brand", "ua", "channelProperties", "customerProperties", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentMethod"]) -> typing.Union['PaymentMethodType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> typing.Union[MetaOapg.properties.resources, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brand"]) -> typing.Union[MetaOapg.properties.brand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ua"]) -> typing.Union[MetaOapg.properties.ua, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channelProperties"]) -> typing.Union['ChannelPropertiesDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerProperties"]) -> typing.Union['CustomerPropertiesDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["paymentMethod", "resources", "brand", "ua", "channelProperties", "customerProperties", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        paymentMethod: typing.Union['PaymentMethodType', schemas.Unset] = schemas.unset,
        resources: typing.Union[MetaOapg.properties.resources, list, tuple, schemas.Unset] = schemas.unset,
        brand: typing.Union[MetaOapg.properties.brand, list, tuple, schemas.Unset] = schemas.unset,
        ua: typing.Union[MetaOapg.properties.ua, str, schemas.Unset] = schemas.unset,
        channelProperties: typing.Union['ChannelPropertiesDto', schemas.Unset] = schemas.unset,
        customerProperties: typing.Union['CustomerPropertiesDto', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentMethodDto':
        return super().__new__(
            cls,
            *args,
            paymentMethod=paymentMethod,
            resources=resources,
            brand=brand,
            ua=ua,
            channelProperties=channelProperties,
            customerProperties=customerProperties,
            _configuration=_configuration,
            **kwargs,
        )

from elepay.model.channel_properties_dto import ChannelPropertiesDto
from elepay.model.customer_properties_dto import CustomerPropertiesDto
from elepay.model.payment_method_type import PaymentMethodType
from elepay.model.resource_type import ResourceType
