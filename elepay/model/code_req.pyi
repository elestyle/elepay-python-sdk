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


class CodeReq(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    EasyQRコードリクエスト
    """


    class MetaOapg:
        required = {
            "amount",
            "orderNo",
        }
        
        class properties:
            amount = schemas.IntSchema
            orderNo = schemas.StrSchema
            currency = schemas.StrSchema
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
            expiryDuration = schemas.IntSchema
            
            
            class frontUrl(
                schemas.StrSchema
            ):
                pass
            
            
            class items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CodeItem']:
                        return CodeItem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CodeItem'], typing.List['CodeItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CodeItem':
                    return super().__getitem__(i)
            __annotations__ = {
                "amount": amount,
                "orderNo": orderNo,
                "currency": currency,
                "description": description,
                "extra": extra,
                "metadata": metadata,
                "expiryDuration": expiryDuration,
                "frontUrl": frontUrl,
                "items": items,
            }
    
    amount: MetaOapg.properties.amount
    orderNo: MetaOapg.properties.orderNo
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderNo"]) -> MetaOapg.properties.orderNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra"]) -> MetaOapg.properties.extra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryDuration"]) -> MetaOapg.properties.expiryDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frontUrl"]) -> MetaOapg.properties.frontUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "orderNo", "currency", "description", "extra", "metadata", "expiryDuration", "frontUrl", "items", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderNo"]) -> MetaOapg.properties.orderNo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra"]) -> typing.Union[MetaOapg.properties.extra, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryDuration"]) -> typing.Union[MetaOapg.properties.expiryDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frontUrl"]) -> typing.Union[MetaOapg.properties.frontUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union[MetaOapg.properties.items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "orderNo", "currency", "description", "extra", "metadata", "expiryDuration", "frontUrl", "items", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        orderNo: typing.Union[MetaOapg.properties.orderNo, str, ],
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        extra: typing.Union[MetaOapg.properties.extra, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        expiryDuration: typing.Union[MetaOapg.properties.expiryDuration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        frontUrl: typing.Union[MetaOapg.properties.frontUrl, str, schemas.Unset] = schemas.unset,
        items: typing.Union[MetaOapg.properties.items, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CodeReq':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            orderNo=orderNo,
            currency=currency,
            description=description,
            extra=extra,
            metadata=metadata,
            expiryDuration=expiryDuration,
            frontUrl=frontUrl,
            items=items,
            _configuration=_configuration,
            **kwargs,
        )

from elepay.model.code_item import CodeItem