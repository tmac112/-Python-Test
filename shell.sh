#!/bin/bash

# 输入文件名和搜索内容
read -p "请输入文件名: " filename
read -p "请输入要搜索的内容: " search_term

# 搜索并保存结果到新文件
grep -n "$search_term" "$filename" > search_results.txt

# 输出结果到控制台
echo "搜索结果："
cat search_results.txt

echo "搜索结果已保存到 search_results.txt 文件中。"
