import os
from datetime import datetime, timedelta

from airflow.decorators import dag, task

from sagetasks.nextflowtower.utils import TowerUtils


@dag(
    schedule_interval=None,
    start_date=datetime(2022, 11, 11),
    catchup=False,
    default_args={
        "retries": 2,
    },
    tags=["nextflow_tower"],
)
def nf_validate_dag():
    @task(multiple_outputs=True)
    def open_tower_workspace():
        """
        Opens tower workspace - things are hard coded for the moment that would be parameterized in future versions

        Returns:
            dict: TowerUtils class instance within dictionary for easy variable passing
        """
        tower_token = os.environ["TOWER_ACCESS_TOKEN"] # TODO configure secrets instead of using env variables
        client_args = TowerUtils.bundle_client_args(
            tower_token, platform="sage", debug_mode=False
        )
        tower_utils = TowerUtils(client_args)
        return {"tower_utils": tower_utils}

    @task()
    def launch_tower_workflow(tower_utils: TowerUtils, workspace_id: str):
        """
        Launches tower workflow

        Args:
            tower_utils (sagetasks.nextflowtower.utils.TowerUtils): TowerUtils class instance
            workspace_id (str): Workspace ID for tower run
        """
        tower_utils.open_workspace(workspace_id)
        tower_utils.launch_workflow(
            compute_env_id="1QX5bol8rZHBZkTAEIvQts",
            pipeline="Sage-Bionetworks-Workflows/nf-validate",
            revision="main",
            profiles=["docker"],
            user_secrets=["SYNAPSE_AUTH_TOKEN"], # TODO need to get a workspace secret in the HTAN tower workspace that has more access - don't have permission to create one
        )

    tower_utils = open_tower_workspace()
    launch_tower_workflow(tower_utils["tower_utils"], "253119656982040")


nf_validate_dag = nf_validate_dag()
