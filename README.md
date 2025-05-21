# 📧 AWS Serverless Email Application

A fault-tolerant serverless email notification system built with **S3, API Gateway, Lambda, Step Functions, SES, and SNS**. Users submit a contact form (hosted on S3), triggering an API Gateway endpoint that orchestrates email delivery via Step Functions and SES.

[![AWS](https://img.shields.io/badge/AWS-FF9900?logo=amazonaws&logoColor=white)](https://aws.amazon.com)

---

## 📌 Objectives
✅ Configure AWS SES
- **Verify sender email**
  
✅ Build Serverless Backend
- **Create Lambda function with SES permissions**
- **Implement Step Functions for fault-tolerant workflows**

✅ Secure API Gateway
- **Deploy REST API with CORS**

✅ Deploy Static Frontend
- **Host on S3 with public access (demo) or CloudFront (production)**
- **Configure CORS for API calls**

---

## 🛠️ Technologies Used
| Service               | Use Case                          |
|-----------------------|-----------------------------------|
| **Amazon S3**         | Host static frontend (HTML/CSS/JS)|
| **API Gateway**       | REST endpoint for form submissions|
| **AWS Lambda**        | Send emails via SES               |
| **Step Functions**    | Orchestrate email workflow        |
| **Amazon SES**        | Email delivery service            |

---

## 🏗️ Architecture
![Architecture Diagram](diagram/ServerlessApplication.png)

---

## 📋 Steps
1. Configure SES
    - Go to SES → Verify Email Address (confirm via inbox).
2. Create Lambda Function
    - Write Python code to send emails via SES.
    - Attach IAM role with ses:SendEmail and logging permissions.
3. Build Step Functions Workflow
    - Define state machine with retries/error handling.
    - Connect to Lambda.
4. Deploy API Gateway
    - Create REST API with POST method.
    - Enable CORS and redeploy.
5. Host Frontend on S3
    - Upload index.html with API Gateway endpoint.
    - Set bucket policy for public read access (or use CloudFront).
6. Test & Monitor
    - Submit form → Check email delivery.

---

## 📸 Visuals
| Results | Image |
|-------------|-------|
| S3 Static Website | ![Alert](images/Topic.png) |
| Lambda Test Email | ![Alert](images/AWSBudgetSNS.png) |
| S3 Static Website Email | ![Alert](images/LambdaEmail.png) |

---

## 🚀 Deployment

### Prerequisites
- AWS Account with SES verified email(s)
- AWS CLI configured (`aws configure`)
- AWS SAM CLI installed (`sam --version`)

### 1. Backend Deployment
```bash
cd backend
sam build
sam deploy --guided
```
> Follow prompts to set stack name/region. Note the API Gateway endpoint output.

### 2. Frontend Deployment
1. **Update `frontend/script.js`** with your API Gateway endpoint:
   ```javascript
   const API_URL = "https://YOUR_API_ID.execute-api.REGION.amazonaws.com/prod/sendEmail";
   ```

2. **Sync to S3**:
   ```bash
   aws s3 sync frontend/ s3://YOUR_BUCKET_NAME --acl public-read
   ```

3. **Set up CloudFront** (Optional but recommended):
   - Create distribution with S3 origin and OAI.
   - Enforce HTTPS and set `index.html` as default root.

---

## 🔒 Security Hardening
| Step                  | Action                                  |
|-----------------------|-----------------------------------------|
| **CloudFront + OAI**  | Replace public S3 access with CDN       |
| **API Gateway Keys**  | Enable and enforce `x-api-key` header   |
| **Least-Privilege**   | Restrict SES/Lambda permissions         |
| **HTTPS Enforcement** | Redirect HTTP → HTTPS in CloudFront     |

---

## 📊 Monitoring
```yaml
# Example CloudWatch Alarms (AWS SAM snippet)
Alarms:
  EmailFailures:
    Type: AWS::CloudWatch::Alarm
    Properties:
      MetricName: ExecutionsFailed
      Namespace: AWS/States
      Threshold: 1
      ComparisonOperator: GreaterThanThreshold
```

---

## 💡 Extending the Project
- **Add Database**: Log submissions to DynamoDB.
- **Templated Emails**: Use SES templates for consistent formatting.
- **SMS Alerts**: Trigger SNS on failures.

---

## 📜 License
MIT License. See [LICENSE](./LICENSE) for details.

---

## 🙏 Credits
- Inspired by [AWS Serverless Patterns](https://serverlessland.com)
- [AWS SAM Template Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html)
