---
name: "wechat-illustrator"
description: "分析公众号文章并生成手绘/漫画风格的封面与插图。当用户提供文章内容或主题并请求配图建议或生成图片时调用。"
---

# 微信公众号插画师 (WeChat Article Illustrator)

这个技能专注于将微信公众号文章、技术博客的内容转化为**极简手绘/漫画风格**的视觉创意，并可以通过调用 Alibaba Qwen-Image-2.0 生成实际图片。

## 核心目标

1.  **提炼核心痛点**：快速识别文章的情绪爆点、技术难点或用户共鸣点。
2.  **金句提炼**：从文章中提取或总结出一句简短有力、富有哲理或幽默感的“金句”（不超过15个字），用于印在图片上。
3.  **视觉隐喻转化**：将抽象概念（如“内卷”、“架构演进”、“系统崩溃”）转化为具象、幽默的画面（如“被压扁的弹簧”、“摇摇欲坠的积木塔”、“着火的服务器”）。
4.  **生成图片**：利用 Qwen-Image-2.0 生成高质量的手绘风格插图，并尝试将金句融入画面。

## 视觉风格定义 (Hand-drawn Doodle Style)

*   **关键词**：`Hand-drawn`, `Doodle`, `Sketch`, `Stick figures`, `Minimalist`, `Technical Manga`, `Excalidraw style`, `xkcd style`.
*   **画面特征**：
    *   **线条**：不完美的、抖动的、手绘感强的黑线条 (Rough, sketchy lines)。
    *   **色彩**：以黑白为主，辅以 1-2 种高亮色（如 🔴 警示红, 🔵 科技蓝, 🟡 强调黄）用于突出重点。
    *   **元素**：火柴人/简笔画人物 (Stick figures with expressive faces)、对话气泡、箭头、流程图框、简单的图标。
    *   **构图**：留白多 (White background)，扁平化，无复杂背景。
    *   **氛围**：幽默、自嘲、夸张、直观。

## 指令流程

当用户提供文章内容后，请按以下步骤执行：

1.  **深度分析**：
    *   用一句话总结文章的核心痛点或主题。
    *   **提取金句**：为每张图片设计一句简短的中文文案（不超过10个字，最好5-8个字），例如“别想太多，干就完了！”。
    *   提取 3-5 个关键情节点或技术概念，并构思对应的视觉隐喻。

2.  **生成方案**：
    *   **设计理念**：必须直击痛点，具有强烈的点击欲望。
    *   **AI 提示词 (英文)**：`hand-drawn doodle style, minimalist sketch, [画面核心描述], text in the image written in Chinese characters: "[金句中文内容]", stick figures, white background, simple black lines, high contrast, [情绪关键词], --ar 16:9`。
    *   *注意：虽然AI生成中文文字能力有限，但在Prompt中明确要求有助于生成类似文字的形状或占位符，后期可PS修改，或者运气好直接生成准确文字。*

3.  **确认与生成 (关键步骤)**：
    *   向用户展示构思好的 Prompt。
    *   **询问用户**：“是否需要我为您生成这张图片？（需要提供 DashScope API Key）”
    *   如果用户同意并提供了 Key（或已在环境变量 `DASHSCOPE_API_KEY` 中设置），使用 `RunCommand` 调用生成脚本：
        ```bash
        pip install dashscope requests  # 确保依赖已安装
        python .trae/skills/wechat-illustrator/src/generate_image.py --prompt "YOUR_PROMPT_HERE" --output-dir "generated_images" --api-key "USER_API_KEY"
        ```
    *   执行完毕后，向用户展示生成的图片路径。

## 输出示例

### 封面建议：程序员的日常夹击
*   **设计理念**：展现程序员在多方压力下的无奈现状，引发共鸣。
*   **画面描述**：画面中央是一个无奈的程序员（火柴人风格），满头大汗，眼神空洞。左边是一个指手画脚的产品经理拿着需求文档（写着“改”字），右边是一个冒着黑烟的服务器（写着“BUG”）。背景有几个大大的箭头指向程序员，象征来自四面八方的压力。色彩只用黑白线条加上红色的“BUG”字样和蓝色的“眼泪”。
*   **Prompt**: `hand-drawn doodle style, minimalist sketch, a stressed stick figure programmer in the center, sweating profusely, surrounded by large black arrows pointing at him representing pressure, on the left a product manager stick figure holding a document saying "CHANGE", on the right a smoking server with "BUG" text, simple rough black lines on white background, red and blue accents, humorous and chaotic atmosphere, wide shot --ar 16:9`

### 插图建议 1：无尽的会议
*   **位置建议**：文章开头，描述现状。
*   **画面描述**：一个长桌子，围坐着一群火柴人，大家都在睡觉或玩手机，只有一个人在前面激情演讲。演讲者的对话气泡里全是乱码或“Blah Blah”。
*   **Prompt**: `hand-drawn doodle style, minimalist sketch, a long meeting table with stick figures sitting around, most stick figures are sleeping or looking at phones, one stick figure standing and presenting with speech bubble containing "Blah Blah", simple black lines on white background, boring atmosphere, humorous`
