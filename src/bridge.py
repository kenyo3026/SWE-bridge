
from dataclasses import dataclass
from typing import Union

from minisweagent.environments.local import LocalEnvironment
from minisweagent.environments.docker import DockerEnvironment
from minisweagent.models import get_model
from minisweagent.run.extra.swebench import get_sb_environment


@dataclass
class Environment:
    local:LocalEnvironment = LocalEnvironment
    docker:DockerEnvironment = DockerEnvironment

@dataclass
class SubmissionData:
    instance_id:str
    model_name_or_path:str
    model_patch:str

class SWEBenchSubmissionBridger:

    # def __init__(self, env:Union[LocalEnvironment, DockerEnvironment]):
    #     self.env = self.setup_env(env)

    def setup_env(self, env):
        if isinstance(env, str):
            try:
                env = Environment.__getattribute__(env)
            except:
                raise ValueError()
        return env

    def format_submission(
        self,
        instance: dict,
        config: dict,
    ):
        instance_id = instance["instance_id"]
        model = get_model(config=config.get("model", {}))
        # task = instance["problem_statement"]

        env = get_sb_environment(config, instance)
        model_patch = env.execute('git add -A && git diff --cached')
        return SubmissionData(
            instance_id=instance_id,
            model_name_or_path=model.config.model_name,
            model_patch=model_patch['output'],
        ).__dict__


if __name__ == '__main__':
    import yaml
    import datasets

    with open('./minisweagent/config/default.yaml', 'r') as f:
        config = yaml.safe_load(f)

    if not 'model_name' in config.get('model', {}):
        config['model']['model_name'] = 'gpt-4o'
    if not 'cwd' in config.get('environment', {}):
        config['environment']['cwd'] = '/testbed'

    dataset_name_or_path = 'princeton-nlp/SWE-bench_Verified'
    split = 'test[:1]'
    dataset = datasets.load_dataset(dataset_name_or_path, split=split)

    instance = dataset[0]
    formatter = SWEBenchSubmissionBridger()
    submission_data = formatter.format_submission(instance, config)

    for key, value in submission_data.items():
        print(f'\033[92m{key:<50}\033[0m: {value}')