<?php
// 检查查询参数是否已设置
if (!isset($_GET['color']) || !isset($_GET['txt'])) {
    echo '参数未设置。';
    exit;
}

$color = $_GET['color'];
$txt = $_GET['txt'];

// 构建Python脚本的命令行参数
$pythonScript = 'text2img_txt.py';

// 使用 escapeshellarg 函数确保参数的安全使用
$color = escapeshellarg($color);
$txt = escapeshellarg($txt);

// 参数顺序调换不影响传入顺序
$command = "python3 $pythonScript $color $txt";

// 执行Python脚本
$output = shell_exec($command);

// 输出Python脚本的结果
echo $output;
?>
