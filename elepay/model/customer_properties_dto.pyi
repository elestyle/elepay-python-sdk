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


class CustomerPropertiesDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    決済方法カスタマ関する情報
    """


    class MetaOapg:
        
        class properties:
            isSupportCustomer = schemas.BoolSchema
            isSupportMultipleSource = schemas.BoolSchema
            __annotations__ = {
                "isSupportCustomer": isSupportCustomer,
                "isSupportMultipleSource": isSupportMultipleSource,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSupportCustomer"]) -> MetaOapg.properties.isSupportCustomer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSupportMultipleSource"]) -> MetaOapg.properties.isSupportMultipleSource: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isSupportCustomer", "isSupportMultipleSource", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSupportCustomer"]) -> typing.Union[MetaOapg.properties.isSupportCustomer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSupportMultipleSource"]) -> typing.Union[MetaOapg.properties.isSupportMultipleSource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isSupportCustomer", "isSupportMultipleSource", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        isSupportCustomer: typing.Union[MetaOapg.properties.isSupportCustomer, bool, schemas.Unset] = schemas.unset,
        isSupportMultipleSource: typing.Union[MetaOapg.properties.isSupportMultipleSource, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomerPropertiesDto':
        return super().__new__(
            cls,
            *args,
            isSupportCustomer=isSupportCustomer,
            isSupportMultipleSource=isSupportMultipleSource,
            _configuration=_configuration,
            **kwargs,
        )
