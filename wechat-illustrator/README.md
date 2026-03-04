# WeChat Article Illustrator (微信公众号插画师)

这是一个专为内容创作者设计的 AI Skill，能够将文章内容自动转化为**极简手绘风格 (Hand-drawn Doodle Style)** 的视觉创意，并一键生成高质量配图。

## ✨ 核心功能

*   **智能分析**：自动提炼文章的核心痛点、情绪爆点。
*   **视觉隐喻**：将抽象概念（如“内卷”、“架构演进”）转化为幽默、具象的画面（如“被压扁的弹簧”、“摇摇欲坠的积木塔”）。
*   **金句提取**：从文章中提取简短有力的金句，并尝试融入画面中。
*   **一键出图**：集成 **Alibaba Qwen-Image-2.0** 模型，直接生成高质量插图。

## 🎨 风格展示

生成的图片采用极简线条、黑白为主（辅以少量高亮色）、火柴人风格，非常适合作为技术博客、公众号文章的封面或插图。

## 🚀 快速开始

### 1. 安装 Skill

```bash
npx skills add <your-username>/wechat-illustrator
```

### 2. 配置 API Key

本 Skill 依赖阿里云 DashScope 服务（Qwen-Image-2.0 模型）。你需要获取一个 API Key 并配置环境变量：

```bash
export DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

### 3. 使用方法

在支持 Skill 的 AI 助手（如 Trae, Cursor 等）中，直接发送你的文章内容或链接，并说：

> "帮我给这篇文章配图"
> "生成一张关于程序员加班的封面图"

## 🛠️ 本地开发

如果你想修改或扩展这个 Skill：

1.  克隆仓库：
    ```bash
    git clone https://github.com/<your-username>/wechat-illustrator.git
    ```
2.  安装依赖：
    ```bash
    pip install -r requirements.txt
    ```
3.  测试脚本：
    ```bash
    python src/generate_image.py --prompt "test prompt" --output-dir "output"
    ```

## 📄 License

MIT License
