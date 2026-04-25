# 键盘输入一段包含中文、英文、数字及标点的文本，保存在字符串变量 s 中。
# 用 Python 内置方法统计 中文字符（含中文标点） 的个数；
# 用 jieba 库对文本分词后，统计 长度≥2 的中文词语 的个数（即忽略单个字的分词结果）。
# 注意：
# 中文字符范围：\u4e00 到 \u9fff 及常见中文标点（如 ，。！？、；：“”‘’（） 等）。
# 分词结果中，非中文字符串不计入词语数。
# 示例：
# 键盘输入：
# 我爱 Python，也爱中国！
# 屏幕输出：
# 中文字符数为：8，有效中文词语数为：2。
import jieba

# 1. 输入文本并去除所有空格
s = input("请输入一段文本：")
# 强制去除所有空格（包括全角空格）
s = s.replace(" ", "").replace("　", "")

# 2. 统计中文字符（含中文标点）的个数
chinese_count = 0
# 直接用列表存标点，避免引号解析错误
cn_punct = list("，。！？、；：“”‘’（）《》【】……——、")
for c in s:
    if '\u4e00' <= c <= '\u9fff' or c in cn_punct:
        chinese_count += 1

# 3. 用jieba分词，并统计长度≥2的中文词语个数
# 强制使用精确模式
words = jieba.lcut(s, cut_all=False)
print("分词结果：", words)

valid_word_count = 0
for word in words:
    if len(word) >= 2:
        # 检查每个字是否都是中文
        is_all_chinese = True
        for c in word:
            if not ('\u4e00' <= c <= '\u9fff'):
                is_all_chinese = False
                break
        if is_all_chinese:
            valid_word_count += 1

# 4. 输出结果
print(f"中文字符数为：{chinese_count}，有效中文词语数为：{valid_word_count}。")