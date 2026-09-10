# AWS S3 Setup Guide for Hospital Media Storage

This guide walks you through setting up AWS S3 for persistent media file storage on Railway.

## Step 1: Create an AWS Account
- Go to [AWS Console](https://aws.amazon.com)
- Sign up or log in
- Confirm your account

## Step 2: Create an S3 Bucket

1. Go to [AWS S3 Console](https://s3.amazonaws.com)
2. Click **"Create bucket"**
3. Bucket name: `hospital-media-storage` (must be globally unique, so consider adding a suffix like `-yourname`)
4. Region: `us-east-1` (or your preferred region)
5. Click **"Create bucket"**

## Step 3: Configure Bucket Permissions

1. In S3 console, select your bucket
2. Go to **Permissions** tab
3. Click **Block public access** → Click **Edit**
4. **Uncheck** "Block all public access"
5. Click **Confirm**
6. Go to **Bucket Policy** and add this policy (replace `hospital-media-storage` with your bucket name):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::hospital-media-storage/*"
    }
  ]
}
```

7. Click **Save**

## Step 4: Create IAM User for S3 Access

1. Go to [AWS IAM Console](https://console.aws.amazon.com/iam)
2. Click **Users** → **Create user**
3. Username: `hospital-s3-user`
4. Click **Next**
5. Click **Attach policies directly**
6. Search for and select: `AmazonS3FullAccess`
7. Click **Next** → **Create user**

## Step 5: Create Access Keys

1. Click on the newly created user (`hospital-s3-user`)
2. Go to **Security credentials** tab
3. Click **Create access key**
4. Select **Application running on AWS compute service** (or other)
5. Click **Next**
6. Click **Create access key**
7. **COPY AND SAVE THESE VALUES** (you can only see them once):
   - Access Key ID
   - Secret Access Key

⚠️ **IMPORTANT**: Store these securely! Do NOT commit them to Git or share publicly.

## Step 6: Configure Railway Environment Variables

1. Go to your [Railway Project Dashboard](https://railway.app)
2. Select your **hospital** project
3. Go to **Variables** section
4. Add these environment variables:

```
USE_S3=True
AWS_ACCESS_KEY_ID=<your-access-key-id-from-step-5>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key-from-step-5>
AWS_STORAGE_BUCKET_NAME=hospital-media-storage
AWS_S3_REGION_NAME=us-east-1
```

Replace:
- `<your-access-key-id-from-step-5>` with the Access Key ID from Step 5
- `<your-secret-access-key-from-step-5>` with the Secret Access Key from Step 5
- `hospital-media-storage` if you used a different bucket name

5. Click **Save**

## Step 7: Deploy

Railway will automatically redeploy when you save environment variables.

Watch the deployment in your Railway dashboard. You should see:
- Dependencies installing (including `boto3` and `django-storages`)
- `collectstatic` running
- App starting successfully

## Step 8: Test

1. Go to your hospital app on Railway
2. Upload a new image in the admin panel
3. Check that it displays correctly
4. (Optional) Go to AWS S3 console and verify the file appears in your bucket

## Troubleshooting

### Files still not loading
- Check Railway logs for S3 errors
- Verify S3 bucket name is correct in environment variables
- Make sure AWS credentials are correct
- Confirm bucket policy allows public read access

### 403 Forbidden errors
- Check bucket permissions (should allow public-read)
- Verify IAM user has S3FullAccess policy

### New environment variables not taking effect
- Force a redeploy in Railway: Deployments → Trigger Deploy

## Files Storage Behavior

- **Old media files** (`/media/` folder): Served locally (won't persist across restarts)
- **New uploads** after S3 setup: Stored in S3 (persists permanently)
- **Static files** (CSS, JS): Served by WhiteNoise (collected during build)

## To Disable S3 Later

Remove or set `USE_S3=False` in Railway variables and redeploy.

## Cost Estimate

AWS S3 pricing (as of 2026):
- Storage: ~$0.023 per GB/month
- Data transfer: ~$0.09 per GB (outbound)

For a small hospital app with a few MB of uploads, expect $1-5/month.

---

Need help? Check AWS S3 documentation: https://docs.aws.amazon.com/s3/
