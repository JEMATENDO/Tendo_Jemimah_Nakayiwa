
import sys
import os
import importlib.util

# Load the X agent module dynamically
spec = importlib.util.spec_from_file_location("x_agent", "X agent.py")
x_agent_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x_agent_module)

# Now we can use XAgent from the module
XAgent = x_agent_module.XAgent

def example_usage():
   
    
    
    agent = XAgent()
    
    # Check if we're authenticated
    user_info = agent.get_user_info()
    if "error" in user_info:
        print("❌ Authentication failed. Please check your credentials.")
        return
    
    print(f"✅ Authenticated as: @{user_info['username']}")
    
    # Send a simple post
    post_text = "Hello from my Python X Agent! 🐍🤖"
    result = agent.send_post(post_text)
    
    if result.get("success"):
        print(f"✅ Post sent successfully!")
        print(f"🔗 URL: {result['url']}")
    else:
        print(f"❌ Error: {result.get('error')}")

if __name__ == "__main__":
    example_usage()
