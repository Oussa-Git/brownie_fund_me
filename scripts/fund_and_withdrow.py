from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():

    account = get_account()
    fund_me = FundMe[-1]

    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"entrance fee = {entrance_fee}")
    print("funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdrow():
    account = get_account()
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdrow()
