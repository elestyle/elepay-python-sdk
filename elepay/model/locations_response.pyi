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


class LocationsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Location情報リスト
    """


    class MetaOapg:
        
        class properties:
            
            
            class locations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LocationDto']:
                        return LocationDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['LocationDto'], typing.List['LocationDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'locations':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LocationDto':
                    return super().__getitem__(i)
            __annotations__ = {
                "locations": locations,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locations"]) -> MetaOapg.properties.locations: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["locations", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locations"]) -> typing.Union[MetaOapg.properties.locations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["locations", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        locations: typing.Union[MetaOapg.properties.locations, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LocationsResponse':
        return super().__new__(
            cls,
            *args,
            locations=locations,
            _configuration=_configuration,
            **kwargs,
        )

from elepay.model.location_dto import LocationDto