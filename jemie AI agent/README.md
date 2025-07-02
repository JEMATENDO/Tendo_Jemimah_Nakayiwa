# X (Twitter) Agent 🐦 By Jemimah Tendo Nakayiwa 

## 🚀 Features

- ✅ Send text posts to X/Twitter
- ✅ Authenticate using Twitter API v2
- ✅ Get authenticated user information
- ✅ Post scheduling functionality
- ✅ Comprehensive error handling
- ✅ Rate limit management
- ✅ Character count validation (280 char limit)
- ✅ Environment variable security


## 🛠️ Setup Instructions

### Step 1: Get Twitter API Credentials

1. **Create a Twitter Developer Account**
   - Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
   - Apply for a developer account (if you don't have one)

2. **Create a New App**
   - Click "Create App" or use an existing app
   - Fill in the required information

3. **Get Your API Keys**
   You'll need these 5 credentials:
   - **Bearer Token** (for API v2 access)
   - **Consumer Key** (API Key)
   - **Consumer Secret** (API Secret)
   - **Access Token** (for your account)
   - **Access Token Secret**

   Make sure your app has **Read and Write** permissions!

### Step 2: Install Dependencies

The required packages should already be installed, but if needed:

```bash
pip install tweepy==4.14.0 python-dotenv==1.0.0
```

### Step 3: Configure Credentials

1. **Copy the example file:**
   ```bash
   copy .env.example .env
   ```

2. **Edit `.env` file** and add your actual credentials:
   ```env
   TWITTER_BEARER_TOKEN=your_actual_bearer_token_here
   TWITTER_CONSUMER_KEY=your_actual_consumer_key_here
   TWITTER_CONSUMER_SECRET=your_actual_consumer_secret_here
   TWITTER_ACCESS_TOKEN=your_actual_access_token_here
   TWITTER_ACCESS_TOKEN_SECRET=your_actual_access_token_secret_here
   ```

   ⚠️ **Never commit your `.env` file to version control!**

## 📖 Usage Examples

### Basic Usage

```python
from X_agent import XAgent

# Initialize the agent
agent = XAgent()

# Check authentication
user_info = agent.get_user_info()
if "error" not in user_info:
    print(f"✅ Authenticated as: @{user_info['username']}")
    
    # Send a post
    result = agent.send_post("Hello from my X Agent! 🤖")
    
    if result.get("success"):
        print(f"✅ Post sent! URL: {result['url']}")
    else:
        print(f"❌ Error: {result.get('error')}")
else:
    print(f"❌ Authentication failed: {user_info['error']}")
```

### Running the Examples

**Run the main agent:**
```bash
python "X agent.py"
```

**Run the example usage:**
```bash
python example_usage.py
```

### Advanced Usage

```python
# Initialize with custom credentials (alternative to .env)
agent = XAgent(
    bearer_token="your_token",
    consumer_key="your_key",
    consumer_secret="your_secret",
    access_token="your_access_token",
    access_token_secret="your_access_token_secret"
)

# Schedule a post for later (simple delay)
result = agent.schedule_post("Scheduled post! ⏰", delay_minutes=5)

# Get user information
user_info = agent.get_user_info()
print(f"User ID: {user_info['user_id']}")
print(f"Username: @{user_info['username']}")
print(f"Display Name: {user_info['name']}")
```

## 🔧 API Reference

### `XAgent()`
**Initialize the agent**
```python
agent = XAgent(
    bearer_token=None,          # Optional: Bearer token
    consumer_key=None,          # Optional: Consumer key
    consumer_secret=None,       # Optional: Consumer secret
    access_token=None,          # Optional: Access token
    access_token_secret=None    # Optional: Access token secret
)
```
If parameters are not provided, the agent will use environment variables.

### `send_post(text, media_ids=None)`
**Send a text post to X**
- `text` (str): Post content (max 280 characters)
- `media_ids` (list, optional): List of media IDs to attach
- **Returns:** Dictionary with success status and post details

### `get_user_info()`
**Get authenticated user information**
- **Returns:** Dictionary with user ID, username, and display name

### `schedule_post(text, delay_minutes=0)`
**Schedule a post with a delay**
- `text` (str): Post content
- `delay_minutes` (int): Minutes to wait before posting
- **Returns:** Same as `send_post()`

## ⚠️ Important Notes

### Security
- **Never commit your `.env` file** to version control
- Keep your API credentials secure and private
- Use environment variables for production deployments
- Consider using OAuth 2.0 for user-facing applications

### Limitations
- Posts are limited to **280 characters**
- Rate limits apply (handled automatically by the agent)
- Requires Twitter API v2 access
- Media uploads not implemented in this basic version

### Error Handling
The agent includes comprehensive error handling for:
- ✅ Invalid credentials
- ✅ Text length validation
- ✅ API errors and exceptions
- ✅ Rate limiting
- ✅ Network issues

## 🐛 Troubleshooting

### Common Issues

**1. Authentication Errors**
```
❌ Error: X Agent not properly initialized. Check your credentials.
```
- **Solution:** Verify all 5 credentials are correctly set in `.env`
- Check that your app has Read and Write permissions

**2. Import Errors**
```
❌ ModuleNotFoundError: No module named 'tweepy'
```
- **Solution:** Install dependencies: `pip install tweepy python-dotenv`

**3. Text Too Long**
```
❌ Post text too long (XXX characters). Maximum is 280.
```
- **Solution:** Shorten your post text to 280 characters or less

**4. Rate Limiting**
- The agent automatically handles rate limits
- If you hit limits frequently, consider spacing out your posts

### Getting Help

1. Check the Twitter API documentation
2. Verify your API credentials in the Developer Portal
3. Test with the example files provided
4. Check the console output for detailed error messages

## 📄 License

This project is for educational and personal use. Please follow Twitter's API Terms of Service and Developer Agreement.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

---

**Happy Posting! 🐦✨**
