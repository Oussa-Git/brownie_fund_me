from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import deploy_mocks, get_account, LOCAL_BLOCKCHAIN


def deploy_fundme():

    account = get_account()

    # if rinkeby network is used , use Pricefeed address associated
    # otherwise use Mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN:
        Pricefeed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        deploy_mocks()

        Pricefeed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        Pricefeed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"Contract Deployed at {fund_me.address}")


def main():

    deploy_fundme()
