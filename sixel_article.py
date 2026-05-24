#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

IMAGE = "cat.jpg"

article_before = """
# 一只猫的下午

午后的阳光落在窗台上，像一层温柔的金色薄毯。
猫趴在那里，半眯着眼，尾巴偶尔轻轻晃一下。

它似乎什么也没想，又似乎已经理解了整个宇宙。
"""

article_after = """
图片之后，故事继续。

窗外有人经过，树叶在风里发出细碎的响声。
猫抬头看了一眼，又重新把下巴放回爪子上。

也许幸福就是这样：
有阳光，有安静，还有一张刚好够暖的窗台。
"""

def print_sixel_image(path: str):
    """
    使用 img2sixel 把图片转换为 sixel 并输出到终端。
    需要安装 libsixel / img2sixel。
    """
    if not Path(path).exists():
        print(f"\n[图片不存在: {path}]\n")
        return

    try:
        subprocess.run(
            ["img2sixel", "-w", "480", path],
            check=True
        )
    except FileNotFoundError:
        print("\n[未找到 img2sixel，请先安装 libsixel]\n")
    except subprocess.CalledProcessError:
        print("\n[图片 sixel 输出失败]\n")

def main():
    print(article_before)
    print_sixel_image(IMAGE)
    print(article_after)

if __name__ == "__main__":
    main()
