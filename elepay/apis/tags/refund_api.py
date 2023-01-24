# coding: utf-8

"""
    elepay API リファレンス

    elepay APIはRESTをベースに構成された決済APIです。支払い処理、返金処理など、決済に関わる運用における様々なことができます。  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: support@elestyle.jp
    Generated by: https://openapi-generator.tech
"""

from elepay.paths.charges_id_refunds.post import CreateRefund
from elepay.paths.charges_id_refunds.get import ListChargesRefunds
from elepay.paths.charges_id_refunds_refund_id.get import RetrieveChargeRefund


class RefundApi(
    CreateRefund,
    ListChargesRefunds,
    RetrieveChargeRefund,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
