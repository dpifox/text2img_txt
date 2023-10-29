<?php
// 检查查询参数是否已设置和是否符合要求
if (!isset($_GET['color']) || !isset($_GET['txt'])) {
    echo '参数未设置。';
    exit;
}

$color = $_GET['color'];
$txt = $_GET['txt'];

if (!is_numeric($color) && !ctype_alpha($color)) {
    echo '参数 color 必须为数字或文本。';
    exit;
}

if (!is_numeric($txt) && !ctype_alpha($txt)) {
    echo '参数 txt 必须为数字或文本。';
    exit;
}

// 构建Python脚本的命令行参数
$pythonScript = 'text2img_txt.py';
// 使用 escapeshellarg 函数确保参数的安全使用
$command = "python3 $pythonScript " . escapeshellarg($color) . " " . escapeshellarg($txt);

// 执行Python脚本
$output = shell_exec($command);

// 输出Python脚本的结果
echo $output;
?>
