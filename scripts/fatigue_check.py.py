# -*- coding: utf-8 -*-

def ask_question(question_text, options):
    """
    在控制台打印问题和选项，接收用户输入并返回对应的分数
    options 格式: [("选项文本", 分数), ...]
    """
    print(f"\n{question_text}")
    for i, (text, score) in enumerate(options, 1):
        print(f"  {i}. {text}")

    while True:
        try:
            choice = int(input(f"请输入最符合的选项编号 (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                return options[choice - 1][1]
            else:
                print(f"输入无效，请输入 1 到 {len(options)} 之间的数字。")
        except ValueError:
            print("输入无效，请输入数字。")

def get_symptom_category(score):
    if score <= 2: return 'I'
    elif score <= 7: return 'II'
    elif score <= 14: return 'III'
    else: return 'IV'

def get_work_category(score):
    if score == 0: return 'A'
    elif score <= 5: return 'B'
    elif score <= 11: return 'C'
    else: return 'D'

def main():
    print("="*60)
    print(" 劳动者疲劳蓄积度自我诊断检查表（2023年改正版） ")
    print("="*60)
    print("本检查表通过您的“自觉症状”和“近1个月的勤务状况”来判定您的疲劳蓄积程度。")
    print("请根据实际情况回答以下问题。\n")

    # --- 第一部分：最近1个月的自觉症状 ---
    print("-" * 60)
    print("【１． 最近 1 个月间的自觉症状】")
    print("-" * 60)

    symptoms_options = [("几乎没有", 0), ("有时有", 1), ("经常有", 3)]
    symptoms_questions = [
        "1. 烦躁易怒",
        "2. 感到不安",
        "3. 无法静下心来",
        "4. 感到忧郁",
        "5. 睡眠不好",
        "6. 身体状态不佳",
        "7. 无法集中注意力",
        "8. 做事经常出错",
        "9. 工作中受到强烈的睡意侵袭",
        "10. 提不起劲，没有干劲",
        "11. 筋疲力尽（不含运动后）",
        "12. 早上起床时感到极其疲惫",
        "13. 相比以前，更容易疲劳",
        "14. 感觉没有食欲"
    ]

    symptom_score = 0
    for q in symptoms_questions:
        symptom_score += ask_question(q, symptoms_options)

    symptom_cat = get_symptom_category(symptom_score)
    print(f"\n>> 自觉症状总分: {symptom_score} 点 -> 评价等级: {symptom_cat}")


    # --- 第二部分：最近1个月的勤务状况 ---
    print("\n" + "-" * 60)
    print("【２． 最近 1 个月间的勤务状况】")
    print("-" * 60)

    work_questions = [
        ("1. 1个月的劳动时间（含加班、休息日工作时间）", [("适当", 0), ("多", 1), ("非常多", 3)]),
        ("2. 不规则的勤务（预定变更、突发工作）", [("少", 0), ("多", 1)]),
        ("3. 出差带来的负担（频率、拘束时间、时差等）", [("没有或较小", 0), ("较大", 1)]),
        ("4. 深夜勤务带来的负担", [("没有或较小", 0), ("较大", 1), ("非常大", 3)]),
        ("5. 休息・假寐的时间及设施", [("适当", 0), ("不适当", 1)]),
        ("6. 工作上的身体负担 (肉工作或冷热环境)", [("较小", 0), ("较大", 1), ("非常大", 3)]),
        ("7. 工作上的精神负担", [("较小", 0), ("较大", 1), ("非常大", 3)]),
        ("8. 职场・顾客等人际关系带来的负担", [("较小", 0), ("较大", 1), ("非常大", 3)]),
        ("9. 规定时间内处理不完的工作量", [("少", 0), ("多", 1), ("非常多", 3)]),
        ("10. 无法按自己的节奏进行的工作", [("少", 0), ("多", 1), ("非常多", 3)]),
        ("11. 下班后也总是挂念工作", [("几乎没有", 0), ("有时有", 1), ("经常有", 3)]),
        ("12. 工作日的睡眠时间", [("充足", 0), ("稍微不足", 1), ("不足", 3)]),
        ("13. 从下班到下一次上班之间的休息时间（勤务间歇）", [("充足", 0), ("稍微不足", 1), ("不足", 3)])
    ]

    work_score = 0
    for q_text, q_options in work_questions:
        work_score += ask_question(q_text, q_options)

    work_cat = get_work_category(work_score)
    print(f"\n>> 勤务状况总分: {work_score} 点 -> 评价等级: {work_cat}")


    # --- 第三部分：综合判定（疲劳蓄积度点数表） ---
    # 矩阵：矩阵[自觉症状][勤务状况]
    fatigue_matrix = {
        'I':   {'A': 0, 'B': 0, 'C': 2, 'D': 4},
        'II':  {'A': 0, 'B': 1, 'C': 3, 'D': 5},
        'III': {'A': 0, 'B': 2, 'C': 4, 'D': 6},
        'IV':  {'A': 1, 'B': 3, 'C': 5, 'D': 7},
    }

    fatigue_value = fatigue_matrix[symptom_cat][work_cat]

    # --- 判定结果与建议 ---
    judgments = {
        0: "较低",
        1: "较低",
        2: "偏高",
        3: "偏高",
        4: "较高",
        5: "较高",
        6: "非常高",
        7: "非常高"
    }

    print("\n" + "=" * 60)
    print(" 【 诊 断 结 果 】 ")
    print("=" * 60)
    print(f"■ 您的疲劳蓄积度点数为：【 {fatigue_value} 】 (范围0~7)")
    print(f"■ 判定结果：疲劳蓄积度 {judgments[fatigue_value]}")
    print("-" * 60)

    if fatigue_value >= 2:
        print("【预防对策建议】")
        print("点数在2~7的人，可能已经蓄积了疲劳。请检查您在“勤务状况”中得分为 1 或 3 的项目。")
        print(" - 个人可裁量改善的项目：请自行改善。")
        print(" - 个人无法裁量改善的项目：请与上司或产业医等沟通改善勤务状况。")
        print(" - 此外，请重新审视您的睡眠和休养。如果加班和休息日工作时间每月超过45小时，请务必探讨缩短工作时间。")
    else:
        print("【预防对策建议】")
        print("目前看来疲劳蓄积度较低。请继续保持良好的睡眠、休养和合理的工作节奏。")

    print("=" * 60)
    print("※ 注意：患有糖尿病、高血压等疾病的人，判定结果可能存在偏差。")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n测试已取消。")
