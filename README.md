# 前端视觉风格

可安装的 Agent skill。`frontend-style-gallery/` 整个文件夹就是技能本体：`SKILL.md` 和 `gallery/` 在一起，复制这一个文件夹就能装到别的机器上。

| 要看什么 | 在哪里 |
| --- | --- |
| 技能说明 | [frontend-style-gallery/SKILL.md](frontend-style-gallery/SKILL.md) |
| 在浏览器里浏览全部风格 | [frontend-style-gallery/gallery/gallery.html](frontend-style-gallery/gallery/gallery.html) |
| 风格索引 | [frontend-style-gallery/gallery/README.md](frontend-style-gallery/gallery/README.md) |
| 重新生成说明和预览 | `python frontend-style-gallery/gallery/generate_gallery.py` |

## 安装

把 `frontend-style-gallery` 文件夹放到 Cursor 的用户 skills 目录，文件夹名保持不变：

`%USERPROFILE%\.cursor\skills\frontend-style-gallery`

本机这份已经用目录联接到上面的路径。改仓库里的技能，本机 Agent 读到的是同一份。

## 使用

Agent 使用这个 skill、而你还没有指定风格时，会先列出 1–21 的全部选项，等你回复编号。可以多选，例如 `5` 或 `5 11`。
