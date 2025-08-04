# n8n LinkedIn Page Post Workflow

This repository contains a comprehensive n8n workflow for automating posts to LinkedIn company pages. The workflow includes media upload, error handling, notifications, and logging capabilities.

## 🚀 Features

- **Automated LinkedIn Page Posting**: Post text and images to LinkedIn company pages
- **Media Upload Support**: Automatically upload and attach images to posts
- **Error Handling**: Robust error handling with notifications
- **Logging**: Track all posts in Google Sheets for analytics
- **Notifications**: Slack notifications for success and failure
- **Scheduled Posting**: Configurable scheduling for automated posting
- **Organization Management**: Automatically retrieve company/organization IDs

## 📋 Prerequisites

Before setting up this workflow, ensure you have:

1. **n8n Instance**: Self-hosted or cloud instance
2. **LinkedIn Developer App**: For API access
3. **LinkedIn Company Page**: Admin access to the page you want to post to
4. **Google Sheets**: For logging (optional)
5. **Slack Workspace**: For notifications (optional)

## 🛠️ Setup Instructions

### 1. LinkedIn API Setup

1. **Create LinkedIn Developer Application**:
   - Go to [LinkedIn Developer Portal](https://developer.linkedin.com/)
   - Create a new app
   - Request access to "Share on LinkedIn" and "Marketing Developer Platform"
   - Add your company page to the app

2. **Configure OAuth Scopes**:
   Required scopes:
   - `w_organization_social` - Post on behalf of organization
   - `r_organization_social` - Read organization info
   - `r_basicprofile` - Basic profile access

3. **Get OAuth Credentials**:
   - Client ID
   - Client Secret
   - Redirect URL (use your n8n instance URL + `/rest/oauth2-credential/callback`)

### 2. n8n Credentials Configuration

#### LinkedIn OAuth2 API Credential
```json
{
  "name": "linkedin-credentials",
  "type": "linkedInOAuth2Api",
  "data": {
    "clientId": "your-linkedin-client-id",
    "clientSecret": "your-linkedin-client-secret"
  }
}
```

#### Google Sheets OAuth2 API Credential (Optional)
```json
{
  "name": "google-sheets-credentials",
  "type": "googleSheetsOAuth2Api",
  "data": {
    "clientId": "your-google-client-id",
    "clientSecret": "your-google-client-secret"
  }
}
```

#### Slack API Credential (Optional)
```json
{
  "name": "slack-credentials",
  "type": "slackApi",
  "data": {
    "accessToken": "your-slack-bot-token"
  }
}
```

### 3. Import the Workflow

1. Copy the content from `linkedin-page-post-workflow.json`
2. In n8n, go to **Workflows** → **Import from URL/File**
3. Paste the JSON content
4. Save the workflow

### 4. Configure the Workflow

#### Update Post Content
Modify the "Prepare Post Content" node:
```javascript
{
  "post_text": "Your custom post content with hashtags #YourHashtag",
  "image_url": "https://your-domain.com/image.jpg",
  "organization_name": "Your Company Name"
}
```

#### Update Google Sheets Configuration
In the "Log to Google Sheets" node:
- Replace `your-google-sheet-id-here` with your actual Google Sheet ID
- Ensure the sheet has columns: Timestamp, Organization, Post ID, Content Preview, Status, Error

#### Configure Scheduling
Modify the "Schedule Trigger" node:
- Set your desired posting frequency
- Consider time zones and optimal posting times

## 📊 Workflow Structure

### Main Workflow Steps

1. **Schedule Trigger**: Initiates the workflow at specified intervals
2. **Prepare Post Content**: Sets up the post text, image URL, and metadata
3. **Get Organization ID**: Retrieves LinkedIn organization/company page ID
4. **Download Image**: Fetches the image from the provided URL
5. **Register Upload**: Registers media upload with LinkedIn API
6. **Extract Media Info**: Processes upload response data
7. **Upload Media**: Uploads the image to LinkedIn's media service
8. **Post to LinkedIn Page**: Creates the actual LinkedIn post
9. **Check Post Success**: Validates if the post was successful
10. **Success/Error Notifications**: Sends appropriate notifications
11. **Log to Google Sheets**: Records the post attempt for analytics

### Node Configurations

#### LinkedIn Post Node
```javascript
{
  "resource": "post",
  "operation": "create",
  "organizationUrn": "={{$node[\"Get Organization ID\"].json[\"id\"]}}",
  "text": "={{$node[\"Prepare Post Content\"].json[\"post_text\"]}}",
  "additionalFields": {
    "visibility": "PUBLIC",
    "content": {
      "media": [{
        "status": "READY",
        "media": "={{$node[\"Upload Media\"].json[\"mediaId\"]}}"
      }]
    }
  }
}
```

## 🔄 Workflow Variations

### 1. Text-Only Posts (No Media)

For text-only posts, you can simplify the workflow by removing:
- Download Image node
- Register Upload node
- Upload Media node
- Extract Media Info node

### 2. Multiple Image Support

To support multiple images, modify the media array:
```javascript
"content": {
  "media": [
    {
      "status": "READY",
      "media": "={{$node[\"Upload Media 1\"].json[\"mediaId\"]}}"
    },
    {
      "status": "READY", 
      "media": "={{$node[\"Upload Media 2\"].json[\"mediaId\"]}}"
    }
  ]
}
```

### 3. Content from External Sources

Replace the "Prepare Post Content" node with:
- **RSS Feed**: Pull content from blog feeds
- **Google Sheets**: Read content from spreadsheets
- **Airtable**: Use Airtable as content management
- **WordPress**: Fetch latest blog posts

### 4. AI-Generated Content

Add OpenAI or other AI nodes to generate content:
```javascript
// Add before "Prepare Post Content"
{
  "name": "Generate AI Content",
  "type": "n8n-nodes-base.openAi",
  "parameters": {
    "resource": "text",
    "operation": "complete",
    "prompt": "Write a professional LinkedIn post about {{topic}}"
  }
}
```

## 🎯 Best Practices

### Content Guidelines
- Keep posts between 150-300 characters for optimal engagement
- Include 3-5 relevant hashtags
- Add a call-to-action (CTA)
- Use emojis sparingly but effectively
- Include branded visuals

### Posting Frequency
- **B2B Companies**: 1-2 posts per day
- **B2C Companies**: 2-3 posts per day
- **Optimal Times**: Tuesday-Thursday, 8-10 AM and 12-2 PM (local time)

### Image Specifications
- **Dimensions**: 1200x630 pixels (recommended)
- **Format**: JPEG or PNG
- **Size**: Under 5MB
- **Aspect Ratio**: 1.91:1 for single images

### Error Handling
- Implement retry logic for failed uploads
- Set up monitoring for API rate limits
- Use webhook notifications for critical failures
- Log all activities for debugging

## 📈 Analytics and Monitoring

### Google Sheets Logging
The workflow logs the following data:
- Timestamp
- Organization name
- Post ID (if successful)
- Content preview
- Status (SUCCESS/FAILED)
- Error message (if any)

### Performance Metrics
Monitor these KPIs:
- Post success rate
- Engagement metrics (fetch via LinkedIn API)
- Optimal posting times
- Content performance by type

## 🚨 Troubleshooting

### Common Issues

#### 1. Authentication Errors
- Verify LinkedIn app permissions
- Check OAuth scopes
- Ensure company page is added to the app
- Refresh OAuth tokens

#### 2. Media Upload Failures
- Check image format and size
- Verify image URL accessibility
- Ensure proper Content-Type headers
- Test with different image sources

#### 3. Organization ID Issues
- Confirm admin access to LinkedIn page
- Verify the organization endpoint response
- Check for multiple organizations

#### 4. Rate Limiting
- Implement exponential backoff
- Reduce posting frequency
- Monitor API usage limits
- Use multiple apps if needed

### Debug Steps
1. Enable workflow debug mode
2. Check individual node outputs
3. Verify API responses
4. Test with manual triggers
5. Review error logs

## 🔒 Security Considerations

- Store credentials securely in n8n
- Use environment variables for sensitive data
- Implement IP whitelisting if possible
- Regular credential rotation
- Monitor for unauthorized access
- Use HTTPS for all endpoints

## 📚 Additional Resources

- [LinkedIn Marketing API Documentation](https://docs.microsoft.com/en-us/linkedin/marketing/)
- [n8n Documentation](https://docs.n8n.io/)
- [LinkedIn Best Practices](https://business.linkedin.com/marketing-solutions/best-practices)
- [n8n Community Forum](https://community.n8n.io/)

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this workflow.

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This workflow is for educational and automation purposes. Ensure compliance with LinkedIn's Terms of Service and API usage policies. The authors are not responsible for any misuse or violations of platform policies.
