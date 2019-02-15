# HaaS - Proof of Concept for Horovod-as-a-Service
## POC Tasks
1. Manual Setup and Testing:
The objective of this task is to determine if the cluster and model works, as well as what resources need to be added or removed to ensure that solution actually works.
- [ ] Create a test console (Cloud9) and verify that the model (`keras_retinanet`) works using the `deeplearning-cfn` template.
>__Note:__ The console will be removed omnce the entire process is automated.
- [ ] Verify what the final `run.sh` and `configure.sh` scripts will eventually look like and test them.
- [ ] Verify what resources the CloudFormation template deploys.
- [ ] Verify and test what resources need to be manually deployed and start looking at how this can be automated either through CloudFormation or with Lambda.