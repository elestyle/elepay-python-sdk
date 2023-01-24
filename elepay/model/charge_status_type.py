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


class ChargeStatusType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    支払い状態
- pending 未支払
- uncaptured 承認済み(未確定)
- captured 支払済み
- partially_refunded 一部返金
- refunded 返金済み
- revoked キャンセル済み

    """


    class MetaOapg:
        enum_value_to_name = {
            "pending": "PENDING",
            "uncaptured": "UNCAPTURED",
            "captured": "CAPTURED",
            "partially_refunded": "PARTIALLY_REFUNDED",
            "refunded": "REFUNDED",
            "revoked": "REVOKED",
        }
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("pending")
    
    @schemas.classproperty
    def UNCAPTURED(cls):
        return cls("uncaptured")
    
    @schemas.classproperty
    def CAPTURED(cls):
        return cls("captured")
    
    @schemas.classproperty
    def PARTIALLY_REFUNDED(cls):
        return cls("partially_refunded")
    
    @schemas.classproperty
    def REFUNDED(cls):
        return cls("refunded")
    
    @schemas.classproperty
    def REVOKED(cls):
        return cls("revoked")
