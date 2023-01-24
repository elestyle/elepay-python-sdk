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


class ReaderStatusType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    リーダーステータス
- pending ペアリング待ち
- active ペアリング済み

    """


    class MetaOapg:
        enum_value_to_name = {
            "pending": "PENDING",
            "active": "ACTIVE",
        }
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("pending")
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("active")