import os
from typing import Any, Dict, Generator, List

import yaml
from clarifai_grpc.grpc.api import resources_pb2, service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2
from google.protobuf.json_format import MessageToDict

from clarifai.client.base import BaseClient
from clarifai.client.dataset import Dataset
from clarifai.client.lister import Lister
from clarifai.client.nodepool import Nodepool
from clarifai.errors import UserError
from clarifai.utils.logging import get_logger


class ComputeCluster(Lister, BaseClient):
  """ComputeCluster is a class that provides access to Clarifai API endpoints related to Compute Cluster information."""

  def __init__(self,
               compute_cluster_id: str = None,
               user_id: str = None,
               base_url: str = "https://api.clarifai.com",
               pat: str = None,
               token: str = None,
               root_certificates_path: str = None,
               **kwargs):
    """Initializes an ComputeCluster object.

    Args:
        compute_cluster_id (str): The ComputeCluster ID for the ComputeCluster to interact with.
        base_url (str): Base API url. Default "https://api.clarifai.com"
        pat (str): A personal access token for authentication. Can be set as env var CLARIFAI_PAT
        token (str): A session token for authentication. Accepts either a session token or a pat. Can be set as env var CLARIFAI_SESSION_TOKEN
        root_certificates_path (str): Path to the SSL root certificates file, used to establish secure gRPC connections.
        **kwargs: Additional keyword arguments to be passed to the App.
            - name (str): The name of the app.
            - description (str): The description of the app.
    """
    self.kwargs = {**kwargs, 'id': compute_cluster_id, 'user_id': user_id}
    self.compute_cluster_info = resources_pb2.ComputeCluster(**self.kwargs)
    self.logger = get_logger(logger_level="INFO", name=__name__)
    BaseClient.__init__(
        self,
        user_id=self.user_id,
        compute_cluster_id=self.id,
        base=base_url,
        pat=pat,
        token=token,
        root_certificates_path=root_certificates_path)
    Lister.__init__(self)

  def list_nodepools(self, page_no: int = None,
                     per_page: int = None) -> Generator[Nodepool, None, None]:
    """Lists all the available nodepools of the compute cluster.

    Args:
        compute_cluster_id (str): The compute cluster ID to list the nodepools.
        page_no (int): The page number to list.
        per_page (int): The number of items per page.

    Yields:
        Nodepool: Nodepool objects for the nodepools in the compute cluster.

    Example:
        >>> from clarifai.client.compute_cluster import ComputeCluster
        >>> compute_cluster = ComputeCluster(compute_cluster_id="compute_cluster_id", user_id="user_id")
        >>> all_nodepools = list(compute_cluster.list_nodepools())

    Note:
        Defaults to 16 per page if page_no is specified and per_page is not specified.
        If both page_no and per_page are None, then lists all the resources.
    """
    request_data = dict(user_app_id=self.user_app_id, compute_cluster_id=self.id)
    all_nodepools_info = self.list_pages_generator(
        self.STUB.ListNodepools,
        service_pb2.ListNodepoolsRequest,
        request_data,
        per_page=per_page,
        page_no=page_no)

    for nodepool_info in all_nodepools_info:
      yield Nodepool.from_auth_helper(auth=self.auth_helper, **nodepool_info)

  def _process_nodepool_config(self, config_filepath: str) -> Dict[str, Any]:
    with open(config_filepath, "r") as file:
      nodepool_config = yaml.safe_load(file)

    nodepool = nodepool_config['nodepool']
    if 'compute_cluster' in nodepool:
      nodepool['compute_cluster'] = resources_pb2.ComputeCluster(**nodepool['compute_cluster'])
    else:
      nodepool['compute_cluster'] = resources_pb2.ComputeCluster(id=self.id, user_id=self.user_id)
    nodepool['node_capacity_type'] = resources_pb2.NodeCapacityType(capacity_types=[
        capacity_type for capacity_type in nodepool['node_capacity_type']['capacity_types']
    ])
    instance_types = []
    for instance_type in nodepool['instance_types']:
      if 'compute_info' in instance_type:
        instance_type['compute_info'] = resources_pb2.ComputeInfo(**instance_type['compute_info'])
      instance_types.append(resources_pb2.InstanceType(**instance_type))
    nodepool['instance_types'] = instance_types
    if "visibility" in nodepool:
      nodepool["visibility"] = resources_pb2.Visibility(**nodepool["visibility"])
    return nodepool

  def create_nodepool(self, nodepool_id: str, config_filepath: str) -> Dataset:
    """Creates a nodepool for the compute cluster.

    Args:
        nodepool_id (str): The nodepool ID for the nodepool to create.
        config_filepath (str): The path to the nodepool config file.

    Returns:
        Nodepool: A Nodepool object for the specified nodepool ID.

    Example:
        >>> from clarifai.client.compute_cluster import ComputeCluster
        >>> compute_cluster = ComputeCluster(compute_cluster_id="compute_cluster_id", user_id="user_id")
        >>> nodepool = compute_cluster.create_nodepool(nodepool_id="nodepool_id", config_filepath="config.yml")
    """
    if not os.path.exists(config_filepath):
      raise UserError(f"Nodepool config file not found at {config_filepath}")

    nodepool_config = self._process_nodepool_config(config_filepath)

    if 'id' in nodepool_config:
      nodepool_id = nodepool_config['id']
      nodepool_config.pop('id')

    request = service_pb2.PostNodepoolsRequest(
        user_app_id=self.user_app_id,
        compute_cluster_id=self.id,
        nodepools=[resources_pb2.Nodepool(id=nodepool_id, **nodepool_config)])
    response = self._grpc_request(self.STUB.PostNodepools, request)
    if response.status.code != status_code_pb2.SUCCESS:
      raise Exception(response.status)
    self.logger.info("\nNodepool created\n%s", response.status)

    return Nodepool.from_auth_helper(self.auth_helper, nodepool_id=nodepool_id)

  def nodepool(self, nodepool_id: str) -> Nodepool:
    """Returns a Nodepool object for the existing nodepool ID.

    Args:
        nodepool_id (str): The nodepool ID for the nodepool to interact with.

    Returns:
        Nodepool: A Nodepool object for the existing nodepool ID.

    Example:
        >>> from clarifai.client.compute_cluster import ComputeCluster
        >>> compute_cluster = ComputeCluster(compute_cluster_id="compute_cluster_id", user_id="user_id")
        >>> nodepool = compute_cluster.nodepool(nodepool_id="nodepool_id")
    """
    request = service_pb2.GetNodepoolRequest(
        user_app_id=self.user_app_id, compute_cluster_id=self.id, nodepool_id=nodepool_id)
    response = self._grpc_request(self.STUB.GetNodepool, request)

    if response.status.code != status_code_pb2.SUCCESS:
      raise Exception(response.status)
    dict_response = MessageToDict(response, preserving_proto_field_name=True)
    kwargs = self.process_response_keys(dict_response[list(dict_response.keys())[1]],
                                        list(dict_response.keys())[1])

    return Nodepool.from_auth_helper(auth=self.auth_helper, **kwargs)

  def delete_nodepools(self, nodepool_ids: List[str]) -> None:
    """Deletes list of nodepools for the compute cluster.

    Args:
        nodepool_ids (List[str]): The nodepool IDs of the compute cluster to delete.

    Example:
        >>> from clarifai.client.compute_cluster import ComputeCluster
        >>> compute_cluster = ComputeCluster(compute_cluster_id="compute_cluster_id", user_id="user_id")
        >>> compute_cluster.delete_nodepools(nodepool_ids=["nodepool_id1", "nodepool_id2"])
    """
    request = service_pb2.DeleteNodepoolsRequest(
        user_app_id=self.user_app_id, compute_cluster_id=self.id, ids=nodepool_ids)
    response = self._grpc_request(self.STUB.DeleteNodepools, request)

    if response.status.code != status_code_pb2.SUCCESS:
      raise Exception(response.status)
    self.logger.info("\nNodepools Deleted\n%s", response.status)

  def __getattr__(self, name):
    return getattr(self.compute_cluster_info, name)

  def __str__(self):
    init_params = [param for param in self.kwargs.keys()]
    attribute_strings = [
        f"{param}={getattr(self.compute_cluster_info, param)}" for param in init_params
        if hasattr(self.compute_cluster_info, param)
    ]
    return f"Clarifai Compute Cluster Details: \n{', '.join(attribute_strings)}\n"
