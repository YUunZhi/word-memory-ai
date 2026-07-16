---
name: get-current-time
description: 获取当前系统本地时间、日期、星期、时区等时间信息的实用工具，当用户询问当前时间、现在几点、日期、星期几、时区时触发
author: Domi
created: 2026-07-03
tags: [utility, time, system]
---

# 获取当前系统时间

## 触发条件
当用户请求获取当前本地时间、日期、星期或时区信息时触发。

## 执行步骤
1. 根据操作系统选择对应的命令：
   - Linux/macOS/Windows Git Bash: 使用 `date +"%Y-%m-%d %H:%M:%S"` 获取格式化的当前时间
   - Windows PowerShell: 使用 `powershell -Command "(Get-Date).ToString('yyyy-MM-dd HH:mm:ss')"`
2. 调用`terminal`工具执行选中的命令
3. 提取命令输出的时间字符串，整理成自然语言返回给用户

## 示例响应
> 当前时间是：2026-07-03 15:42:30

## 注意事项
- 该skill获取的是运行环境的本地系统时间，而非UTC时间
- 如果需要UTC时间，可以修改命令为`date -u +"%Y-%m-%d %H:%M:%S"`或对应的PowerShell命令