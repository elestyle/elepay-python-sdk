# coding: utf-8

"""
    elepay API リファレンス

    elepay APIはRESTをベースに構成された決済APIです。支払い処理、返金処理など、決済に関わる運用における様々なことができます。   # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RefundReq(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'charge_id': 'str',
        'amount': 'int',
        'currency': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'charge_id': 'chargeId',
        'amount': 'amount',
        'currency': 'currency',
        'reason': 'reason'
    }

    def __init__(self, charge_id=None, amount=None, currency=None, reason=None):  # noqa: E501
        """RefundReq - a model defined in OpenAPI"""  # noqa: E501

        self._charge_id = None
        self._amount = None
        self._currency = None
        self._reason = None
        self.discriminator = None

        if charge_id is not None:
            self.charge_id = charge_id
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if reason is not None:
            self.reason = reason

    @property
    def charge_id(self):
        """Gets the charge_id of this RefundReq.  # noqa: E501

        Charge ID  # noqa: E501

        :return: The charge_id of this RefundReq.  # noqa: E501
        :rtype: str
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this RefundReq.

        Charge ID  # noqa: E501

        :param charge_id: The charge_id of this RefundReq.  # noqa: E501
        :type: str
        """

        self._charge_id = charge_id

    @property
    def amount(self):
        """Gets the amount of this RefundReq.  # noqa: E501

        返金額。全額返金、及び amount の指定で任意の金額で返金ができます。  # noqa: E501

        :return: The amount of this RefundReq.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RefundReq.

        返金額。全額返金、及び amount の指定で任意の金額で返金ができます。  # noqa: E501

        :param amount: The amount of this RefundReq.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this RefundReq.  # noqa: E501

        通貨コード (ISO_4217)  # noqa: E501

        :return: The currency of this RefundReq.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this RefundReq.

        通貨コード (ISO_4217)  # noqa: E501

        :param currency: The currency of this RefundReq.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def reason(self):
        """Gets the reason of this RefundReq.  # noqa: E501

        返金理由  # noqa: E501

        :return: The reason of this RefundReq.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this RefundReq.

        返金理由  # noqa: E501

        :param reason: The reason of this RefundReq.  # noqa: E501
        :type: str
        """

        self._reason = reason

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RefundReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
