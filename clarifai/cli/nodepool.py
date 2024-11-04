import click
from clarifai.cli.base import cli
from clarifai.client.compute_cluster import ComputeCluster
from clarifai.utils.cli import display_co_resources


@cli.group(['nodepool', 'np'])
def nodepool():
  """Manage Nodepools: create, delete, list"""
  pass


@nodepool.command()
@click.option(
    '-cc_id',
    '--compute_cluster_id',
    required=True,
    help='Compute Cluster ID for the compute cluster to interact with.')
@click.option(
    '-config',
    '--config_filepath',
    type=click.Path(exists=True),
    required=True,
    help='Path to the nodepool config file.')
@click.option(
    '-np_id', '--nodepool_id', required=False, help='New Nodepool ID for the nodepool to create.')
@click.pass_context
def create(ctx, compute_cluster_id, config_filepath, nodepool_id):
  """Create a new Nodepool with the given config file."""
  compute_cluster = ComputeCluster(
      compute_cluster_id=compute_cluster_id,
      user_id=ctx.obj['user_id'],
      pat=ctx.obj['pat'],
      base_url=ctx.obj['base_url'])
  if nodepool_id:
    compute_cluster.create_nodepool(config_filepath, nodepool_id=nodepool_id)
  else:
    compute_cluster.create_nodepool(config_filepath)


@nodepool.command()
@click.option(
    '-cc_id',
    '--compute_cluster_id',
    required=True,
    help='Compute Cluster ID for the compute cluster to interact with.')
@click.option('--page_no', required=False, help='Page number to list.', default=1)
@click.option('--per_page', required=False, help='Number of items per page.', default=16)
@click.pass_context
def list(ctx, compute_cluster_id, page_no, per_page):
  """List all nodepools for the user."""
  compute_cluster = ComputeCluster(
      compute_cluster_id=compute_cluster_id,
      user_id=ctx.obj['user_id'],
      pat=ctx.obj['pat'],
      base_url=ctx.obj['base_url'])
  response = compute_cluster.list_nodepools(page_no, per_page)
  display_co_resources(response, "Nodepool")


@nodepool.command()
@click.option(
    '-cc_id',
    '--compute_cluster_id',
    required=True,
    help='Compute Cluster ID for the compute cluster to interact with.')
@click.option('-np_id', '--nodepool_id', help='Nodepool ID of the user to delete.')
@click.pass_context
def delete(ctx, compute_cluster_id, nodepool_id):
  """Deletes a nodepool for the user."""
  compute_cluster = ComputeCluster(
      compute_cluster_id=compute_cluster_id,
      user_id=ctx.obj['user_id'],
      pat=ctx.obj['pat'],
      base_url=ctx.obj['base_url'])
  compute_cluster.delete_nodepools([nodepool_id])
