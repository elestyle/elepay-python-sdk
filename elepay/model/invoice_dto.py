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


class InvoiceDto(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    インボイスオブジェクト
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            object = schemas.StrSchema
            liveMode = schemas.BoolSchema
        
            @staticmethod
            def customer() -> typing.Type['CustomerDto']:
                return CustomerDto
            invoiceNo = schemas.StrSchema
            name = schemas.StrSchema
            memo = schemas.StrSchema
            amount = schemas.IntSchema
            currency = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['InvoiceStatusType']:
                return InvoiceStatusType
            operator = schemas.StrSchema
            sendTime = schemas.Int64Schema
            paidTime = schemas.Int64Schema
            expiryTime = schemas.Int64Schema
            createTime = schemas.Int64Schema
            
            
            class items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['InvoiceItem']:
                        return InvoiceItem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['InvoiceItem'], typing.List['InvoiceItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'InvoiceItem':
                    return super().__getitem__(i)
            remark = schemas.StrSchema
            
            
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
                "id": id,
                "object": object,
                "liveMode": liveMode,
                "customer": customer,
                "invoiceNo": invoiceNo,
                "name": name,
                "memo": memo,
                "amount": amount,
                "currency": currency,
                "status": status,
                "operator": operator,
                "sendTime": sendTime,
                "paidTime": paidTime,
                "expiryTime": expiryTime,
                "createTime": createTime,
                "items": items,
                "remark": remark,
                "metadata": metadata,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["liveMode"]) -> MetaOapg.properties.liveMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'CustomerDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoiceNo"]) -> MetaOapg.properties.invoiceNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memo"]) -> MetaOapg.properties.memo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'InvoiceStatusType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sendTime"]) -> MetaOapg.properties.sendTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paidTime"]) -> MetaOapg.properties.paidTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryTime"]) -> MetaOapg.properties.expiryTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createTime"]) -> MetaOapg.properties.createTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remark"]) -> MetaOapg.properties.remark: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "object", "liveMode", "customer", "invoiceNo", "name", "memo", "amount", "currency", "status", "operator", "sendTime", "paidTime", "expiryTime", "createTime", "items", "remark", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["liveMode"]) -> typing.Union[MetaOapg.properties.liveMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['CustomerDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoiceNo"]) -> typing.Union[MetaOapg.properties.invoiceNo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memo"]) -> typing.Union[MetaOapg.properties.memo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['InvoiceStatusType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> typing.Union[MetaOapg.properties.operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sendTime"]) -> typing.Union[MetaOapg.properties.sendTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paidTime"]) -> typing.Union[MetaOapg.properties.paidTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryTime"]) -> typing.Union[MetaOapg.properties.expiryTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createTime"]) -> typing.Union[MetaOapg.properties.createTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union[MetaOapg.properties.items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remark"]) -> typing.Union[MetaOapg.properties.remark, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "object", "liveMode", "customer", "invoiceNo", "name", "memo", "amount", "currency", "status", "operator", "sendTime", "paidTime", "expiryTime", "createTime", "items", "remark", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        liveMode: typing.Union[MetaOapg.properties.liveMode, bool, schemas.Unset] = schemas.unset,
        customer: typing.Union['CustomerDto', schemas.Unset] = schemas.unset,
        invoiceNo: typing.Union[MetaOapg.properties.invoiceNo, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        memo: typing.Union[MetaOapg.properties.memo, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        status: typing.Union['InvoiceStatusType', schemas.Unset] = schemas.unset,
        operator: typing.Union[MetaOapg.properties.operator, str, schemas.Unset] = schemas.unset,
        sendTime: typing.Union[MetaOapg.properties.sendTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        paidTime: typing.Union[MetaOapg.properties.paidTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        expiryTime: typing.Union[MetaOapg.properties.expiryTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createTime: typing.Union[MetaOapg.properties.createTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        items: typing.Union[MetaOapg.properties.items, list, tuple, schemas.Unset] = schemas.unset,
        remark: typing.Union[MetaOapg.properties.remark, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InvoiceDto':
        return super().__new__(
            cls,
            *args,
            id=id,
            object=object,
            liveMode=liveMode,
            customer=customer,
            invoiceNo=invoiceNo,
            name=name,
            memo=memo,
            amount=amount,
            currency=currency,
            status=status,
            operator=operator,
            sendTime=sendTime,
            paidTime=paidTime,
            expiryTime=expiryTime,
            createTime=createTime,
            items=items,
            remark=remark,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from elepay.model.customer_dto import CustomerDto
from elepay.model.invoice_item import InvoiceItem
from elepay.model.invoice_status_type import InvoiceStatusType
