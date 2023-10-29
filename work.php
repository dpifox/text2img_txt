<?php
// 获取查询参数
$color = $_GET['color'];
$txt = $_GET['txt'];

// 构建Python脚本的命令行参数
$pythonScript = 'text2img_txt.py';
$command = "python3 $pythonScript $color $txt";

// 执行Python脚本
$output = shell_exec($command);

// 输出Python脚本的结果
echo $output;
?>