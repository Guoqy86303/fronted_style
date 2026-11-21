---
name: frontend-style-gallery
description: >-
  Catalog and plan frontend visual styles (21 styles) for any project. Use when
  planning or choosing a UI/visual style, selecting a design direction, building
  a style plan, picking colors, or answering "which style fits this
  project/product". If the user has not already chosen a style, the first reply
  must list all 21 styles as a numbered menu and wait for a number. Covers
  minimalist, flat, material, fluent, enterprise-data, glassmorphism,
  neumorphism, neo-brutalism, editorial, pixel-retro, cyber-neon, illustrative,
  cartoon-2d, maximalist, medieval, sacred-art, silk-road-dunhuang,
  islamic-geometric, chinese-contemporary, postmodern, and ink-wash styles.
---

# 前端视觉风格图库 · Frontend Style Gallery

This skill is a **planning catalog** of 21 frontend visual styles. Use it when
you need to pick, recommend, or plan a visual direction for a UI, or when you
are building a design plan and must weigh style trade-offs.

The installable unit is the directory that contains this `SKILL.md`. Copy that
whole directory to a skills folder and keep the folder name
`frontend-style-gallery`. Specs below match the Chinese `README.md` files in
the gallery; do not invent a 22nd style or a different palette.

`<GALLERY>` is the `gallery` directory next to this file. Resolve it from the
`SKILL.md` you actually loaded. Do not hard-code a drive letter.

Each style lives in its own numbered folder with a `README.md` and a
`preview.svg`. The browsable index is `<GALLERY>/gallery.html`.

> 图片是原创的示意界面，用于表达风格，不代表任何现成产品的完整设计规范。

## 开头对话

使用本 skill 时，只要用户还没有用编号或风格名称选定方向，第一条回复就只发下面这份完整清单，然后停下等用户选。

- 必须带编号 1–21，一项不漏。
- 不要先缩成 2–3 个候选，不要先写布局或配色方案。
- 用户若同时要求推荐，仍先发完整清单，再在清单后面加一行建议编号。
- 用户这条消息里已经写出编号或风格名称时，视为已选定，不要再发清单。
- 编号与文件夹前缀一致：1 是 `01-minimalist`，21 是 `21-ink-wash`。

按下面的文字发送：

```
请选择视觉风格。回复编号即可，可以多选（例如 5，或 5 11）。

视觉与交互
1. 极简主义 · Minimalism — 留白、克制的配色、清晰的字体层级，让内容成为主角
2. 扁平化 · Flat Design — 纯色、简单图标和规整卡片，减少材质模拟
3. Material Design · Material Design 3 — 色彩角色、层级、圆角组件和动效
4. Fluent Design · Fluent 2 — 柔和表面、圆角、细边框，桌面软件气质
5. 企业数据风 · Enterprise Data — 稳定网格、密集而有序的表格与图表
6. 玻璃拟态 · Glassmorphism — 半透明面板、背景模糊、浅边框和叠层
7. 新拟态 · Neumorphism — 同色表面的柔和高光与阴影，轻微凸起或凹陷
8. 新粗野主义 · Neo-brutalism — 粗边框、硬阴影、鲜艳色块和夸张字体
9. 编辑杂志风 · Editorial — 大标题、衬线字体、图文交错和留白
10. 像素风 / 复古游戏风 · Pixel / Retro — 像素块、等宽字、有限色盘和游戏界面
11. 赛博霓虹风 · Cyber / Neon — 深色背景、荧光色、发光元素和科技感线条
12. 插画手绘风 · Illustrative — 手绘角色、有机图形和温暖配色
13. 2D 卡通风 · 2D Cartoon — 平面角色、清楚轮廓线和纯色填充
14. 华丽极繁主义 / 哥特装饰 · Ornate Maximalism — 尖拱、玫瑰窗、花饰细线、宝石色与金色

文化与历史
15. 中世纪手抄本风 · Medieval Manuscript — 羊皮纸底色、装饰边框和手抄本式插图
16. 宗教艺术启发 / 彩窗 · Sacred Art — 留白、光线与彩窗结构
17. 西域 / 敦煌艺术启发 · Silk Road / Dunhuang — 青绿、赭红、金色及莲花、卷草纹样
18. 伊斯兰艺术启发 / 几何纹样 · Islamic Geometric — 重复几何纹样与对称节奏
19. 中国现代设计风 · Chinese Contemporary — 现代网格、中文排版、克制的中国红与留白
20. 后现代风 · Postmodern — 不对称构图、几何拼贴、鲜明配色和风格混搭
21. 中国水墨风 · Chinese Ink Wash — 墨色层次、山水意象、纸色留白和小面积朱印
```


## 选定之后

用户给出编号或名称之后，再按顺序做。不要再次弹出完整清单。

1. **Understand the product** — What is it? (tool / game / brand site / SaaS /
   cultural exhibit / kids product). Who is the audience? What is the emotional
   goal (calm, fun, sacred, efficient, premium)?
2. **Read the chosen style** — Open `<GALLERY>/<NN-name>/README.md` and
   `preview.svg`. Check "使用时留意", readability, and information density.
3. **Check the example palette** — Start from the 3 example hex colors, then
   adapt them to the brand.
4. **Decide on combination** — Multiple numbers are allowed. A common pattern
   is one overall style plus one local effect (for example enterprise-data
   with a glassmorphism hero).
5. **Write the plan** — State the chosen style(s), the rationale, the starting
   palette, the cautions, and which gallery files were referenced. In Plan
   mode, stop at a reviewable plan.

### 推荐时才用的对照

只在清单已经发出、或用户已经选定之后，用来解释建议。不能用来代替完整编号清单。

| Goal / constraint | Start with these styles |
| --- | --- |
| 突出颜色本身（如 RGB / 颜色玩具） | 1 极简主义、2 扁平化 |
| 强调玩具感 / 趣味 | 10 像素风、12 插画手绘风、13 2D 卡通风 |
| 强调发光效果 | 11 赛博霓虹风 |
| 高效密集信息 / 后台 | 5 企业数据风、4 Fluent、3 Material |
| 品牌官网 / 作品集 | 1 极简主义、9 编辑杂志风、8 新粗野主义 |
| 文化 / 历史 / 展览 | 15 中世纪手抄本、17 敦煌、18 伊斯兰几何、21 中国水墨、16 宗教彩窗 |
| 高端 / 仪式感 | 14 华丽极繁主义（哥特装饰） |
| 桌面 / 办公工具 | 4 Fluent、3 Material |
| 创意 / 戏谑 | 20 后现代风、8 新粗野主义 |
| 轻松 / 亲近 / 教育 | 12 插画手绘风、13 2D 卡通风 |

颜色玩具的三条提示写在 `<GALLERY>/README.md` 的「选型示例：颜色本身是主角」。

## The 21 styles

Grouped by the gallery's own categories.

### 视觉与交互（Visual & Interaction）

#### 01 · 极简主义 / Minimalism
- **识别特征**: 留白、克制的配色、清晰的字体层级，让内容成为主角。
- **适用场景**: 品牌官网、作品集、专注型工具。
- **示例配色**: `#f8f7f3 · #272c26 · #777a71`
- **使用时留意**: 页面可能显得单薄；需认真处理排版、间距和对比度。
- **文件**: `<GALLERY>\01-minimalist\`

#### 02 · 扁平化 / Flat Design
- **识别特征**: 用纯色、简单图标和规整卡片组织信息，减少材质模拟。
- **适用场景**: 移动应用、后台、轻量产品。
- **示例配色**: `#19457e · #4c82d5 · #25b09b`
- **使用时留意**: 不要让按钮与普通色块难以区分；用状态、文案和对比建立交互提示。
- **文件**: `<GALLERY>\02-flat\`

#### 03 · Material Design / Material Design 3
- **识别特征**: 以色彩角色、层级、圆角组件和动效构建统一界面。
- **适用场景**: 跨平台应用、功能较多的产品。
- **示例配色**: `#6750a4 · #e9e4f5 · #2f2942`
- **使用时留意**: 参考官方组件规范，同时建立自己的品牌色和排版。
- **参考**: [Material Design 3](https://m3.material.io/)
- **文件**: `<GALLERY>\03-material\`

#### 04 · Fluent Design / Fluent 2
- **识别特征**: 柔和的表面、圆角、细边框与交互反馈，带有桌面软件气质。
- **适用场景**: 办公工具、桌面客户端、协作应用。
- **示例配色**: `#edf4fd · #235c9d · #243b5a`
- **使用时留意**: 保持信息层级清楚；透明与阴影只用于需要强调的层。
- **参考**: [Fluent 2](https://fluent2.microsoft.design/)
- **文件**: `<GALLERY>\04-fluent\`

#### 05 · 企业数据风 / Enterprise Data
- **识别特征**: 稳定网格、密集而有序的信息、表格与图表，优先支持高效操作。
- **适用场景**: SaaS、运营后台、数据分析。
- **示例配色**: `#161d27 · #0f62fe · #f6f7f8`
- **使用时留意**: 数字、表格和筛选器的可读性比装饰更重要。
- **文件**: `<GALLERY>\05-enterprise-data\`

#### 06 · 玻璃拟态 / Glassmorphism
- **识别特征**: 半透明面板、背景模糊、浅边框和叠层制造磨砂玻璃感。
- **适用场景**: 天气、音乐、创意展示、活动页。
- **示例配色**: `#5546c7 · #e07aaf · #ffcd6a`
- **使用时留意**: 复杂背景会降低文字对比度；正文区域要有足够清晰的底色。
- **文件**: `<GALLERY>\06-glassmorphism\`

#### 07 · 新拟态 / Neumorphism / Soft UI
- **识别特征**: 同色表面配合柔和高光与阴影，呈现轻微凸起或凹陷。
- **适用场景**: 音乐控件、概念展示、小面积装饰。
- **示例配色**: `#e4ebf3 · #7ca9c7 · #56677c`
- **使用时留意**: 低对比效果可能影响可访问性；核心按钮需要明显的边界与状态。
- **文件**: `<GALLERY>\07-neumorphism\`

#### 08 · 新粗野主义 / Neo-brutalism
- **识别特征**: 粗边框、硬阴影、鲜艳色块和夸张字体，表达强烈个性。
- **适用场景**: 创意品牌、作品集、趣味产品。
- **示例配色**: `#f5ed67 · #f7a1cf · #111111`
- **使用时留意**: 强烈视觉可能干扰长时间阅读；信息密集页要适度收敛。
- **文件**: `<GALLERY>\08-neo-brutalism\`

#### 09 · 编辑杂志风 / Editorial
- **识别特征**: 大标题、衬线字体、图文交错和精心控制的留白，强调阅读节奏。
- **适用场景**: 媒体、摄影、品牌故事、作品集。
- **示例配色**: `#f2eee7 · #1e1d1b · #c6a886`
- **使用时留意**: 移动端需重新安排图文顺序，避免标题过大造成拥挤。
- **文件**: `<GALLERY>\09-editorial\`

#### 10 · 像素风 / 复古游戏风 / Pixel / Retro
- **识别特征**: 像素块、等宽字、有限色盘和游戏界面元素带来复古趣味。
- **适用场景**: 小游戏、实验作品、趣味工具。
- **示例配色**: `#141c2e · #ffe36e · #fe8b99`
- **使用时留意**: 正文不要全部使用低分辨率字体；让游戏元素服务于实际操作。
- **关键词**: 像素风、2D、游戏风
- **文件**: `<GALLERY>\10-pixel-retro\`

#### 11 · 赛博霓虹风 / Cyber / Neon
- **识别特征**: 深色背景、荧光色、发光元素和科技感线条。
- **适用场景**: 游戏、音乐、科技主题展示。
- **示例配色**: `#080c1c · #54f1df · #fd5ed7`
- **使用时留意**: 发光效果使用过多会伤害可读性；确保文字与背景有充分对比。
- **文件**: `<GALLERY>\11-cyber-neon\`

#### 12 · 插画手绘风 / Illustrative / Hand-drawn
- **识别特征**: 手绘角色、有机图形和温暖配色营造亲近、轻松的氛围。
- **适用场景**: 教育、生活方式、儿童产品。
- **示例配色**: `#fff8ed · #8dc8a0 · #fa9c77`
- **使用时留意**: 插画应有统一的笔触与色盘，不要挡住关键操作。
- **文件**: `<GALLERY>\12-illustrative\`

#### 13 · 2D 卡通风 / 2D Cartoon
- **识别特征**: 平面角色、清楚的轮廓线、纯色填充和轻快的互动气氛。
- **适用场景**: 儿童产品、休闲游戏、教学工具。
- **示例配色**: `#d8f3f4 · #8bd1b5 · #f2765b`
- **使用时留意**: 角色和控件保持一致的线宽与色盘，避免装饰影响导航。
- **文件**: `<GALLERY>\13-cartoon-2d\`

#### 14 · 华丽极繁主义 / 哥特装饰 / Ornate Maximalism
- **识别特征**: 以中世纪哥特教堂为灵感：尖拱、玫瑰窗、花饰细线、宝石色与金色层层叠加，强调精致工艺和仪式感。
- **适用场景**: 艺术展览、奇幻叙事、珠宝与高端文化品牌。
- **示例配色**: `#4b1831 · #162c53 · #d9b770`
- **使用时留意**: 华丽来自细节与秩序；让装饰围绕主视觉与文字展开，正文仍需清晰。此例借鉴教堂建筑装饰，不代表所有极繁主义。
- **参考**: [V&A：哥特风格中的彩窗与装饰](https://www.vam.ac.uk/articles/the-gothic-style-an-introduction)
- **文件**: `<GALLERY>\14-maximalist\`

### 文化与历史（Culture & History）

#### 15 · 中世纪手抄本风 / Medieval Manuscript
- **识别特征**: 羊皮纸底色、装饰边框、衬线字与手抄本式插图。这里展示的是欧洲手抄本方向。
- **适用场景**: 历史内容、奇幻游戏、博物馆专题。
- **示例配色**: `#efe3c8 · #7e302d · #b88a43`
- **使用时留意**: 中世纪跨越多个地区与传统；具体项目应先确定时代和地域。
- **参考**: [Getty：中世纪手抄本](https://www.getty.edu/art/exhibitions/scriptorium/)
- **文件**: `<GALLERY>\15-medieval\`

#### 16 · 宗教艺术启发 / 彩窗 / Sacred Art / Stained Glass
- **识别特征**: 以宁静的留白、光线与彩窗结构表达神圣空间感；示例具体采用基督教哥特彩窗语汇。
- **适用场景**: 展览、历史文化内容、相关社群项目。
- **示例配色**: `#14243d · #d3a35f · #9f6b7a`
- **使用时留意**: 宗教传统各不相同，实际使用时应明确对象并核对符号含义。
- **参考**: [大都会艺术博物馆：宗教图像的跨文化差异](https://www.metmuseum.org/de/perspectives/virgin-mary-guanyin)
- **文件**: `<GALLERY>\16-sacred-art\`

#### 17 · 西域 / 敦煌艺术启发 / Silk Road / Dunhuang
- **识别特征**: 借鉴敦煌装饰的青绿、赭红、金色及莲花、卷草等纹样，形成壁画与丝路气质。
- **适用场景**: 文化展览、历史教育、旅游专题。
- **示例配色**: `#255b61 · #b25344 · #dfad63`
- **使用时留意**: "西域"涵盖广阔地区，不能用一套图案概括；此图只聚焦敦煌启发。
- **参考**: [敦煌研究院：莫高窟装饰图案](https://www.dha.ac.cn/info/1425/3618.htm)
- **文件**: `<GALLERY>\17-silk-road-dunhuang\`

#### 18 · 伊斯兰艺术启发 / 几何纹样 / Islamic Geometric
- **识别特征**: 重复的几何纹样、对称节奏、植物纹与书法传统；示例只采用抽象几何。
- **适用场景**: 文化展览、工艺档案、建筑专题。
- **示例配色**: `#092f3d · #caa96a · #b15f3d`
- **使用时留意**: "穆斯林风格"并非单一风格；涉及经文或书法时须确保文字准确且使用得体。
- **关键词**: 穆斯林风格
- **参考**: [大都会艺术博物馆：伊斯兰艺术几何纹样](https://www.metmuseum.org/es/essays/geometric-patterns-in-islamic-art)
- **文件**: `<GALLERY>\18-islamic-geometric\`

#### 19 · 中国现代设计风 / Chinese Contemporary
- **识别特征**: 现代网格与中文排版结合克制的中国红、留白和抽象几何。
- **适用场景**: 中国品牌、文化科技、现代产品。
- **示例配色**: `#f7f5f0 · #d94236 · #252d2c`
- **使用时留意**: 不要把中国风简化为红金龙凤；先确定品牌与受众。
- **文件**: `<GALLERY>\19-chinese-contemporary\`

#### 20 · 后现代风 / Postmodern / Memphis-inspired
- **识别特征**: 不对称构图、几何拼贴、鲜明配色和风格混搭，带有戏谑感。
- **适用场景**: 创意工作室、时尚、艺术活动。
- **示例配色**: `#f6c848 · #e25975 · #48bfc0`
- **使用时留意**: 后现代不是任意堆叠；文字、导航和操作仍需清晰。
- **参考**: [V&A：什么是后现代主义](https://www.vam.ac.uk/articles/what-is-postmodernism)
- **文件**: `<GALLERY>\20-postmodern\`

#### 21 · 中国水墨风 / Chinese Ink Wash
- **识别特征**: 墨色层次、山水意象、纸色留白和小面积朱印。
- **适用场景**: 文化、阅读、茶艺、艺术展览。
- **示例配色**: `#f4f0e7 · #444d49 · #b7483b`
- **使用时留意**: 留白与笔墨节奏比贴一张山水背景更关键；避免压低正文对比度。
- **参考**: [大都会艺术博物馆：中国山水画](https://www.metmuseum.org/exhibitions/listings/2017/streams-and-mountains)
- **文件**: `<GALLERY>\21-ink-wash\`

## Using the gallery files

`<GALLERY>` = the `gallery` directory next to this `SKILL.md`

- **Browse all styles at once**: open `<GALLERY>/gallery.html` in a browser.
  It supports search (e.g. 像素、水墨、宗教) and category filters
  (全部 / 视觉与交互 / 文化与历史).
- **Read one style's spec**: `<GALLERY>/<NN-name>/README.md`
- **See one style's schematic**: `<GALLERY>/<NN-name>/preview.svg`
  (open in a browser; SVGs are scalable and text-editable).
- **Regenerate the whole gallery**: run
  `python <GALLERY>/generate_gallery.py`.
  The generator rewrites every `README.md`, `preview.svg`, `gallery.html`,
  and the gallery index. Edit style facts in `generate_gallery.py`, then
  regenerate, then mirror any catalog change back into this skill.

## Design-system references (beyond this gallery)

- [Google Material Design 3](https://m3.material.io/)
- [Microsoft Fluent 2](https://fluent2.microsoft.design/)
- [IBM Carbon Design System](https://carbondesignsystem.com/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Figma：网页设计趋势与风格](https://www.figma.com/resource-library/web-design-trends/)
- [Webflow：玻璃拟态](https://webflow.com/blog/glassmorphism)
- [Webflow：粗野主义网页设计](https://webflow.com/blog/10-brutalist-websites)

## Notes for the planner

- The SVG previews are **original schematics**, not official screenshots of
  the referenced design systems. Treat them as direction, not spec.
- Cultural styles (15–18, 21) carry real cultural/religious meaning. When
  planning, verify the specific tradition, era, and region, and check symbol
  accuracy before using them.
- For a product whose subject is color itself (the original note was written
  for `RGB_selection_toy`), start from 极简主义 or 扁平化 to 突出颜色本身;
  try 像素风 or 插画手绘风 to 强调玩具感; try 赛博霓虹风 to 强调发光效果.
  See `<GALLERY>\README.md`.
