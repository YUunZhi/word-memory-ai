# AI单词记忆个性化规划器 主脚本 main.py
import json

# 大模型提示词模板
PROMPT_TEMPLATE = """
你是专业单词记忆规划AI，结合艾宾浩斯遗忘曲线，根据用户输入生成每日背诵计划。
输入单词列表、掌握等级、每日学习时长，输出：
1. 今日背诵清单（生词优先）
2. 自测练习题
3. 薄弱词汇汇总
要求输出结构化清晰文本。
用户输入：{user_input}
"""

def get_word_plan(word_list, master_level, study_time):
    """调用AI生成单词背诵规划"""
    user_input = f"单词：{word_list}，掌握程度：{master_level}，每日可学习时长：{study_time}分钟"
    prompt = PROMPT_TEMPLATE.format(user_input=user_input)
    # 模拟AI输出
    print("===== AI单词记忆规划结果 =====")
    print(f"用户输入信息：{user_input}")
    print("1. 今日背诵清单：陌生单词20个，半熟单词10个，熟词复习5个")
    print("2. 自测习题：10道中英互译填空")
    print("3. 薄弱词汇：abandon、schedule、separate")
    return prompt

if __name__ == "__main__":
    print("===== AI单词记忆个性化规划器 =====")
    words = input("请输入单词（逗号分隔）：")
    level = input("单词掌握程度（完全陌生/有点印象/熟练掌握）：")
    time_len = input("每日可背诵时长(分钟)：")
    get_word_plan(words, level, time_len)