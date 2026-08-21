# Academic Figures Drawer

Academic Figures Drawer turns a paper, method description, codebase, or visual reference into a clear, editable, camera-ready academic figure. It is designed for ML/AI papers in venues such as ICML, NeurIPS, and ICLR.

Academic Figures Drawer 可将论文、方法描述、代码库或视觉参考图转换为清晰、可编辑、适合论文发表的学术图。它面向 ICML、NeurIPS、ICLR 等机器学习与人工智能论文场景。

## What it produces / 输出内容

- Editable Draw.io source: `<figure>.drawio`
- Preview and export files: PNG, SVG, PDF, or a local HTML preview when requested
- A concise framework view showing `input → transformation → contribution → output`
- An optional module-detail view showing operation order, tensor shapes, attention directions, or feature interactions
- Evidence files such as `brief.md`, `visual-spec.md`, `layout-grid.md`, `asset-ledger.md`, and `defect-log.md` for non-trivial figures

- 可编辑的 Draw.io 源文件：`<figure>.drawio`
- PNG、SVG、PDF 导出文件，或按需生成的本地 HTML 预览
- 用于说明“输入 → 变换 → 核心创新 → 输出”的整体框架图
- 可选的模块细节图，用于说明操作顺序、张量维度、注意力方向或特征交互
- 对复杂图形生成 `brief.md`、`visual-spec.md`、`layout-grid.md`、`asset-ledger.md` 和 `defect-log.md` 等过程记录

The `.drawio` file is the source of truth. Raster images are used only for an explicitly requested real-world input or context asset; model computation is redrawn with editable vector primitives.

`.drawio` 文件是唯一的可编辑源文件。真实物体或应用场景图片只应出现在明确需要的输入/上下文区域；模型计算过程应使用可编辑的矢量图形重新绘制。

## Installation / 安装

Copy the `academic-figures-drawer` directory into a directory scanned by Codex skills. For a personal installation, the usual location is:

将 `academic-figures-drawer` 目录复制到 Codex 会扫描的 skill 目录。个人安装通常放在：

```text
~/.codex/skills/academic-figures-drawer/
```

The package can also be used directly from its current path:

也可以直接从当前路径使用：

```text
C:\Code\DrawioSkill\academic-figures-drawer\
```

After installation, invoke it with:

安装后使用以下方式触发：

```text
$academic-figures-drawer
```

## Quick start / 快速开始

Give the skill the scientific source and the desired figure type. Include a reference image when its style or composition should be followed.

向 skill 提供论文内容或方法描述，并说明希望生成的图形类型。如果需要参考某张图的风格或构图，同时提供参考图片。

### English prompt

```text
Use $academic-figures-drawer to create an editable, camera-ready figure for this method.

Figure type: framework overview plus one module-detail panel.
Input: multichannel time-series signal.
Core contribution: an adaptive cross-channel interaction block.
Output: prediction head and final task output.
Requirements: landscape layout, readable at two-column width, muted semantic colors,
one restrained accent color for the contribution, tensor shapes where informative,
and a PNG preview next to the .drawio source.
```

### 中文提示词

```text
使用 $academic-figures-drawer 为下面的方法生成可编辑、适合论文发表的结构图。

图形类型：整体框架图 + 一个核心模块细节图。
输入：多通道时间序列信号。
核心创新：自适应跨通道交互模块。
输出：预测头和最终任务输出。
要求：横向布局，缩小到论文双栏宽度后仍清晰；使用低饱和度语义配色；
用一个克制的强调色突出原创模块；只在有助于理解的位置标注张量维度；
并在 .drawio 源文件旁生成 PNG 预览。
```

## Recommended workflow / 推荐工作流

### 1. Extract the semantic graph / 提取语义图

First identify the real input, essential preprocessing, named stages, paper contribution, output, and any training-only branches. Do not add layers, dimensions, losses, or metrics that are not supported by the source.

先确认真实输入、必要预处理、主要阶段、论文创新、最终输出，以及仅训练阶段存在的分支。不要凭空补充论文没有提供的层、维度、损失或指标。

### 2. Build a visual contract / 建立视觉规范

Use a supplied figure as a style reference only after extracting its font hierarchy, palette, spacing rhythm, corner radius, stroke width, arrow grammar, and panel composition. Without a reference, use the default contract in `references/figure-contract.md` and `references/topconf-paper-style.md`.

如果提供了参考图，应先提取字体层级、配色、间距节奏、圆角、线宽、箭头语法和面板构成，再开始绘图。没有参考图时，使用 `references/figure-contract.md` 和 `references/topconf-paper-style.md` 中的默认规范。

### 3. Optional ImageGen concept pass / 可选的 ImageGen 草图阶段

For difficult compositions or real-world input context, generate a clean concept image first (for example with image-2). Ask for a wide academic composition with no scientific text, equations, or tiny unlabeled blocks. Treat the image as a composition and visual-language reference; then redraw the semantic content as Draw.io vectors.

对于复杂构图或真实输入场景，可以先用图像生成模型（例如 image-2）生成草图。提示词应要求宽幅学术构图、无科学文字、无公式、无微小无标签模块。草图只用于参考构图和视觉语言，最终语义内容要重新用 Draw.io 矢量图绘制。

### 4. Author the editable diagram / 绘制可编辑图

Use a concise framework view for the global story. Add a separate module view only when the internal mechanism matters. Show tensor shapes, Q/K/V, residual paths, or interaction axes only where they answer a reader question.

整体框架图只展示关键阶段和模块关系。只有在内部机制确实重要时才增加模块细节图。张量维度、Q/K/V、残差路径或交互轴只在能够回答读者问题的位置出现。

Use the semantic palette consistently:

统一使用具有固定含义的语义配色：

| Meaning / 含义 | Fill / 填充 | Stroke / 描边 |
|---|---|---|
| Input or raw signal / 输入或原始信号 | `#E8F2F5` | `#58727D` |
| Existing component / 已有组件 | `#EAF0F6` | `#63758A` |
| Feature or tensor transform / 特征或张量变换 | `#EDE9F4` | `#7B6A9A` |
| Training/task head / 训练或任务头 | `#F4EEDC` | `#9A7B3F` |
| Paper contribution / 论文创新 | `#F1D7D4` | `#B44948` |
| Output or decision / 输出或决策 | `#E5F1E3` | `#5A8A55` |

### 5. Validate and refine / 校验与精修

Run both validators before handoff:

交付前运行两个校验脚本：

```powershell
python <skill-dir>\scripts\validate_visual_quality.py <figure>.drawio
python <skill-dir>\scripts\validate_drawio.py <figure>.drawio
```

Then inspect a canvas-only screenshot at the intended paper width. Confirm that panel titles are dominant, the contribution block is not smaller than standard helper modules, and the smallest required label remains readable. Fix overflow, crossings, orphan labels, uneven spacing, and excessive text before reducing font size.

For the complete reusable review contract—including compact-canvas rules, rendered LaTeX checks, explicit arrow source/target semantics, transparent real-object asset boundaries, and the three-cycle export review—see [`references/general-quality-contract.md`](references/general-quality-contract.md).

随后在论文目标尺寸下检查只包含画布的截图。确认面板标题最醒目，原创模块的面积不小于普通辅助模块，最小的必要文字仍然可读。优先修复溢出、连线穿模、孤立标签、间距不均和文字冗余，不要先通过缩小字号解决拥挤。

For a local browser preview:

生成本地浏览器预览：

```powershell
python <skill-dir>\scripts\serve_drawio_preview.py <figure>.drawio --port 8765
```

For a reusable evidence workspace:

创建可复用的图形证据工作区：

```powershell
python <skill-dir>\scripts\init_figure_workspace.py <work-dir> --title "Your Figure Title"
```

## Choosing a figure type / 图形类型选择

| Type / 类型 | Use when / 适用场景 | Typical content / 典型内容 |
|---|---|---|
| Framework overview / 整体框架图 | The reader needs the global story first / 读者首先需要理解总体逻辑 | 5–8 stages, main data flow, contribution location, final output |
| Module detail / 模块细节图 | The novelty depends on internal mechanics / 创新点依赖内部机制 | Operation order, tensor shapes, Q/K/V, feature-interaction direction |
| Multi-panel figure / 多面板图 | One canvas would become crowded / 单一画布会过于拥挤 | (a) overview, (b) proposed module, optional training or downstream panel |
| Reference replication / 参考图复刻 | Style and layout must follow a supplied figure / 需要沿用给定参考图的风格和构图 | Extracted style contract plus a vector redraw |

## Package structure / 目录结构

```text
academic-figures-drawer/
├── SKILL.md                         # Core agent instructions / 核心 skill 指令
├── README.md                        # This guide / 本使用说明
├── agents/openai.yaml               # UI metadata / 界面元数据
├── references/                      # Style, XML, and review guidance / 规范与校验文档
├── scripts/                         # Preview, validation, layout utilities / 工具脚本
└── data/                            # Local shape and icon indexes / 本地形状与图标索引
```

## Design principles / 设计原则

- Clarity before decoration. / 清晰度优先于装饰。
- Show the contribution with one restrained accent color. / 用一个克制的强调色突出论文创新。
- Keep real images in input/context regions. / 将真实图片限制在输入或上下文区域。
- Use vectors for model computation. / 模型计算过程使用矢量图形表达。
- Preserve scientific semantics; never invent missing facts. / 保留科学语义，不虚构缺失事实。
- Optimize for two-column readability, not editor zoom. / 以论文双栏尺寸的可读性为最终标准，而不是编辑器缩放效果。
- Fit the canvas to the composition and remove redundant whitespace. / 让画布贴合实际构图，删除冗余留白。
- Make every connector and symbol semantically explicit. / 确保每条连线和每个符号的语义都明确。
- Review exported artifacts iteratively, not only the editable canvas. / 反复检查导出物，而不只检查可编辑画布。
