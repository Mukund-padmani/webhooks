Prerequisites

Make sure installed:

Python 3.10+
MongoDB (running locally)
pip


Check versions:

python --version
mongo --version

⚙️ Setup Instructions
1️⃣ Go to project folder
cd webhookapp

2️⃣ Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install flask pymongo


Or if you create requirements.txt:

pip install -r requirements.txt


Example requirements.txt:

flask
pymongo

🗄️ Start MongoDB

Make sure MongoDB server is running.

Windows:

net start MongoDB


OR start from MongoDB Compass background service.

▶️ Run the App
python app.py


You should see:

Running on http://127.0.0.1:5000

🌐 Test in Browser

Open:

http://127.0.0.1:5000/

🔌 Webhook Endpoint
POST /webhook


GitHub will send events here.

View Stored Events
GET /events


Open in browser:

http://127.0.0.1:5000/events

🔗 Connect GitHub Webhook
In GitHub Repo:

Settings → Webhooks → Add Webhook

Payload URL:
http://YOUR_PUBLIC_URL/webhook


For local testing use ngrok:

ngrok http 5000


Then use:

https://xxxxx.ngrok.io/webhook


Content type:

application/json


Select events:

Push
Pull Request

🧾 MongoDB Schema Used

Stored document example:

{
  request_id: "commit_hash_or_pr_id",
  author: "username",
  action: "PUSH | PULL_REQUEST | MERGE",
  from_branch: "feature",
  to_branch: "main",
  timestamp: "UTC datetime string"
}
