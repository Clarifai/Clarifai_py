import json
import os
import subprocess

# throw error if huggingface_hub wasn't installed
try:
  from huggingface_hub import snapshot_download
except ImportError:
  raise ImportError(
      "The 'huggingface_hub' package is not installed. Please install it using 'pip install huggingface_hub'."
  )


class HuggingFaceLoarder:

  def __init__(self, model_name=None, token=None):
    self.model_name = model_name
    self.token = token
    if token:
      try:
        os.environ['HF_TOKEN'] = token
        subprocess.run(f'huggingface-cli login --token={os.environ["HF_TOKEN"]}', shell=True)
      except Exception as e:
        print("Error setting HF token ", e)

  def download_checkpoints(self, checkpoint_path: str):
    if os.path.exists(checkpoint_path):
      print("Checkpoints already exist")
    else:
      os.makedirs(checkpoint_path, exist_ok=True)
      try:
        is_hf_model_exists = self.validate_hf_model()
        if not is_hf_model_exists:
          print("Model not found on Hugging Face")
          return False
        snapshot_download(repo_id=self.model_name, local_dir=checkpoint_path)
      except Exception as e:
        print("Error downloading model checkpoints ", e)
        return False

      if not self.validate_download(checkpoint_path):
        print("Error downloading model checkpoints")
        return False
      return True

  def validate_hf_model(self,):
    # check if model exists on HF

    from huggingface_hub import file_exists, repo_exists
    return repo_exists(self.model_name) and file_exists(self.model_name, 'config.json')

  def validate_download(self, checkpoint_path: str):
    # check if model exists on HF
    from huggingface_hub import list_repo_files

    return (len(os.listdir(checkpoint_path)) >= len(list_repo_files(self.model_name))) and len(
        list_repo_files(self.model_name)) > 0

  def fetch_labels(self, checkpoint_path: str):
    # Fetch labels for classification, detection and segmentation models
    config_path = os.path.join(checkpoint_path, 'config.json')
    with open(config_path, 'r') as f:
      config = json.load(f)

    labels = config['id2label']
    return labels