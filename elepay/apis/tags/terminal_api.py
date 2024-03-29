# coding: utf-8

"""
    elepay API リファレンス

    elepay APIはRESTをベースに構成された決済APIです。支払い処理、返金処理など、決済に関わる運用における様々なことができます。  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: support@elestyle.jp
    Generated by: https://openapi-generator.tech
"""

from elepay.paths.terminal_readers.post import CreateReader
from elepay.paths.terminal_readers_reader_id.delete import DeleteReader
from elepay.paths.terminal_readers_reader_id.get import GetReader
from elepay.paths.terminal_locations.get import ListLocations
from elepay.paths.terminal_readers.get import ListReaders


class TerminalApi(
    CreateReader,
    DeleteReader,
    GetReader,
    ListLocations,
    ListReaders,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
