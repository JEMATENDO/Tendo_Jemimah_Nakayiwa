import tweepy
import os
from datetime import datetime
import json
from dotenv import load_dotenv


load_dotenv()

class XAgent:
   
    def __init__(self, bearer_token=None, consumer_key=None, consumer_secret=None, 
                 access_token=None, access_token_secret=None):
        self.bearer_token = bearer_token or os.getenv('TWITTER_BEARER_TOKEN')
        self.consumer_key = consumer_key or os.getenv('TWITTER_CONSUMER_KEY')
        self.consumer_secret = consumer_secret or os.getenv('TWITTER_CONSUMER_SECRET')
        self.access_token = access_token or os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = access_token_secret or os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        
        self.client = None
        self._setup_client()
    
    def _setup_client(self):
        if not all([self.bearer_token, self.consumer_key, self.consumer_secret, 
                   self.access_token, self.access_token_secret]):
            print("Warning: Not all Twitter API credentials are provided.")
            print("Please set environment variables or pass credentials to constructor:")
            print("- TWITTER_BEARER_TOKEN")
            print("- TWITTER_CONSUMER_KEY")
            print("- TWITTER_CONSUMER_SECRET")
            print("- TWITTER_ACCESS_TOKEN")
            print("- TWITTER_ACCESS_TOKEN_SECRET")
            return
        
        try:
            self.client = tweepy.Client(
                bearer_token=self.bearer_token,
                consumer_key=self.consumer_key,
                consumer_secret=self.consumer_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
                wait_on_rate_limit=True
            )
            print("✅ X Agent initialized successfully!")
        except Exception as e:
            print(f"❌ Error initializing X Agent: {e}")
            self.client = None
    
    def send_post(self, text, media_ids=None):
        if not self.client:
            return {"error": "X Agent not properly initialized. Check your credentials."}
        
        if len(text) > 280:
            return {"error": f"Post text too long ({len(text)} characters). Maximum is 280."}
        
        try:
            response = self.client.create_tweet(text=text, media_ids=media_ids)
            
            if response.data:
                return {
                    "success": True,
                    "tweet_id": response.data['id'],
                    "text": text,
                    "timestamp": datetime.now().isoformat(),
                    "url": f"https://twitter.com/user/status/{response.data['id']}"
                }
            else:
                return {"error": "Failed to create tweet", "response": response}
                
        except Exception as e:
            return {"error": f"Error sending post: {str(e)}"}
    
    def get_user_info(self):
        if not self.client:
            return {"error": "X Agent not properly initialized"}
        
        try:
            user = self.client.get_me()
            if user.data:
                return {
                    "success": True,
                    "user_id": user.data.id,
                    "username": user.data.username,
                    "name": user.data.name
                }
            else:
                return {"error": "Could not retrieve user information"}
        except Exception as e:
            return {"error": f"Error getting user info: {str(e)}"}
    
    def schedule_post(self, text, delay_minutes=0):
        import time
        
        if delay_minutes > 0:
            print(f"📅 Post scheduled to be sent in {delay_minutes} minutes...")
            time.sleep(delay_minutes * 60)
        
        return self.send_post(text)


def main():
    print("🐦 X (Twitter) Agent")
    print("=" * 50)
    
    agent = XAgent()
    
    user_info = agent.get_user_info()
    if "error" in user_info:
        print(f"❌ {user_info['error']}")
        print("\n📋 Setup Instructions:")
        print("1. Create a Twitter Developer account at https://developer.twitter.com")
        print("2. Create a new app and get your API keys")
        print("3. Set the following environment variables:")
        print("   - TWITTER_BEARER_TOKEN")
        print("   - TWITTER_CONSUMER_KEY")
        print("   - TWITTER_CONSUMER_SECRET")
        print("   - TWITTER_ACCESS_TOKEN")
        print("   - TWITTER_ACCESS_TOKEN_SECRET")
        return
    
    print(f"✅ Authenticated as: @{user_info['username']} ({user_info['name']})")
    
    sample_text = f"Hello from my X Agent! 🤖 Posted at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    print(f"\n📝 Sending post: '{sample_text}'")
    result = agent.send_post(sample_text)
    
    if result.get("success"):
        print(f"✅ Post sent successfully!")
        print(f"🔗 URL: {result['url']}")
        print(f"🆔 Tweet ID: {result['tweet_id']}")
    else:
        print(f"❌ Error: {result.get('error')}")


if __name__ == "__main__":
    main()