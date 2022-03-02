from scripts.helpful_scripts import get_account

from scripts.deploy import deploy_fundme


def test_fund_and_withdrow():

    account = get_account()
    fund_me = deploy_fundme()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx_2 = fund_me.withdraw({"from": account})
    tx_2.wait(2)
    assert fund_me.addressToAmountFunded(account.address) == 0
