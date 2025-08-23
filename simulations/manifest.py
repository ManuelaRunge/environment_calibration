
# This is a user-modifiable Python file designed to be a set of simple input file and directory settings that you can choose and change.
from pathlib import Path
import os

VENV_PATH = '/gpfs/projects/b1139/environments/emodpy_pmc/'

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CURRENT_DIR.parent

job_directory = "/gpfs/projects/b1139/ipti_pmc/_mrm9534/env_calib_experiments/"
os.makedirs(job_directory, exist_ok=True)

input_files_path = "/gpfs/projects/b1139/ipti_pmc/simulation_inputs/"
simulation_coordinator_path =  "/gpfs/home/mrm9534/ipti_pmc/environment_calibration/simulation_inputs/simulation_coordinator.csv"
calibration_coordinator_path =  "/gpfs/home/mrm9534/ipti_pmc/environment_calibration/simulation_inputs/calibration_coordinator.csv"
site_coordinator_path =  "/gpfs/projects/b1139/ipti_pmc/simulation_inputs/site_coordinator.csv"


DOWNLOAD_DIR = CURRENT_DIR / "download" / "bin_230614_PT"
schema_file = DOWNLOAD_DIR / "schema.json"

eradication_path = DOWNLOAD_DIR / "Eradication"
plugins_folder = DOWNLOAD_DIR / "reporter_plugins"
assets_input_dir = CURRENT_DIR / "Assets"
comps_id_folder = PROJECT_DIR/"simulations" / "COMPS_ID"
suite_id_file = comps_id_folder / 'Suite'
version_file = comps_id_folder / "version.txt"
eradication_found = comps_id_folder / 'eradication_found'
sif_id = comps_id_folder / 'sif.id'

simulation_input_filepath = "/gpfs/projects/b1139/ipti_pmc/simulation_inputs/"
simulation_output_filepath = "/gpfs/projects/b1139/ipti_pmc/_mrm9534/env_calib_outputs/"
benchmark_simulation_filepath = "/gpfs/projects/b1139/ipti_pmc/_mrm9534/env_calib_outputs/"
base_script_plot_filepath = PROJECT_DIR / "create_plots"
base_reference_filepath = "/gpfs/projects/b1139/ipti_pmc/reference_datasets/"
plot_output_filepath = "/gpfs/projects/b1139/ipti_pmc/_mrm9534/env_calib_plots/"
python_plot_output_filepath = "/gpfs/projects/b1139/ipti_pmc/_mrm9534/env_calib_plots_Python"


sweep_sim_coordinator_path = "/gpfs/projects/b1139/ipti_pmc/simulation_inputs/sweep_sim_coordinator.csv"

my_ep4_assets = None
requirements = PROJECT_DIR / "requirements.txt"

# Define Comps platform
platform_name = "SLURM_LOCAL" #"Calculon"
priority = 'BelowNormal'
node_group_private = 'idm_48cores'
node_group = 'idm_abcd'

# This is the path to the sisf image used to run EMOD
SIF_PATH = "--bind /projects /gpfs/projects/b1139/images/dtk_run_rocky_py39.sif"

# ========================================================
"""
This section contains the most important parameters that you may want to change before running the snakemake workflow.
use_local_eradication: set to 0 to run workflow using the Eradication and schema currently under download_folder.
                       set to 1 to get Eradicaiton and schema from emod_malaria and unzip them to download_folder.
singularity_id: the AC id for singularity image that the simulation will be run with.
                Set it to None if you don't want to run with any singularity image.
"""
use_local_eradication = True
eradication_path = '/gpfs/home/mrm9534/download/Eradication'
singularity_id = "8df53802-53f3-ec11-a9f9-b88303911bc1"
# ========================================================


