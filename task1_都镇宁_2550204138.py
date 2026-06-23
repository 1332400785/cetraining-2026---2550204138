# -*- coding: utf-8 -*-
import sys
import io
# 修复 Windows GBK 控制台编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='replace')

"""
学生信息管理系统 - 增删改查菜单
作者: 都镇宁
学号: 2550204138
"""

students = []  # 存储学生信息的列表，每个学生为一个字典


def add_student():
    """添加学生信息"""
    print("\n===== 添加学生 =====")
    sid = input("请输入学号: ").strip()
    name = input("请输入姓名: ").strip()
    age = input("请输入年龄: ").strip()
    major = input("请输入专业: ").strip()

    student = {
        "学号": sid,
        "姓名": name,
        "年龄": age,
        "专业": major
    }
    students.append(student)
    print(f"[OK] 学生 {name} 添加成功！")


def show_students():
    """显示所有学生信息"""
    print("\n===== 学生列表 =====")
    if not students:
        print("暂无学生信息。")
        return

    print(f"{'序号':<6}{'学号':<14}{'姓名':<10}{'年龄':<8}{'专业':<16}")
    print("-" * 54)
    for i, s in enumerate(students, 1):
        print(f"{i:<6}{s['学号']:<14}{s['姓名']:<10}{s['年龄']:<8}{s['专业']:<16}")
    print(f"\n共 {len(students)} 条记录")


def search_student():
    """查询学生信息"""
    print("\n===== 查询学生 =====")
    keyword = input("请输入要查询的学号或姓名: ").strip()

    results = [s for s in students if keyword in s['学号'] or keyword in s['姓名']]
    if not results:
        print("未找到匹配的学生信息。")
        return

    print(f"\n找到 {len(results)} 条匹配记录:")
    print(f"{'学号':<14}{'姓名':<10}{'年龄':<8}{'专业':<16}")
    print("-" * 48)
    for s in results:
        print(f"{s['学号']:<14}{s['姓名']:<10}{s['年龄']:<8}{s['专业']:<16}")


def update_student():
    """修改学生信息"""
    print("\n===== 修改学生 =====")
    sid = input("请输入要修改的学生学号: ").strip()

    for s in students:
        if s['学号'] == sid:
            print(f"当前信息: 姓名={s['姓名']}, 年龄={s['年龄']}, 专业={s['专业']}")
            print("（直接回车保留原值）")

            name = input("新姓名: ").strip()
            age = input("新年龄: ").strip()
            major = input("新专业: ").strip()

            if name:
                s['姓名'] = name
            if age:
                s['年龄'] = age
            if major:
                s['专业'] = major

            print(f"[OK] 学号 {sid} 的信息已更新！")
            return

    print(f"未找到学号为 {sid} 的学生。")


def delete_student():
    """删除学生信息"""
    print("\n===== 删除学生 =====")
    sid = input("请输入要删除的学生学号: ").strip()

    for i, s in enumerate(students):
        if s['学号'] == sid:
            confirm = input(f"确认删除 {s['姓名']}(学号:{sid})？(y/n): ").strip().lower()
            if confirm == 'y':
                del students[i]
                print(f"[OK] 学生 {s['姓名']} 已删除！")
            else:
                print("已取消删除。")
            return

    print(f"未找到学号为 {sid} 的学生。")


def main():
    """主菜单"""
    menu = """
╔══════════════════════════════════╗
║     学生信息管理系统 v1.0        ║
║     都镇宁  2550204138          ║
╠══════════════════════════════════╣
║  1. 添加学生信息                 ║
║  2. 显示所有学生                 ║
║  3. 查询学生信息                 ║
║  4. 修改学生信息                 ║
║  5. 删除学生信息                 ║
║  0. 退出系统                     ║
╚══════════════════════════════════╝
"""

    while True:
        print(menu)
        choice = input("请输入选项 (0-5): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            show_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '0':
            print("\n谢谢使用，再见！")
            break
        else:
            print("\n无效选项，请重新输入！")


if __name__ == "__main__":
    main()