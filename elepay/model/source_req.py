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


class SourceReq(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    カスタマソースリクエスト
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def paymentMethod() -> typing.Type['PaymentMethodType']:
                return PaymentMethodType
        
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
            __annotations__ = {
                "paymentMethod": paymentMethod,
                "resource": resource,
                "description": description,
                "extra": extra,
                "metadata": metadata,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentMethod"]) -> 'PaymentMethodType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource"]) -> 'ResourceType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra"]) -> MetaOapg.properties.extra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["paymentMethod", "resource", "description", "extra", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentMethod"]) -> typing.Union['PaymentMethodType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource"]) -> typing.Union['ResourceType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra"]) -> typing.Union[MetaOapg.properties.extra, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["paymentMethod", "resource", "description", "extra", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        paymentMethod: typing.Union['PaymentMethodType', schemas.Unset] = schemas.unset,
        resource: typing.Union['ResourceType', schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        extra: typing.Union[MetaOapg.properties.extra, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SourceReq':
        return super().__new__(
            cls,
            *args,
            paymentMethod=paymentMethod,
            resource=resource,
            description=description,
            extra=extra,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from elepay.model.payment_method_type import PaymentMethodType
from elepay.model.resource_type import ResourceType
