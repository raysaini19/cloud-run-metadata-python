# cloud-run-metadata-python

```
gcloud run deploy metadata-service \
    --source . \
    --project <project_name> \
    --platform managed \
    --region <region> \
    --allow-unauthenticated
```

```
echo eyJhbGciOiJSUzI1NiIsImtpZC... | cut -d "." -f2 | base64 --decode | jq
```