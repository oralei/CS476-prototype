from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
from cloudinary.utils import cloudinary_url
from datetime import datetime

import cloudinary
import cloudinary.uploader
import cloudinary.api

import os

# Load .env into environment variables
load_dotenv()

app = Flask(__name__)

# --- Cloudinary Setup ---
cloudinary.config(
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key = os.getenv("CLOUDINARY_API_KEY"),
    api_secret = os.getenv("CLOUDINARY_API_SECRET"),
)

# --- MongoDB Setup ---
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")

# Create Mongo client (do this once)
client = MongoClient(MONGODB_URI)

db = client[MONGODB_DB]
coll = db[MONGODB_COLLECTION]

uploads_db = client["uploads"]
images_coll = uploads_db["images"]

@app.route('/')
def home():
    # Fetch a few users from sample_mflix.users
    users = list(
        coll.find(
            {},
            {"name": 1, "email": 1}
        ).limit(10)
    )

    # ObjectId -> string for Jinja
    for u in users:
        u["_id"] = str(u["_id"])

    return render_template('home.html', users=users)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route("/view-image")
def view_image():
    
    docs = list(images_coll.find().sort("_id", -1).limit(30))

    for d in docs:
        d["_id"] = str(d["_id"])
        url, _ = cloudinary_url(
            d["public_id"],
            secure=True,
            width=100,
            crop="scale"
        )
        d["url"] = url

    return render_template("view-image.html", images=docs)

@app.route('/upload-test', methods=['GET', 'POST'])
def upload_test():
    if request.method == 'POST':
        file = request.files['image']  # Get file from form
        upload_result = cloudinary.uploader.upload(
            file,
            folder="/images",        # this creates/uses folders automatically
            resource_type="image"        # optional, keeps it strict for images
        )
        
        # Store the reference in MongoDB
        image_doc = {
            "public_id": upload_result["public_id"],
            "secure_url": upload_result["secure_url"],
            "format": upload_result["format"],
            "uploaded_at": datetime.now(),
        }
        
        images_coll.insert_one(image_doc)
        
        return redirect('/view-image')  # or wherever you want
    
    # If GET request, show the form
    return render_template('upload-test.html')