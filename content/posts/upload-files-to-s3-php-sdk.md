---
title: "How to upload files to S3 using PHP SDK"
date: 2025-04-04T11:30:03+00:00
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
Alright, uploading files to S3 with PHP? Super simple with the AWS SDK. Let’s break it down.

First, install the AWS SDK for PHP (if you haven’t already):
```bash
composer require aws/aws-sdk-php
```

And then here is an example script

```php
<?php

require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;

// AWS S3 config
$s3 = new S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1', // Change to your region
    'credentials' => [
        'key'    => 'your-access-key',
        'secret' => 'your-secret-key',
    ],
]);

$bucketName = 'your-bucket-name';
$filePath = 'path/to/local/file.txt';
$keyInS3 = 'folder-in-s3/file.txt'; // Where it should be stored in S3

try {
    $s3->putObject([
        'Bucket' => $bucketName,
        'Key'    => $keyInS3,
        'SourceFile' => $filePath,
        'ACL'    => 'public-read', // Or private, depending on your needs
    ]);
    echo "Upload successful!\n";
} catch (AwsException $e) {
    echo "Upload failed: " . $e->getMessage() . "\n";
}

?>
```