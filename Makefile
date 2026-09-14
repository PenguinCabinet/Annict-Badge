deploy:
	gcloud functions deploy annict --gen2 --region=asia-northeast1 --runtime=python314 --entry-point=Annict --trigger-http --allow-unauthenticated --update-secrets=annict-badge-key=annict-badge-key:latest
	
