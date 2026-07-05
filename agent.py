import os
import json
from google import genai
from google.genai import types

# 1. Client Initialize (Ye aapki set ki hui GEMINI_API_KEY ko automatic utha lega)
client = genai.Client()

# 2. TOOL (Function): Jo agent khud manually kaam karne ke badle automatically execute karega
def save_script_to_file(filename: str, content: str) -> str:
    """Saves the generated script content to a local file on the disk."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully saved script to {filename}"
    except Exception as e:
        return f"Failed to save file: {str(e)}"

# Tools ka map banaya taaki agent ise pehchan sake
tools_map = {
    "save_script_to_file": save_script_to_file
}

# 3. Agent Loop Execution
def run_concierge_agent(user_prompt: str):
    print("🤖 Concierge Agent is processing your request...")
    
    system_instruction = (
        "You are a specialized Personal Content Concierge. Your job is to take a raw topic, "
        "turn it into a highly engaging short-form mystery/riddle script, and then use the "
        "provided `save_script_to_file` tool to save that output into a file named 'generated_script.json'."
    )
    
    # Model configuration aur tool binding
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            tools=[save_script_to_file], # Agent ko tool dena
            temperature=0.7
        )
    )
    
    # Check karna ki kya Agent ne file save karne wala tool call kiya?
    if response.function_calls:
        for call in response.function_calls:
            print(f"⚡ Agent decided to execute tool: {call.name}")
            tool_to_call = tools_map[call.name]
            # Code automatically file ko disk par write kar dega
            tool_result = tool_to_call(**call.args)
            print(f"✅ Tool Output: {tool_result}")
    else:
        print("Response received without tool call:")
        print(response.text)

if __name__ == "__main__":
    # Test Prompt: Aap yahan koi bhi topic badal sakte hain, ye usi par script auto-generate kar dega
    sample_topic = "Create a unique logic riddle about a locked room for an IQ bait video script."
    run_concierge_agent(sample_topic)