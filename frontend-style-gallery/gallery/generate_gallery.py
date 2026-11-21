"""Generate the editable SVG previews and Chinese notes for the style gallery."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent
W, H = 960, 560


def rect(x, y, w, h, fill, r=0, stroke=None, sw=1, extra=""):
    border = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{border} {extra}/>'


def line(x1, y1, x2, y2, color, sw=2, extra=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" {extra}/>'


def circle(x, y, r, fill, extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {extra}/>'


def text(x, y, value, size=20, color="#111", weight=400, family="Arial, sans-serif", extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" font-family="{family}" {extra}>{escape(value)}</text>'


def path(d, fill="none", stroke="none", sw=1, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def svg(title, body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">'
            f'<title>{escape(title)}</title><defs>{defs}</defs>{body}</svg>\n')


def minimalist():
    b = [rect(0, 0, W, H, "#f8f7f3"), text(70, 65, "FORM / FUNCTION", 16, "#272722", 700),
         text(698, 65, "WORK    ABOUT    CONTACT", 13, "#686963"), line(70, 90, 890, 90, "#dadad3", 1),
         text(70, 202, "A quieter way", 61, "#242821", 600), text(70, 272, "to make things.", 61, "#242821", 600),
         text(73, 330, "Useful tools. Thoughtful details. Room to breathe.", 18, "#777a71"),
         rect(70, 386, 190, 50, "#272c26", 3), text(102, 418, "Explore work  ↗", 16, "#ffffff", 600),
         line(70, 491, 890, 491, "#dadad3", 1), text(70, 521, "01 / SIMPLE", 13, "#797b73"),
         text(780, 521, "EST. 2026", 13, "#797b73")]
    return svg("极简主义风格示例", "".join(b))


def flat():
    b = [rect(0, 0, W, H, "#f4f7fb"), rect(0, 0, 220, H, "#19457e"),
         text(34, 52, "TASKFLOW", 21, "#fff", 700),
         *[text(36, 126+i*60, label, 17, "#fff" if i == 0 else "#bad0e9", 600 if i == 0 else 400)
           for i, label in enumerate(["▣  Dashboard", "□  Projects", "☑  My tasks", "◷  Calendar", "⚙  Settings"])],
         text(258, 58, "Overview", 31, "#193459", 700), text(260, 91, "Your workspace at a glance", 16, "#71829a"),
         rect(258, 129, 190, 130, "#4c82d5", 12), rect(466, 129, 190, 130, "#25b09b", 12),
         rect(674, 129, 190, 130, "#f4a743", 12),
         text(282, 174, "PROJECTS", 15, "#e8f1ff", 600), text(282, 229, "12", 42, "#fff", 700),
         text(490, 174, "COMPLETED", 15, "#e2fff8", 600), text(490, 229, "48", 42, "#fff", 700),
         text(698, 174, "UPCOMING", 15, "#fff7e9", 600), text(698, 229, "07", 42, "#fff", 700),
         rect(258, 291, 606, 214, "#fff", 12), text(284, 333, "Recent tasks", 20, "#193459", 700),
         *[line(284, 364+i*47, 836, 364+i*47, "#e9eef5", 1) for i in range(3)],
         *[text(286, 394+i*47, label, 16, "#46576f") for i, label in enumerate(["Design system update", "Homepage review", "Prepare release notes"])],
         *[rect(736, 376+i*47, 92, 25, "#dcecfb" if i != 1 else "#e0f7ed", 12) for i in range(3)]]
    return svg("扁平化风格示例", "".join(b))


def material():
    defs = '<filter id="shadow"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-opacity=".12"/></filter>'
    b = [rect(0, 0, W, H, "#f5f3fa"), rect(0, 0, W, 78, "#e9e4f5"),
         text(46, 51, "◉  MATERIA", 24, "#302954", 700), text(690, 49, "Explore     Saved     Profile", 16, "#51466a"),
         text(60, 138, "Discover something new", 38, "#2f2942", 600),
         text(61, 172, "Curated spaces for curious minds", 16, "#6a6379"),
         rect(60, 214, 395, 266, "#dcd3f4", 28, extra='filter="url(#shadow)"'),
         circle(258, 321, 84, "#a58bdf"), circle(225, 299, 48, "#c3b1ed"),
         text(88, 426, "Creative spaces", 27, "#2f2942", 700),
         rect(486, 214, 414, 118, "#fff", 24, extra='filter="url(#shadow)"'),
         text(517, 260, "Start with a prompt", 21, "#2f2942", 600),
         text(517, 290, "Build your first collection", 15, "#6a6379"),
         rect(486, 353, 414, 127, "#fff", 24, extra='filter="url(#shadow)"'),
         text(517, 403, "Browse the library", 21, "#2f2942", 600),
         rect(770, 385, 99, 45, "#6750a4", 23), text(793, 414, "OPEN", 14, "#fff", 700)]
    return svg("Material Design 风格示例", "".join(b), defs)


def fluent():
    defs = '<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#dbeafa"/><stop offset="1" stop-color="#f4e8f3"/></linearGradient><filter id="sh"><feDropShadow dx="0" dy="6" stdDeviation="10" flood-opacity=".10"/></filter>'
    b = [rect(0, 0, W, H, "url(#bg)"), rect(38, 34, 884, 490, "#ffffff", 18, "#dde2ec", 1, 'filter="url(#sh)"'),
         rect(38, 34, 205, 490, "#f5f7fb", 18), text(68, 78, "✦  Workspace", 21, "#243b5a", 700),
         *[text(72, 149+i*51, label, 16, "#235c9d" if i == 0 else "#69788e") for i, label in enumerate(["⌂   Home", "▤   Documents", "▦   Boards", "◷   Activity"])],
         line(243, 34, 243, 524, "#e8ebf1", 1), text(279, 87, "Good morning, Alex", 30, "#20324e", 600),
         text(280, 117, "Pick up where you left off", 16, "#6a798d"),
         rect(280, 157, 595, 91, "#edf4fd", 12), circle(325, 203, 23, "#d6e8ff"),
         text(367, 197, "Project notes", 20, "#243b5a", 600), text(367, 223, "Edited 2 hours ago", 14, "#718099"),
         rect(280, 271, 281, 185, "#fff", 12, "#dfe5ee"), rect(582, 271, 293, 185, "#fff", 12, "#dfe5ee"),
         rect(301, 292, 239, 88, "#cce3f9", 8), rect(603, 292, 251, 88, "#e5dcf8", 8),
         text(301, 412, "Planning board", 19, "#243b5a", 600), text(603, 412, "Team library", 19, "#243b5a", 600)]
    return svg("Fluent Design 风格示例", "".join(b), defs)


def enterprise():
    b = [rect(0, 0, W, H, "#f6f7f8"), rect(0, 0, W, 62, "#161d27"), text(28, 42, "NEXUS / ANALYTICS", 19, "#fff", 700),
         text(728, 40, "Export   Help   ● Admin", 14, "#c6cdd7"), rect(0, 62, 196, H-62, "#fff"),
         *[text(27, 120+i*49, label, 15, "#0f62fe" if i == 0 else "#657282", 600 if i == 0 else 400)
           for i, label in enumerate(["Overview", "Performance", "Customers", "Reports", "Settings"])],
         line(196, 62, 196, H, "#e0e4e8", 1), text(228, 118, "Performance overview", 28, "#1b2733", 600),
         text(229, 148, "Last 30 days  /  Updated today", 14, "#7b8793"),
         *[rect(228+i*225, 177, 210, 101, "#fff", 2, "#dce1e6") for i in range(3)],
         *[text(246+i*225, 208, label, 13, "#667481") for i, label in enumerate(["REVENUE", "ACTIVE USERS", "CONVERSION"])],
         *[text(246+i*225, 254, value, 30, "#1b2733", 700) for i, value in enumerate(["$48,290", "12,804", "8.4%"])],
         rect(228, 301, 659, 206, "#fff", 2, "#dce1e6"), text(248, 335, "Traffic trend", 18, "#1b2733", 600),
         *[line(249, 374+i*34, 866, 374+i*34, "#e7ebef", 1) for i in range(4)],
         path("M250 455 L320 426 L390 438 L460 397 L530 411 L600 382 L670 394 L740 357 L865 373", "none", "#0f62fe", 4)]
    return svg("企业数据风格示例", "".join(b))


def glass():
    defs = '<linearGradient id="g" x2="1" y2="1"><stop stop-color="#5546c7"/><stop offset=".5" stop-color="#e07aaf"/><stop offset="1" stop-color="#f5b279"/></linearGradient><filter id="blur"><feGaussianBlur stdDeviation="32"/></filter>'
    b = [rect(0, 0, W, H, "url(#g)"), circle(765, 108, 175, "#ffcd6a", 'opacity=".7" filter="url(#blur)"'),
         circle(134, 450, 150, "#5ddbd2", 'opacity=".6" filter="url(#blur)"'),
         rect(64, 55, 832, 450, "#ffffff", 28, "#ffffff", 2, 'fill-opacity=".19" stroke-opacity=".55"'),
         text(105, 103, "AURORA", 20, "#fff", 700), text(688, 103, "Home    Explore    Profile", 15, "#fff"),
         text(105, 235, "Color the", 58, "#fff", 700), text(105, 298, "moment.", 58, "#fff", 700),
         text(108, 340, "Find a palette for every feeling.", 18, "#fff"),
         rect(107, 382, 160, 49, "#fff", 24, extra='fill-opacity=".88"'), text(136, 413, "Explore colors", 15, "#543f86", 700),
         rect(611, 172, 220, 255, "#fff", 22, "#fff", 1, 'fill-opacity=".25" stroke-opacity=".55"'),
         circle(719, 262, 62, "#ffe3bb", 'fill-opacity=".7"'), text(646, 374, "Soft sunset", 22, "#fff", 600),
         text(646, 402, "#FFB48C   #E98FD1", 13, "#fff")]
    return svg("玻璃拟态风格示例", "".join(b), defs)


def neumorphism():
    defs = '<filter id="out"><feDropShadow dx="-8" dy="-8" stdDeviation="10" flood-color="#fff"/><feDropShadow dx="8" dy="8" stdDeviation="10" flood-color="#aab8cb"/></filter><filter id="in"><feGaussianBlur stdDeviation="0"/></filter>'
    b = [rect(0, 0, W, H, "#e4ebf3"), text(70, 73, "SOFT / SOUND", 21, "#617186", 700),
         text(730, 73, "Discover    Library", 15, "#7d8da0"),
         rect(147, 110, 665, 356, "#e4ebf3", 30, extra='filter="url(#out)"'),
         circle(479, 239, 92, "#e4ebf3", 'filter="url(#out)"'),
         circle(479, 239, 70, "#9bc5d9"), circle(479, 239, 49, "#7ca9c7"),
         text(401, 361, "Blue Hours", 29, "#56677c", 700), text(424, 390, "Lina Solis", 17, "#8192a5"),
         circle(390, 427, 22, "#e4ebf3", 'filter="url(#out)"'), circle(479, 427, 26, "#e4ebf3", 'filter="url(#out)"'),
         circle(568, 427, 22, "#e4ebf3", 'filter="url(#out)"'),
         text(381, 433, "‹", 22, "#718ba4", 700), text(473, 434, "▶", 16, "#718ba4"), text(560, 433, "›", 22, "#718ba4", 700)]
    return svg("新拟态风格示例", "".join(b), defs)


def brutalist():
    b = [rect(0, 0, W, H, "#f5ed67"), rect(27, 24, 906, 71, "#fff", 0, "#131313", 4),
         text(48, 73, "LOUD / LAB", 31, "#111", 900, "Arial Black, Arial, sans-serif"),
         text(642, 67, "WORK  ABOUT  CONTACT", 16, "#111", 800),
         rect(48, 129, 547, 326, "#111"), rect(38, 119, 547, 326, "#f7a1cf", 0, "#111", 4),
         text(65, 208, "MAKE IT", 68, "#111", 900, "Arial Black, Arial, sans-serif"),
         text(65, 288, "LOUD.", 86, "#111", 900, "Arial Black, Arial, sans-serif"),
         text(67, 348, "Ideas that refuse to blend in.", 20, "#111", 700),
         rect(69, 375, 188, 51, "#fff", 0, "#111", 3), text(91, 409, "SEE THE WORK →", 17, "#111", 800),
         rect(640, 145, 262, 272, "#111"), rect(630, 135, 262, 272, "#78d7e5", 0, "#111", 4),
         circle(762, 250, 88, "#f5ed67", 'stroke="#111" stroke-width="4"'),
         text(691, 255, "★  WOW", 28, "#111", 900),
         text(632, 474, "NO BORING IDEAS. EVER.", 19, "#111", 900)]
    return svg("新粗野主义风格示例", "".join(b))


def editorial():
    b = [rect(0, 0, W, H, "#f2eee7"), text(52, 52, "THE DAILY FORM", 24, "#211f1d", 700, "Georgia, serif"),
         text(706, 52, "ART     CULTURE     IDEAS", 14, "#5a554f", 600), line(52, 72, 908, 72, "#24211e", 2),
         text(52, 143, "An eye for", 65, "#1e1d1b", 400, "Georgia, serif"),
         text(52, 213, "the unexpected.", 65, "#1e1d1b", 400, "Georgia, serif"),
         text(54, 258, "ISSUE 04    /    DESIGN & CULTURE", 14, "#8d684e", 700),
         rect(53, 292, 515, 206, "#c6a886"),
         path("M53 498 L210 351 L310 431 L420 319 L568 498 Z", "#675f55"),
         circle(423, 359, 37, "#e8d3ab"),
         line(606, 292, 908, 292, "#292623", 1), text(607, 335, "FEATURE STORY", 15, "#9b6f54", 700),
         text(606, 386, "Finding beauty", 33, "#24211e", 400, "Georgia, serif"),
         text(606, 426, "in ordinary", 33, "#24211e", 400, "Georgia, serif"),
         text(606, 466, "moments", 33, "#24211e", 400, "Georgia, serif"),
         line(52, 524, 908, 524, "#24211e", 1)]
    return svg("编辑杂志风格示例", "".join(b))


def pixel():
    b = [rect(0, 0, W, H, "#141c2e"), rect(34, 30, 892, 500, "#1f2c42", 0, "#8bdbb2", 5),
         text(70, 86, "★ PIXEL PLAYGROUND ★", 32, "#ffe36e", 900, "monospace"),
         text(700, 84, "SCORE  00850", 18, "#9bebb7", 700, "monospace"),
         line(69, 108, 890, 108, "#8bdbb2", 4),
         text(92, 197, "CHOOSE YOUR", 52, "#fff", 900, "monospace"),
         text(92, 267, "NEXT COLOR_", 52, "#fe8b99", 900, "monospace"),
         text(94, 316, "A tiny adventure in RGB.", 20, "#b8d5cc", 600, "monospace"),
         rect(94, 354, 250, 60, "#ffe36e", 0, "#121b2c", 4), text(124, 393, "▶ START GAME", 23, "#171d2b", 900, "monospace"),
         *[rect(586+x*36, 168+y*36, 31, 31, ["#fe8b99", "#ffe36e", "#67d7bc", "#7385df"][(x+y)%4])
           for y in range(6) for x in range(7) if (x+y)%3 != 0],
         text(70, 485, "PRESS ENTER TO BEGIN", 16, "#8bdbb2", 700, "monospace")]
    return svg("复古像素风格示例", "".join(b))


def cyber():
    defs = '<linearGradient id="c" x2="1" y2="1"><stop stop-color="#080c1c"/><stop offset="1" stop-color="#1b1235"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="4"/></filter>'
    b = [rect(0, 0, W, H, "url(#c)"),
         *[line(0, 360+i*35, 960, 360+i*35, "#4a246b", 1) for i in range(6)],
         *[line(480, 350, x, 560, "#4a246b", 1) for x in range(-200, 1200, 100)],
         text(64, 73, "// CHROMA SYSTEM", 20, "#54f1df", 700, "monospace"),
         text(712, 73, "EXPLORE  /  01", 17, "#fd5ed7", 700, "monospace"),
         text(64, 201, "THE FUTURE", 67, "#ffffff", 900, "Arial Black, Arial, sans-serif"),
         text(64, 277, "IS IN COLOR", 67, "#54f1df", 900, "Arial Black, Arial, sans-serif"),
         line(64, 297, 610, 297, "#fd5ed7", 4),
         text(66, 344, "BUILD  //  MIX  //  CREATE", 21, "#c5b5e9", 700, "monospace"),
         rect(66, 385, 221, 57, "#fd5ed7", 0), text(96, 423, "ENTER LAB  →", 20, "#120d21", 900, "monospace"),
         circle(762, 265, 120, "#fd5ed7", 'opacity=".5" filter="url(#glow)"'),
         circle(762, 265, 98, "#15152c", 'stroke="#54f1df" stroke-width="7"'),
         circle(762, 265, 70, "#1d1435", 'stroke="#fd5ed7" stroke-width="5"'),
         circle(762, 265, 37, "#54f1df")]
    return svg("赛博霓虹风格示例", "".join(b), defs)


def illustration():
    b = [rect(0, 0, W, H, "#fff8ed"), circle(780, 430, 228, "#fae7d5"),
         text(60, 71, "little things ☀", 27, "#486e64", 700), text(704, 69, "Explore    About", 16, "#67877d"),
         text(63, 198, "Make space", 58, "#345e58", 700), text(63, 262, "for play.", 58, "#345e58", 700),
         text(65, 314, "Colorful ideas for everyday curious minds.", 18, "#64817a"),
         rect(65, 356, 190, 56, "#fa9c77", 28), text(96, 393, "Let's explore  →", 18, "#fff", 700),
         path("M610 408 C560 310 585 183 697 175 C801 160 872 248 832 353 C819 405 760 436 703 430 Z", "#8dc8a0"),
         circle(698, 244, 65, "#ffcf85"), circle(789, 269, 47, "#ffac90"),
         path("M635 380 C676 302 737 344 750 407 Z", "#4e8f78"),
         circle(670, 232, 7, "#345e58"), circle(711, 232, 7, "#345e58"),
         path("M673 256 Q694 274 714 256", "none", "#345e58", 4),
         circle(844, 174, 19, "#ffd574"), circle(575, 194, 10, "#fa9c77")]
    return svg("插画手绘风格示例", "".join(b))


def cartoon_2d():
    b = [rect(0, 0, W, H, "#d8f3f4"), rect(34, 30, 892, 500, "#fffdf6", 30, "#263d42", 4),
         text(68, 80, "HAPPY PLANET", 27, "#263d42", 900), text(691, 78, "PLAY   LEARN   ABOUT", 16, "#263d42", 700),
         text(72, 204, "A world of", 58, "#263d42", 900), text(72, 275, "little wonders!", 58, "#f2765b", 900),
         text(75, 318, "Explore, collect, and make something bright.", 18, "#607477"),
         rect(74, 363, 191, 57, "#f7c952", 28, "#263d42", 3), text(105, 401, "LET'S PLAY", 20, "#263d42", 900),
         circle(710, 275, 126, "#8bd1b5", 'stroke="#263d42" stroke-width="5"'),
         circle(671, 247, 10, "#263d42"), circle(751, 247, 10, "#263d42"),
         path("M669 292 Q710 334 754 292", "none", "#263d42", 5),
         circle(608, 182, 33, "#f7c952", 'stroke="#263d42" stroke-width="4"'),
         circle(842, 191, 21, "#f2765b", 'stroke="#263d42" stroke-width="4"'),
         path("M575 401 Q701 448 845 399", "none", "#263d42", 4)]
    return svg("2D 卡通风格示例", "".join(b))


def maximalist():
    gold, pale, burgundy, blue = "#d9b770", "#f4dfaa", "#4b1831", "#162c53"
    defs = '<radialGradient id="rose"><stop stop-color="#ca8d6b"/><stop offset=".6" stop-color="#503c74"/><stop offset="1" stop-color="#142d51"/></radialGradient>'
    b = [rect(0, 0, W, H, "#1d1524"), rect(17, 16, 926, 528, burgundy, 2, gold, 3),
         rect(31, 30, 898, 500, "none", 1, "#8b654b", 1),
         rect(46, 45, 868, 470, "none", 1, gold, 1),
         *[circle(74+i*38, 45, 3, gold) for i in range(22)],
         *[circle(74+i*38, 515, 3, gold) for i in range(22)],
         text(74, 91, "✦  ATELIER CATHEDRAL  ✦", 20, pale, 700, "Georgia,serif"),
         text(698, 90, "COLLECTION    STORY", 13, pale, 600),
         line(75, 108, 885, 108, gold, 1),
         path("M75 112 Q480 140 885 112", "none", "#8b654b", 1),
         text(79, 210, "The art of", 60, pale, 500, "Georgia,serif"),
         text(79, 280, "abundance", 66, gold, 600, "Georgia,serif"),
         line(80, 301, 469, 301, gold, 2),
         text(82, 344, "A study of ornament, light,", 18, "#ead8c5", 400, "Georgia,serif"),
         text(82, 370, "and meticulous detail.", 18, "#ead8c5", 400, "Georgia,serif"),
         rect(81, 405, 200, 51, "#8e3150", 1, gold, 2),
         text(111, 438, "EXPLORE THE ART", 15, pale, 700, "Georgia,serif"),
         path("M562 468 L562 250 Q562 158 720 91 Q878 158 878 250 L878 468 Z", blue, gold, 5),
         path("M578 452 L578 252 Q578 172 720 111 Q862 172 862 252 L862 452 Z", "none", "#a17557", 2),
         circle(720, 290, 134, "url(#rose)", f'stroke="{gold}" stroke-width="5"'),
         circle(720, 290, 118, "none", f'stroke="{pale}" stroke-width="2"'),
         circle(720, 290, 84, "none", f'stroke="{gold}" stroke-width="3"')]
    for angle in range(0, 360, 30):
        b.append(path("M720 203 Q741 235 720 285 Q699 235 720 203 Z", "#a24862", gold, 2,
                      f'transform="rotate({angle} 720 290)"'))
        b.append(path("M720 163 Q737 183 720 207 Q703 183 720 163 Z", "#477492", gold, 1,
                      f'transform="rotate({angle} 720 290)"'))
    b += [circle(720, 290, 42, "#b5845e", f'stroke="{gold}" stroke-width="3"'),
          circle(720, 290, 24, "#f2d79c", 'stroke="#4b1831" stroke-width="2"'),
          path("M692 291 Q720 247 748 291 Q720 335 692 291 Z", "none", "#622344", 3),
          *[path(f"M{x-17} 466 Q{x} 418 {x+17} 466", "none", gold, 2) for x in (615, 666, 774, 825)],
          line(75, 477, 477, 477, gold, 1),
          text(80, 500, "ORNAMENT  •  LIGHT  •  CRAFT", 13, pale, 700, "Georgia,serif")]
    return svg("哥特教堂启发的华丽极繁主义风格示例", "".join(b), defs)


def medieval():
    b = [rect(0, 0, W, H, "#4c241f"), rect(33, 27, 894, 506, "#efe3c8", 4, "#bb9c55", 7),
         rect(51, 45, 858, 470, "none", 1, "#ae7b3d", 2),
         *[circle(x, y, 11, "#b88a43") for x in (77, 883) for y in (71, 488)],
         text(85, 95, "THE GILDED ATLAS", 28, "#633727", 700, "Georgia,serif"),
         line(85, 112, 875, 112, "#a37c4a", 2),
         text(86, 205, "Stories from", 60, "#4d2a24", 600, "Georgia,serif"),
         text(86, 270, "another age", 60, "#4d2a24", 600, "Georgia,serif"),
         text(88, 320, "Manuscripts  •  Maps  •  Legends", 19, "#8a5f45", 600, "Georgia,serif"),
         rect(88, 366, 216, 52, "#7e302d", 3), text(120, 400, "OPEN THE BOOK", 17, "#f8e7bd", 700, "Georgia,serif"),
         rect(622, 149, 220, 280, "#d8c49c", 110, "#9a6b3f", 5),
         path("M647 395 L700 256 L734 335 L776 213 L818 395 Z", "#7c834c"),
         circle(713, 220, 32, "#c59743"),
         text(617, 469, "✦  CHRONICLE  ✦", 18, "#7e302d", 700, "Georgia,serif")]
    return svg("中世纪手抄本风格示例", "".join(b))


def sacred():
    b = [rect(0, 0, W, H, "#14243d"), rect(32, 29, 896, 502, "#f7f2e5", 3),
         text(67, 83, "LIGHT & STILLNESS", 24, "#243451", 700, "Georgia,serif"),
         text(716, 80, "EXHIBITION  /  2026", 14, "#7a6a52"), line(67, 104, 895, 104, "#b59b6b", 2),
         text(70, 217, "A place for", 61, "#243451", 500, "Georgia,serif"),
         text(70, 285, "reflection", 61, "#243451", 500, "Georgia,serif"),
         text(73, 330, "Art, light and shared human stories.", 18, "#776e61"),
         rect(74, 373, 204, 49, "#8b673d", 2), text(106, 405, "VIEW THE WORK", 16, "#fff", 700),
         path("M615 430 L615 260 A115 115 0 0 1 845 260 L845 430 Z", "#253e68", "#a8894e", 8),
         path("M640 407 L640 268 A90 90 0 0 1 820 268 L820 407 Z", "#596ca0", "#d3ad67", 5),
         circle(730, 273, 50, "#d3a35f"),
         path("M641 402 L730 300 L820 402 Z", "#9f6b7a", "#d9b678", 4),
         line(730, 169, 730, 430, "#dab977", 5), line(640, 307, 820, 307, "#dab977", 5)]
    return svg("宗教艺术启发的彩窗风格示例", "".join(b))


def silk_road():
    b = [rect(0, 0, W, H, "#c18b5d"), rect(27, 24, 906, 512, "#eee0be", 5, "#693e34", 5),
         *[circle(74+i*61, 66, 12, "#b14f3e") for i in range(14)],
         text(69, 111, "SILK ROAD ARCHIVE", 23, "#654138", 700),
         text(70, 218, "Colors across", 58, "#793f36", 700, "Georgia,serif"),
         text(70, 285, "the desert", 58, "#793f36", 700, "Georgia,serif"),
         text(72, 331, "A visual journey through Dunhuang motifs.", 18, "#8d6654"),
         rect(72, 372, 202, 51, "#255b61", 2), text(100, 406, "EXPLORE ARCHIVE", 15, "#f7e8bf", 700),
         rect(603, 132, 259, 300, "#255b61", 126, "#aa6748", 7),
         path("M630 401 Q653 304 730 294 Q811 305 833 401 Z", "#bd6b47"),
         path("M640 281 Q730 136 823 281 Q730 236 640 281 Z", "#dfad63"),
         circle(730, 267, 46, "#d7ae66"), circle(730, 267, 25, "#b25344"),
         *[circle(628+i*33, 455, 7, "#255b61") for i in range(8)],
         text(670, 493, "敦煌  /  DUNHUANG", 18, "#654138", 700)]
    return svg("西域敦煌艺术启发风格示例", "".join(b))


def islamic():
    b = [rect(0, 0, W, H, "#092f3d"), rect(26, 23, 908, 514, "#f4eedc", 4, "#caa96a", 5),
         rect(43, 40, 874, 480, "none", 2, "#caa96a", 2),
         text(77, 96, "GEOMETRY & LIGHT", 25, "#0b4551", 700),
         text(75, 202, "Patterns of", 58, "#123f49", 600, "Georgia,serif"),
         text(75, 270, "connection", 58, "#123f49", 600, "Georgia,serif"),
         text(77, 315, "Explore geometry, craft and visual rhythm.", 18, "#687d77"),
         rect(77, 360, 211, 54, "#0b6570", 3), text(105, 395, "VIEW COLLECTION", 16, "#fff", 700),
         rect(574, 134, 286, 307, "#d7c18b", 1, "#0b6570", 4)]
    for y in (183, 259, 335, 411):
        for x in (625, 704, 783):
            b.extend([rect(x-28, y-28, 56, 56, "none", 0, "#0b6570", 3, f'transform="rotate(45 {x} {y})"'),
                      circle(x, y, 23, "none", 'stroke="#b15f3d" stroke-width="3"')])
    return svg("伊斯兰艺术启发的几何纹样风格示例", "".join(b))


def chinese_modern():
    b = [rect(0, 0, W, H, "#f7f5f0"), text(62, 68, "观色  /  CHROMA", 25, "#252d2c", 700),
         text(720, 65, "作品     关于     联系", 16, "#68736e"), line(62, 90, 898, 90, "#d6d7d0", 1),
         rect(622, 133, 244, 310, "#d94236", 4),
         circle(744, 267, 86, "#f6d9b8"),
         path("M667 319 Q744 188 820 320", "none", "#d94236", 22),
         text(70, 227, "把颜色，", 65, "#252d2c", 700, "Microsoft YaHei, sans-serif"),
         text(70, 307, "变成灵感。", 65, "#252d2c", 700, "Microsoft YaHei, sans-serif"),
         text(75, 350, "A contemporary study in color and form.", 18, "#68736e"),
         rect(75, 387, 185, 50, "#252d2c", 2), text(119, 419, "探索作品  →", 17, "#fff", 700),
         line(62, 489, 898, 489, "#d6d7d0", 1), text(64, 521, "设计 / 文化 / 日常", 14, "#68736e")]
    return svg("中国现代设计风格示例", "".join(b))


def postmodern():
    b = [rect(0, 0, W, H, "#eee9df"),
         *[circle(88+i*110, 75, 15, "#171e3d") for i in range(8)],
         rect(43, 110, 503, 366, "#f6c848", 0, "#171e3d", 4),
         text(71, 200, "RULES?", 80, "#171e3d", 900, "Arial Black,Arial,sans-serif"),
         text(71, 280, "REMIX.", 75, "#e25975", 900, "Arial Black,Arial,sans-serif"),
         text(76, 334, "A studio for unexpected ideas.", 20, "#171e3d", 700),
         rect(76, 366, 188, 54, "#171e3d"), text(105, 401, "SEE PROJECTS", 17, "#fff", 800),
         rect(634, 96, 221, 165, "#48bfc0", 0, "#171e3d", 4, 'transform="rotate(12 744 178)"'),
         circle(718, 338, 98, "#e25975", 'stroke="#171e3d" stroke-width="4"'),
         path("M723 265 L815 413 L630 413 Z", "#f6c848", "#171e3d", 4),
         rect(570, 428, 316, 46, "#f3a869", 0, "#171e3d", 3),
         text(602, 459, "DESIGN IS A QUESTION", 19, "#171e3d", 900)]
    return svg("后现代风格示例", "".join(b))


def ink_wash():
    b = [rect(0, 0, W, H, "#f4f0e7"),
         path("M430 450 Q545 350 611 216 Q660 118 710 170 Q740 200 775 307 Q814 406 920 450 Z", "#d0d1c9"),
         path("M485 450 Q568 332 616 287 Q657 214 690 258 Q742 342 796 450 Z", "#92968d"),
         path("M577 451 Q646 344 692 336 Q750 333 839 450 Z", "#444d49"),
         path("M530 468 Q660 428 908 475", "none", "#b7bbb2", 25, 'opacity=".5"'),
         text(72, 91, "山 水 之 间", 31, "#26332f", 600, "serif"),
         line(74, 110, 410, 110, "#6c736d", 1),
         text(74, 227, "留白之间", 61, "#26332f", 500, "serif"),
         text(77, 292, "自有天地", 61, "#26332f", 500, "serif"),
         text(78, 348, "Ink, space, and quiet motion.", 18, "#737c75"),
         rect(78, 387, 173, 48, "#26332f", 2), text(107, 418, "观赏作品", 18, "#f4f0e7", 600),
         rect(821, 83, 40, 40, "#b7483b"), text(829, 111, "印", 23, "#fff", 700, "serif")]
    return svg("水墨风格示例", "".join(b))


STYLES = [
    ("01-minimalist", "极简主义", "Minimalism", "留白、克制的配色、清晰的字体层级，让内容成为主角。", "品牌官网、作品集、专注型工具", "页面可能显得单薄；需要认真处理排版、间距和对比度。", "#f8f7f3 · #272c26 · #777a71", minimalist),
    ("02-flat", "扁平化", "Flat Design", "用纯色、简单图标和规整卡片组织信息，减少材质模拟。", "移动应用、后台、轻量产品", "不要让按钮与普通色块难以区分；用状态、文案和对比建立交互提示。", "#19457e · #4c82d5 · #25b09b", flat),
    ("03-material", "Material Design", "Material Design 3", "以色彩角色、层级、圆角组件和动效构建统一界面。", "跨平台应用、功能较多的产品", "参考官方组件规范，同时建立自己的品牌色和排版。", "#6750a4 · #e9e4f5 · #2f2942", material),
    ("04-fluent", "Fluent Design", "Fluent 2", "柔和的表面、圆角、细边框与交互反馈，带有桌面软件气质。", "办公工具、桌面客户端、协作应用", "保持信息层级清楚；透明与阴影只用于需要强调的层。", "#edf4fd · #235c9d · #243b5a", fluent),
    ("05-enterprise-data", "企业数据风", "Enterprise Data", "稳定网格、密集而有序的信息、表格与图表，优先支持高效操作。", "SaaS、运营后台、数据分析", "数字、表格和筛选器的可读性比装饰更重要。", "#161d27 · #0f62fe · #f6f7f8", enterprise),
    ("06-glassmorphism", "玻璃拟态", "Glassmorphism", "半透明面板、背景模糊、浅边框和叠层制造磨砂玻璃感。", "天气、音乐、创意展示、活动页", "复杂背景会降低文字对比度；正文区域要有足够清晰的底色。", "#5546c7 · #e07aaf · #ffcd6a", glass),
    ("07-neumorphism", "新拟态", "Neumorphism / Soft UI", "同色表面配合柔和高光与阴影，呈现轻微凸起或凹陷。", "音乐控件、概念展示、小面积装饰", "低对比效果可能影响可访问性；核心按钮需要明显的边界与状态。", "#e4ebf3 · #7ca9c7 · #56677c", neumorphism),
    ("08-neo-brutalism", "新粗野主义", "Neo-brutalism", "粗边框、硬阴影、鲜艳色块和夸张字体，表达强烈个性。", "创意品牌、作品集、趣味产品", "强烈视觉可能干扰长时间阅读；信息密集页要适度收敛。", "#f5ed67 · #f7a1cf · #111111", brutalist),
    ("09-editorial", "编辑杂志风", "Editorial", "大标题、衬线字体、图文交错和精心控制的留白，强调阅读节奏。", "媒体、摄影、品牌故事、作品集", "移动端需重新安排图文顺序，避免标题过大造成拥挤。", "#f2eee7 · #1e1d1b · #c6a886", editorial),
    ("10-pixel-retro", "像素风 / 复古游戏风", "Pixel / Retro", "像素块、等宽字、有限色盘和游戏界面元素带来复古趣味。", "小游戏、实验作品、趣味工具", "正文不要全部使用低分辨率字体；让游戏元素服务于实际操作。", "#141c2e · #ffe36e · #fe8b99", pixel),
    ("11-cyber-neon", "赛博霓虹风", "Cyber / Neon", "深色背景、荧光色、发光元素和科技感线条。", "游戏、音乐、科技主题展示", "发光效果使用过多会伤害可读性；确保文字与背景有充分对比。", "#080c1c · #54f1df · #fd5ed7", cyber),
    ("12-illustrative", "插画手绘风", "Illustrative / Hand-drawn", "手绘角色、有机图形和温暖配色营造亲近、轻松的氛围。", "教育、生活方式、儿童产品", "插画应有统一的笔触与色盘，不要挡住关键操作。", "#fff8ed · #8dc8a0 · #fa9c77", illustration),
    ("13-cartoon-2d", "2D 卡通风", "2D Cartoon", "平面角色、清楚的轮廓线、纯色填充和轻快的互动气氛。", "儿童产品、休闲游戏、教学工具", "角色和控件保持一致的线宽与色盘，避免装饰影响导航。", "#d8f3f4 · #8bd1b5 · #f2765b", cartoon_2d),
    ("14-maximalist", "华丽极繁主义 / 哥特装饰", "Ornate Maximalism", "以中世纪哥特教堂为灵感：尖拱、玫瑰窗、花饰细线、宝石色与金色层层叠加，强调精致工艺和仪式感。", "艺术展览、奇幻叙事、珠宝与高端文化品牌", "华丽来自细节与秩序；让装饰围绕主视觉与文字展开，正文仍需清晰。此例借鉴教堂建筑装饰，不代表所有极繁主义。", "#4b1831 · #162c53 · #d9b770", maximalist),
    ("15-medieval", "中世纪手抄本风", "Medieval Manuscript", "羊皮纸底色、装饰边框、衬线字与手抄本式插图。这里展示的是欧洲手抄本方向。", "历史内容、奇幻游戏、博物馆专题", "中世纪跨越多个地区与传统；具体项目应先确定时代和地域。", "#efe3c8 · #7e302d · #b88a43", medieval),
    ("16-sacred-art", "宗教艺术启发 / 彩窗", "Sacred Art / Stained Glass", "以宁静的留白、光线与彩窗结构表达神圣空间感；示例具体采用基督教哥特彩窗语汇。", "展览、历史文化内容、相关社群项目", "宗教传统各不相同，实际使用时应明确对象并核对符号含义。", "#14243d · #d3a35f · #9f6b7a", sacred),
    ("17-silk-road-dunhuang", "西域 / 敦煌艺术启发", "Silk Road / Dunhuang", "借鉴敦煌装饰的青绿、赭红、金色及莲花、卷草等纹样，形成壁画与丝路气质。", "文化展览、历史教育、旅游专题", "“西域”涵盖广阔地区，不能用一套图案概括；此图只聚焦敦煌启发。", "#255b61 · #b25344 · #dfad63", silk_road),
    ("18-islamic-geometric", "伊斯兰艺术启发 / 几何纹样", "Islamic Geometric", "重复的几何纹样、对称节奏、植物纹与书法传统；示例只采用抽象几何。", "文化展览、工艺档案、建筑专题", "“穆斯林风格”并非单一风格；涉及经文或书法时须确保文字准确且使用得体。", "#092f3d · #caa96a · #b15f3d", islamic),
    ("19-chinese-contemporary", "中国现代设计风", "Chinese Contemporary", "现代网格与中文排版结合克制的中国红、留白和抽象几何。", "中国品牌、文化科技、现代产品", "不要把中国风简化为红金龙凤；先确定品牌与受众。", "#f7f5f0 · #d94236 · #252d2c", chinese_modern),
    ("20-postmodern", "后现代风", "Postmodern / Memphis-inspired", "不对称构图、几何拼贴、鲜明配色和风格混搭，带有戏谑感。", "创意工作室、时尚、艺术活动", "后现代不是任意堆叠；文字、导航和操作仍需清晰。", "#f6c848 · #e25975 · #48bfc0", postmodern),
    ("21-ink-wash", "中国水墨风", "Chinese Ink Wash", "墨色层次、山水意象、纸色留白和小面积朱印。", "文化、阅读、茶艺、艺术展览", "留白与笔墨节奏比贴一张山水背景更关键；避免压低正文对比度。", "#f4f0e7 · #444d49 · #b7483b", ink_wash),
]


SOURCES = {
    "14-maximalist": ("V&A：哥特风格中的彩窗与装饰", "https://www.vam.ac.uk/articles/the-gothic-style-an-introduction"),
    "15-medieval": ("Getty：中世纪手抄本", "https://www.getty.edu/art/exhibitions/scriptorium/"),
    "16-sacred-art": ("大都会艺术博物馆：宗教图像的跨文化差异", "https://www.metmuseum.org/de/perspectives/virgin-mary-guanyin"),
    "17-silk-road-dunhuang": ("敦煌研究院：莫高窟装饰图案", "https://www.dha.ac.cn/info/1425/3618.htm"),
    "18-islamic-geometric": ("大都会艺术博物馆：伊斯兰艺术几何纹样", "https://www.metmuseum.org/es/essays/geometric-patterns-in-islamic-art"),
    "20-postmodern": ("V&A：什么是后现代主义", "https://www.vam.ac.uk/articles/what-is-postmodernism"),
    "21-ink-wash": ("大都会艺术博物馆：中国山水画", "https://www.metmuseum.org/exhibitions/listings/2017/streams-and-mountains"),
}


def main():
    rows = []
    cards = []
    for slug, name, english, feature, use, note, palette, render in STYLES:
        folder = ROOT / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "preview.svg").write_text(render(), encoding="utf-8")
        source = SOURCES.get(slug)
        source_note = f"\n## 进一步参考\n\n- [{source[0]}]({source[1]})\n" if source else ""
        readme = f"""# {name} · {english}

![{name}示例](preview.svg)

## 视觉特征

{feature}

## 常见用途

{use}。

## 示例配色

`{palette}`

## 使用时留意

{note}

{source_note}
> 图片是原创的示意界面，用于表达风格，不代表任何现成产品的完整设计规范。
"""
        (folder / "README.md").write_text(readme, encoding="utf-8")
        rows.append(f"| [{name}]({slug}/README.md) | {feature} | {use} |")
        category = "文化与历史" if int(slug[:2]) >= 15 and slug != "20-postmodern" else "视觉与交互"
        aliases = "穆斯林风格" if slug == "18-islamic-geometric" else "像素风 2D 游戏风" if slug == "10-pixel-retro" else ""
        cards.append(f'<a class="card" data-category="{category}" data-keywords="{aliases}" href="{slug}/README.md"><img src="{slug}/preview.svg" alt="{escape(name)}示例图"><span class="label">{escape(name)} <small>{escape(english)}</small></span><p>{escape(feature)}</p></a>')

    index = """# 前端视觉风格图库

每个子文件夹含一份中文说明和一张可直接用浏览器打开的 SVG 示意图。SVG 是可缩放的图片，也可用文本编辑器修改。打开 [可视化总览](gallery.html) 可搜索和浏览所有风格。原有像素风在 [10-pixel-retro](10-pixel-retro/README.md)。下面的分类同时包括整体视觉风格与局部效果，实际项目可组合使用。

| 风格 | 识别特征 | 适用场景 |
| --- | --- | --- |
""" + "\n".join(rows) + """

## 选型示例：颜色本身是主角

这组提示来自颜色选择玩具（RGB selection toy），也适用于同类「要让颜色被看见」的产品：

- **突出颜色本身**：从极简主义或扁平化开始，减少其他视觉元素。
- **强调玩具感**：试试复古像素风或插画手绘风。
- **强调发光效果**：试试赛博霓虹风。

## 参考资料

- [Google Material Design 3](https://m3.material.io/)
- [Microsoft Fluent 2](https://fluent2.microsoft.design/)
- [IBM Carbon Design System](https://carbondesignsystem.com/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Figma：网页设计趋势与风格](https://www.figma.com/resource-library/web-design-trends/)
- [Webflow：玻璃拟态](https://webflow.com/blog/glassmorphism)
- [Webflow：粗野主义网页设计](https://webflow.com/blog/10-brutalist-websites)
- [Getty：中世纪手抄本](https://www.getty.edu/art/exhibitions/scriptorium/)
- [敦煌研究院：莫高窟图案](https://www.dha.ac.cn/info/1425/3618.htm)
- [大都会艺术博物馆：伊斯兰艺术几何纹样](https://www.metmuseum.org/es/essays/geometric-patterns-in-islamic-art)
- [V&A：后现代主义](https://www.vam.ac.uk/articles/what-is-postmodernism)
- [大都会艺术博物馆：中国山水画](https://www.metmuseum.org/exhibitions/listings/2017/streams-and-mountains)

运行 `python generate_gallery.py` 可以重新生成全部说明与 SVG 预览。预览是原创示意，不是上述设计系统的官方组件截图。
"""
    (ROOT / "README.md").write_text(index, encoding="utf-8")
    gallery = """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>前端视觉风格图库</title><style>
*{box-sizing:border-box}body{margin:0;background:#f5f5f2;color:#242824;font:16px/1.55 system-ui,'Microsoft YaHei',sans-serif}
main{max-width:1320px;margin:auto;padding:42px 24px 70px}h1{font-size:clamp(28px,4vw,48px);margin:0 0 8px}header p{color:#59645e;margin:0 0 32px}
.filters{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 24px}.filters input{min-width:220px;flex:1;padding:12px 16px;border:1px solid #cdd5ce;border-radius:10px;font:inherit}.filters button{border:1px solid #cdd5ce;background:#fff;border-radius:10px;padding:9px 16px;font:inherit;cursor:pointer}.filters button.active{background:#263b32;color:#fff}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:22px}.card{display:block;background:white;color:inherit;text-decoration:none;border:1px solid #e4e7e2;border-radius:16px;overflow:hidden;transition:transform .2s,box-shadow .2s}.card[hidden]{display:none}
.card:hover,.card:focus-visible{transform:translateY(-4px);box-shadow:0 14px 35px #2233221a;outline:none}.card img{display:block;width:100%;aspect-ratio:12/7;object-fit:cover;background:#e8ecea}.label{display:block;font-weight:700;font-size:20px;margin:16px 18px 0}.label small{display:block;font-size:13px;font-weight:400;color:#788179}.card p{font-size:14px;color:#5d665f;margin:10px 18px 22px;min-height:44px}
</style></head><body><main><header><h1>前端视觉风格图库</h1><p>21 种风格 · 包含像素风、2D 卡通、极繁和文化艺术方向</p></header><div class="filters"><input id="search" type="search" placeholder="搜索风格，例如：像素、水墨、宗教" aria-label="搜索风格"><button class="active" data-filter="全部">全部</button><button data-filter="视觉与交互">视觉与交互</button><button data-filter="文化与历史">文化与历史</button></div><div class="grid">""" + "\n".join(cards) + """</div></main><script>
const input=document.querySelector('#search'),buttons=[...document.querySelectorAll('[data-filter]')],cards=[...document.querySelectorAll('.card')];let current='全部';
function update(){const q=input.value.trim().toLocaleLowerCase();for(const card of cards)card.hidden=(current!=='全部'&&card.dataset.category!==current)||!(card.textContent+' '+card.dataset.keywords).toLocaleLowerCase().includes(q)}
input.addEventListener('input',update);for(const button of buttons)button.addEventListener('click',()=>{current=button.dataset.filter;for(const b of buttons)b.classList.toggle('active',b===button);update()});
</script></body></html>
"""
    (ROOT / "gallery.html").write_text(gallery, encoding="utf-8")


if __name__ == "__main__":
    main()
