# 🚗 MA AAA RMV Appointment Reminder
This tool helps anyone who missed the expiration of drive license (Registration, Non-CDL License, State ID and Real ID transactions) to get their AAA RMV appointment as soon as possible. It will run as scheduled to fetch the latest available appointment on the AAA website. You may be lucky to get a soon appointment from someone who canceled.

# ⚠️ !!Important
Please do not abuse this tool and schedule the appointment on the AAA RMV official website and RMV website as appropriate. cuz it will cause lots of traffic to AAA web server. 
Please use this when you really need it!!

## 🧰 Pre-request
### Apply Google API key
1. Go to the Google Cloud Console (https://console.cloud.google.com/).
2. Create a new project (or select an existing project).
3. Go to the APIs & Services > Credentials page.
4. Click the Create credentials button and select API key.
5. Copy / save the generated API key.
6. Enable the Google Maps JavaScript API (or any other API you plan to use) in the APIs & Services > Dashboard page. ([Enable Geocoding API service](https://console.cloud.google.com/marketplace/product/google/geocoding-backend.googleapis.com?q=search&referrer=search&project=flash-crawler-375801))

## Environment variable
### System variables:
1. GOOGLE_API_KEY: Used to calculate the drive time from your home to the target RMV location
2. (Optional)SMS_TOKEN: It can help send sms notification to your phone
3. (Optional)NOTIFICATION_SENDER_EMAIL_PASSWORD: `email password`
4. (Optional)NOTIFICATION_SENDER_EMAIL: `email account`

Note: 
- The email can not use `GMAIL` due to the security policy. you also need to disable two the two steps verification
- All these variables could also be set in the action secret.

### 🚚 Service variable
1. HOME_ADDRESS: `copy your home address from google map` 
2. ACCEPTED_DRIVE_TIME: Set the maximum drive time you accepted
3. TOP_RES: Only send the top n(th) res to your email or message
4. TARGET_EMAIL: The target email to receive the notification
5. TARGET_PHONE: The target phone to receive the notification

# 📝 Usage
## Repo set up
1. Create a new repository, ensuring the visibility is set to private.
2. Clone the repository you'd like to fork locally.
3. Create a new remote using the upstream repository's URL.
4. Set the origin URL to that of your newly-created private repository.
5. Push to origin.
6. fill the .env file and wait for the action to run as scheduled
7. Uncomment the schedule in the github action configuration.