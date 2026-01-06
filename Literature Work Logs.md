# Logs of My Research (Take-Home Assignment - PSU)

The main idea is to merge everything (control, perception, reasoning and language) into one unified model.

### Types of models that are the SOTA:
- Vision Language Action Models (VLAs)
- World Models

Vision Language Action Models: Vision-Language-Action (VLA) models unify perception and motor control into a single transformer-based architecture.

World Models: understand the dynamics of the real world, including physics and spatial properties through input data, including text, image, video, and movement, to generate videos that simulate realistic physical environments. World models are used to generate custom synthetic data or downstream AI models for training robots and autonomous vehicles.


### Some problems that are right now the main focus on the research community:
- Lack of Physical Data for large-scale generalization
- Cross-Embodiment Generalization
- Zero-shot Task Generalization
- Sim2Real Transfer
- Reasoning and Self-correction


### Generalization Specific Problems:
- Cross-Embodiment Generalization
- Sim2Real Transfer
- Zero-shot Task Generalization


> ## Generalization Problem Choice:
> There are two problems that I find most interesting and are the most important ones right now: 
> - Cross-Embodiment Generalization
> - Zero-shot Task Generalization. 


**Background**: While current models can perform tasks they were specifically trained for (in-distribution), the "holy grail" of the field is enabling a robot to perform a task it has never seen before, using a body (morphology) it was not trained on. The central challenge is to overcome the Out-of-Distribution (OOD) Gap. This is not just about recognizing a new image, it is about generalist models that can do the following: 

- Generalize to Novel Tasks: Following a language command for a skill, like "zest the lemon", without ever having seen a single demonstration of "zesting."

- Generalize to Unseen Environments: Operating in a new kitchen or warehouse (essentially a new environment) with different lighting and layouts without any priors about mapping.

- Cross-Embodiment Transfer: A single AI "brain" controlling different robots, such as a humanoid-arm, an entire humanoid, or a mobile platform, without being fine-tuned for each specific hardware's physics.


> To Sum-up in technical terms: Training a single policy that can generalize across different robot morphologies (different arms, grippers, mobile bases, humanoids) without retraining.


## Literature Work:


### Top Models:

| Name    | Description  | Type          | Paper/Website Link | GitHub Link                                           |
|---------|--------------|---------------|--------------------|-------------------------------------------------------|
| OpenVLA | An Open-Source Vision-Language-Action Model | Model         | [ArXiv](https://arxiv.org/abs/2406.09246) | [GitHub](https://github.com/openvla/openvla)           |
| π0      | A Vision-Language-Action Flow Model for General Robot Control | Model         | [Website](https://www.pi.website/download/pi0.pdf)      | Proprietary |
| RDT2    | Enabling Zero-Shot Cross-Embodiment Generalization by Scaling Up UMI Data | Model & Data   | [Website](https://rdt-robotics.github.io/rdt2/#)      | [GitHub](https://github.com/thu-ml/RDT2)               |
| Nvidia Groot N1   | Open vision-language-action (VLA) model for generalized humanoid robot skills | Model & Data | [Paper](https://arxiv.org/abs/2503.14734)  |   [GitHub](https://github.com/NVIDIA/Isaac-GR00T?tab=readme-ov-file)  |
| ECoT    |   OpenVLA-based Embodied Chain-of-Thought |   Model & Data    | [Paper](https://arxiv.org/pdf/2407.08693) | [GitHub](https://github.com/MichalZawalski/embodied-CoT/)   |


### Datasets and Benchmarks:
| Name  | Link |
|-------|------|
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models | [Website](https://robotics-transformer-x.github.io/) |
| RDT2: Enabling Zero-Shot Cross-Embodiment Generalization by Scaling Up UMI Data | [Website](https://rdt-robotics.github.io/rdt2/#) | 


### Latest Research Papers on Generalization:
| Name    |     Venue     | Paper/Website Link | GitHub Link |
|---------|---------------|------------------|------------|
| OpenVLA |      CoRL     | [ArXiv](https://arxiv.org/abs/2406.09246) | [GitHub](https://github.com/openvla/openvla)           |
| Robotics Control via Embodied Chain of Thought Reasoning | CoRL | [PDF](./Literature_Review/Papers/2407.08693v3.pdf) | [Embodied-CoT](https://github.com/MichalZawalski/embodied-CoT/) |
| TrackVLA++: Unleashing Reasoning and Memory Capabilities in VLA Models for Embodied Visual Tracking | ArXiv | [PDF](./Literature_Review/Papers/2510.07134.pdf) | Not Released Yet |
| DEEPTHINKVLA: ENHANCING REASONING CAPABILITY OF VISION-LANGUAGE-ACTION MODELS | ArXiv | [PDF](./Literature_Review/Papers/2511.15669.pdf) | [DeepThinkVLA](https://github.com/OpenBMB/DeepThinkVLA) |
| ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation | ArXiv | [PDF](./Literature_Review/Papers/2512.02013.pdf) | Not Released Yet |


## Replication:
- Selected the [OpenVLA](https://github.com/openvla/openvla) as the main replication code, because it is being used by almost every other paper for baseline. 
- Chose Google Colab as both my laptop and PC does not have enough VRAM to load OpenVLA-7B model.
- Colab has Nvidia T4 (15GB VRAM) and it's architecture does not support flash-attention (>=Ampere-based GPUs are required) and bitsandbytes are not supported with OpenVLA's environment so sticking wit full precision, and without flash-attention.
> - Due to the size of the evaluation and episodes per task, I have reduced the number of tasks to only 1 and episodes to 5 instead of original 10 tasks and 50 episodes. This will make it feasible to run and produce some reproducible and comparable results, instead of complete tasks which will take 5-6 days based on the current available resources, and colab also does not allow background execution.

### Configurations:
- `Model`: `openvla/openvla-7b-finetuned-libero-object`
- `Task`: `libero-object`
- `Tasks_ID`: 1
- `Episodes`: 5
- `Model Precision`: Full 16-bit

### Results Logs:
| Task id | Episode # | Task Prompt | Success | Accuracy &uarr; |
|--------|-----------|-------------|---------|---------|
| 1 | 1 | pick up the alphabet soup and place it in the basket | <span style="color: green;">True</span> | 100% |
| 1 | 1 | pick up the alphabet soup and place it in the basket | <span style="color: green;">True</span>  | 100% |
| 1 | 1 | pick up the alphabet soup and place it in the basket | <span style="color: green;">True</span>  | 100% |
| 1 | 1 | pick up the alphabet soup and place it in the basket | <span style="color: green;">True</span>  | 100% |
| 1 | 1 | pick up the alphabet soup and place it in the basket | <span style="color: red;">False</span>  | 80% |

### Comparison with paper results:
| Paper Accuracy | Replication Accuracy |
|----------------|----------------------|
|88.4% | 80% |

The numbers are mentioned here: [Paper Results Table](https://github.com/openvla/openvla?tab=readme-ov-file#openvla-fine-tuning-results)
These results are based on 10 Tasks and 50 episodes per task and Replication results are based on only 1 Task and 5 episodes because of the the resources that I had access to, to replicate these results. Unfortunately, Google Colab keep running out of credits and I have to wait hours to try again later. 

<h1>Sample Outputs</h1>
<h2>Task Prompt: pick up the alphabet soup and place it in the basket</h2>

| ![](./output/2026_01_05-21_05_25--episode1--successTrue--taskpick_up_the_alphabet_soup_and_place_it_in_the_bask-ezgif.com-video-to-gif-converter.gif) | ![](./output/2026_01_05-21_05_25--episode3--successTrue--taskpick_up_the_alphabet_soup_and_place_it_in_the_bask-ezgif.com-video-to-gif-converter.gif) | ![](./output/2026_01_05-21_05_25--episode5--successFalse--taskpick_up_the_alphabet_soup_and_place_it_in_the_bask-ezgif.com-video-to-gif-converter.gif) |
|:--:|:--:|:--:|
| **Episode:** 1, **Task:** 1, **Success:** True | **Episode:** 3, **Task:** 1, **Success:** True | **Episode:** 5, **Task:** 1, **Success:** False |


<h2>Results Graph</h2>
<div style="display: flex; justify-content: center; gap: 8px;">
  <div style="text-align: center;">
    <img src="./output/openvla_replication_accuracy_per_episode.png" alt="">
  </div>


</div>


</br>

## New Ideas:

These ideas should not require huge amount of compute, preferably within Google Colab, otherwise it would be impossible to do anything that requires a lot of compute and time.


1. Language Perturbation on Task Efficiency
    - Check the performance of the model perturbation of Task Prompt. Use another model to apply perturbation on runtime while keep the main goal intact. This will test the robustness of the model to language perturbation to effectively show model's zero-shot performance on the same task and goal but different and slightly confusing wording.  
2. Visual Inconsistency Invariance:
    - Check model's robustness to visual changes that are not in the original dataset like changing the color of the basket's or soup's texture. This will test the model's vision generalization ability.  
