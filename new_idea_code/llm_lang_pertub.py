from agents import Agent, ModelSettings, Runner
from pydantic import BaseModel
import os
os.environ["OPENAI_API_KEY"] = ""

AGENT_SYS_PROMPT = """You are a language perturbation module for evaluating zero-shot generalization in embodied AI systems.

Your task is to rephrase a robot task instruction in a way that:
- Preserves the exact physical goal and success condition of the original task.
- Does NOT introduce any new objects, actions, constraints, ordering, or tools.
- Does NOT simplify the instruction.
- Makes the wording slightly indirect, less canonical, or mildly ambiguous in phrasing, while remaining interpretable.

Guidelines:
- The rephrased instruction must still describe the same task that would be considered successful under the original evaluation.
- You may change sentence structure, use less direct verbs, or add mild indirection.
- Do NOT add temporal requirements (e.g., “slowly”, “carefully”, “after that”).
- Do NOT add spatial constraints unless they are already present in the original instruction.
- Do NOT add extra steps or goals.
- Do NOT remove any required action.
- The end goal in both the original task and the rephrased task should be the same, but described in a slightly different way

Output format (strict):
{
  "rephrased_output": "<single rephrased instruction string>"
}

If you cannot produce a valid rephrasing without changing the task semantics, return the original instruction unchanged."""
class rephrase_task_output(BaseModel):
  rephrased_output:str

class Language_Pertubration_Agent:
  def __init__(self) -> None:
    self.agent = Agent(
      name="Language Perturbation",
      model="gpt-5-mini",
      instructions=AGENT_SYS_PROMPT
      output_type=rephrase_task_output
    )
    
  def perturbate(self, original_task:str) ->str:
    response = Runner.run_sync(self.agent, original_task)
    return str(dict(response.final_output)["rephrased_output"])
    
