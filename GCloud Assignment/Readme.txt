	1) Set up the Google Cloud Variables
DB_INSTANCE_NAME=db-instance
PROJECT_NAME=cis3111-2023-september 
REGION=europe-west1
DB_USER=user
DB_NAME=user 
CLOUD_SQL_PASSWORD=pass1234

	2) Set up cloud enviroment
gcloud auth list
gcloud config list project
gcloud config set project $PROJECT_NAME
gcloud config set compute/region $REGION

	3)API requests
gcloud services enable compute.googleapis.com sqladmin.googleapis.com

	4)SQL instance
gcloud sql instances create $DB_INSTANCE_NAME --region=$REGION
gcloud sql databases create $DB_NAME --instance $DB_INSTANCE_NAME
gcloud sql users create $DB_USER --host=% --instance $DB_INSTANCE_NAME --password $CLOUD_SQL_PASSWORD

	5)Clone code
git clone https://github.com/AndreM27/CIS3111-SEPT.git

	6)run code
cd CIS3111-SEPT/
cd GCloud\ Assignment/
gcloud app deploy --promote --stop-previous-version app.yaml