import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.hello_world.hello_world_client import (
        HelloWorldClient as CalculatorClient,
    )
    testnetAlgodClient=AlgodClient("a"*64,"	https://testnet-api.algonode.cloud")
    testIndexerclient=IndexerClient("a"*64,"https://testnet-idx.algonode.cloud")
    myAccount=algokit_utils.get_account_from_mnemonic("pulp million float faith limb limit spice silent correct used style acid either inhale obscure hour marriage scan shaft quality marriage insane version absorb sentence")

    app_client = CalculatorClient(
        algod_client=testnetAlgodClient,
        creator=myAccount,
        indexer_client=testIndexerclient,
    )

    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )
    logger.info(f"Deployed Caluclator with app ID:(app_client.app_id)")
    a=10
    b=5
    response = app_client.add(a=a,b=b)
    logger.info(
        f"Called add on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a={a} and b={b}, received: {response.return_value}"
    )
    a=10
    b=6
    response = app_client.sub(a=a,b=b)
    logger.info(
        f"Called sub on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a={a} and b={b}, received: {response.return_value}"
    )
    a=10
    b=10
    response = app_client.mul(a=a,b=b)
    logger.info(
        f"Called mul on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a={a} and b={b}, received: {response.return_value}"
    )
    a=10
    b=2
    response = app_client.div(a=a,b=b)
    logger.info(
        f"Called div on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a={a} and b={b}, received: {response.return_value}"
    )