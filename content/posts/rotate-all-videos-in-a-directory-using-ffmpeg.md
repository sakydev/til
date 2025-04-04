---
author: "Saqib Razzaq"
title: "How to rotate all videos in directory using Ffmpeg"
date: "2020-04-19"
tags: ["php", "ffmpeg"]
ShowToc: true
TocOpen: true
---

```php

    if (!$argv['1']) { exit("php rotate_360.php input_dir output_dir degress_to_rot"); }
    print_r($argv);
    $input_dir = $argv['1'];
    $output_dir = $argv['2'];
    if (!file_exists($output_dir)) { @mkdir($output_dir); }
    $degress = !empty($argv['3']) ? $argv['3'] : 360;
    
    $files = glob("{$input_dir}/*.mp4");
    foreach ($files as $key => $file) {
    	$filename = pathinfo($file, PATHINFO_FILENAME); // outputs nameonly
    	$command = "ffmpeg -i {$input_dir}/{$filename}.mp4 -c copy -metadata:s:v:0 rotate={$degress} {$output_dir}/{$filename}-out.mp4";
    	echo $command . "\n";
    	shell_exec($command);
    }
```