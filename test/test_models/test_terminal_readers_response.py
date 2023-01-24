# coding: utf-8

"""
    elepay API リファレンス

    elepay APIはRESTをベースに構成された決済APIです。支払い処理、返金処理など、決済に関わる運用における様々なことができます。  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: support@elestyle.jp
    Generated by: https://openapi-generator.tech
"""

import unittest

import elepay
from elepay.model.terminal_readers_response import TerminalReadersResponse
from elepay import configuration


class TestTerminalReadersResponse(unittest.TestCase):
    """TerminalReadersResponse unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
