This folder contains only the files from original OpenVLA code that were changed in order to complete this assignment and implement the new idea.

## Files:
- [run_libero_eval.py](./run_libero_eval.py) This file contains the main evaluation code that can be used to run the evaluation on LIBERO Simulation based benchmarks.
- [openvla_utils.py](./openvla_utils.py) this file contains the updated code of utility functions that I changes in order to run on colab and also for the implementation of new idea.
- [llm_lang_pertub.py](./llm_lang_pertub.py) contains the code for the Language Perturbation Shift module. This code contains a code for OpenAI Agents SDK-based agent that is specifically designed and prompted carefully for this task.
  - This file contains an agent that return the output in a structued format that can be easily used in downstream tasks.
  - The system prompt of the agent is also present in this file that is used on the runtime to generate variants of the `Task_Description`.


### Files' Placement in original code
Due to large codebase of the OpenVLA and LIBERO, I am just sharing the files that I used for replication and edited to implement my new idea. The following table shows where each of this file should be placed in the original OpenVLA code repo in order to run it successfully:

| File | Destination Path |
|------|------------------|
|[run_libero_eval.py](./run_libero_eval.py) | [openvla/experiments/robot/libero](https://github.com/openvla/openvla/tree/main/experiments/robot/libero) |
| [openvla_utils.py](./openvla_utils.py) | [openvla/experiments/robot](https://github.com/openvla/openvla/tree/main/experiments/robot) |
| [llm_lang_pertub.py](./llm_lang_pertub.py) | [openvla/experiments/robot/libero](https://github.com/openvla/openvla/tree/main/experiments/robot/libero) |


### Other files in this repo:
- [colab_setup_openvla](colab_setup_openvla.txt): This file contains the bash commands to setup the OpenVLA specifically on Google Colab along with Conda, LIBERO Simulation, and LIBERO Objects dataset (~5GB).
- [graph.py](graph.py): This file contains the python code that I used to generate the graph.
- [openvla_env.yml](openvla_env.yml): This file contains the environment configurations for the conda env. 
