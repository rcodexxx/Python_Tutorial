import os
import sys
import re


def check_folder(student_id):
    folder_path = f"Class_member/{student_id}"
    errors = []

    # 1. 檢查資料夾是否存在
    if not os.path.isdir(folder_path):
        errors.append(f"錯誤：{folder_path} 資料夾不存在")
        return False

    # 獲取資料夾中的所有項目
    contents = os.listdir(folder_path)

    # 2. 檢查是否有 .md 文件
    md_files = [f for f in contents if f.endswith('.md')]
    if not md_files:
        errors.append(f"錯誤：{folder_path} 中沒有 .md 文件")
        return False
    elif len(md_files) > 1:
        errors.append(f"錯誤：{folder_path} 中有多個 .md 文件")
        return False

    # 3. 檢查是否有 images 資料夾
    if 'images' not in contents or not os.path.isdir(os.path.join(folder_path, 'images')):
        errors.append(f"錯誤：{folder_path} 中沒有 images 資料夾")
        return False

    # 4. 檢查是否只有 .md 文件和 images 資料夾
    allowed_items = {md_files[0], 'images'}
    if set(contents) != allowed_items:
        errors.append(f"錯誤：{folder_path} 中包含不允許的文件或資料夾")
        return False

    # 5. 檢查 .md 文件內容
    md_file_path = os.path.join(folder_path, md_files[0])
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 定義檢查規則
    name_pattern = r"姓名:\s*[^\n]+"
    id_pattern = rf"學號:\s*{student_id}"  # 學號必須與資料夾名稱一致
    github_pattern = r"Github 帳號:\s*!\[\]\(\./images/[^\)]+\)"

    if not re.search(name_pattern, content):
        errors.append(f"錯誤：{md_file_path} 中缺少 '姓名' 欄位或格式不正確")
        return False
    if not re.search(id_pattern, content):
        errors.append(f"錯誤：{md_file_path} 中的學號與資料夾名稱 {student_id} 不符")
        return False
    if not re.search(github_pattern, content):
        errors.append(f"錯誤：{md_file_path} 中的圖片不正確，應為 ![](./images/...)")
        return False

    if errors:
        return False, errors

    print(f"{student_id} 符合")
    return True, []


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    student_id = sys.argv[1]
    success, errors = check_folder(student_id)
    if success:
        sys.exit(0)
    else:
        print("提交不符合：")
        for error in errors:
            print(error)
        sys.exit(1)