import pytest
from src.generators import transactions, filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency() -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == {'id': 939719570,
                               'state': 'EXECUTED',
                               'date': '2018-06-30T02:08:58.425572',
                               'operationAmount':
                                   {'amount': '9824.07',
                                    'currency': {
                                           'name': 'USD',
                                           'code': 'USD'
                                         }
                                    },
                               'description': 'Перевод организации',
                               'from': 'Счет 75106830613657916952',
                               'to': 'Счет 11776614605963066702'}
    assert next(usd_transactions) == {'id': 142264268,
                               'state': 'EXECUTED',
                               'date': '2019-04-04T23:20:05.206878',
                               'operationAmount':
                                   {'amount': '79114.93',
                                    'currency': {
                                            'name': 'USD',
                                            'code': 'USD'
                                         }
                                    },
                               'description': 'Перевод со счета на счет',
                               'from': 'Счет 19708645243227258542',
                               'to': 'Счет 75651667383060284188'}


def test_filter_by_currency_rub() -> None:
    rub_transactions = filter_by_currency(transactions, "руб.")
    assert next(rub_transactions) == {"id": 873106923,
                                      "state": "EXECUTED",
                                      "date": "2019-03-23T01:09:46.296404",
                                      "operationAmount": {
                                          "amount": "43318.34",
                                          "currency": {
                                              "name": "руб.",
                                              "code": "RUB"
                                          }
                                      },
                                      "description": "Перевод со счета на счет",
                                      "from": "Счет 44812258784861134719",
                                      "to": "Счет 74489636417521191160"
                                      }

def test_filter_by_currency_() -> None:
    assert filter_by_currency(transactions, "")


def test_filter_by_currency__() -> None:
    assert filter_by_currency(transactions, "ERI")


def test_transaction_description():
    trans = transaction_descriptions(transactions)
    assert next(trans) == "Перевод организации"
    assert next(trans) == "Перевод со счета на счет"
    assert next(trans) == "Перевод со счета на счет"
    assert next(trans) == "Перевод с карты на карту"
    assert next(trans) == "Перевод организации"


def test_card_number_generator():
    num = card_number_generator(x=1, y=5)
    assert next(num) == "0000 0000 0000 0001"
    assert next(num) == "0000 0000 0000 0002"
    assert next(num) == "0000 0000 0000 0003"
    assert next(num) == "0000 0000 0000 0004"
    assert next(num) == "0000 0000 0000 0005"