---
title: "How to download all files from an S3 bucket"
date: 2020-09-15T11:30:03+00:00
tags: ["AWS", "S3"]
draft: false
hidemeta: false
comments: false
canonicalURL: "https://canonical.url/to/page"
disableShare: false
disableHLJS: false
hideSummary: true
searchHidden: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
---
To download all files from an S3 bucket using the AWS CLI, use the following command:

```bash
aws s3 sync s3://your-bucket-name/ /local/destination/path
```

This command will download all objects from the S3 bucket while preserving the folder structure. If you only want specific file types, you can use the `--exclude` and `--include` options.

Example: Download only `.jpg` files:
```bash
aws s3 sync s3://your-bucket-name/ /local/destination/path --exclude "*" --include "*.jpg"
```