# ppt-master skill

本仓库通过 `.claude/settings.json` 注册了 [ppt-master](https://github.com/hugohe3/ppt-master)
插件市场（MIT，v6.2.0），并在项目作用域启用 `ppt-master@ppt-master`。
skill 本体（约 116MB / 1.2 万个文件，主要是 SVG 图标与音效素材）不入库，
由 Claude Code 自行拉取和更新。

## 首次使用需要做的三件事

1. **信任本目录** —— 首次在此目录启动 Claude Code 时接受 trust 提示，
   `extraKnownMarketplaces` 才会生效。

2. **安装插件**。项目 settings 只负责“启用”，来自外部 GitHub 源的插件不会自动下载，
   需要显式安装一次：

   ```
   /plugin install ppt-master@ppt-master
   ```

   或在 shell 里：

   ```
   claude plugin install ppt-master@ppt-master --scope project
   ```

   装完如果提示 `Run /reload-plugins to activate.`，执行 `/reload-plugins` 即可。

3. **装 Python 依赖**。后处理脚本（SVG → 原生 PPTX、图表、旁白音频）需要：

   ```sh
   # 插件装在 ~/.claude/plugins/cache/ 下，先定位 requirements.txt
   find ~/.claude/plugins/cache -path '*ppt-master*/requirements.txt' -maxdepth 5
   pip install -r <上面找到的路径>
   ```

   主要依赖：`python-pptx`、`PyMuPDF`、`skia-pathops`、`uharfbuzz`、`edge-tts`、
   `mammoth`、`Pillow`、`numpy`。

## 用法

装好后直接用自然语言触发，不需要记命令：

```
用 ./sources/report.pdf 生成一份 PPT
把这份 pptx 美化一下
```

skill 支持 PDF / DOCX / URL / Markdown / 图片作为输入，产出带真实 DrawingML
形状、文本框、图表和动画的可编辑 .pptx。

## 可选：AI 配图

`references/image-*` 相关能力需要图像模型的 API key，通过插件目录下的 `.env`
配置（参考同目录 `.env.example`），支持 OpenAI / Gemini / MiniMax / Qwen 等后端。
不配置也能正常生成 PPT，只是不会有 AI 生成的插图。

## 升级 / 卸载

```
/plugin marketplace update ppt-master     # 刷新市场目录
/plugin uninstall ppt-master@ppt-master   # 卸载
```

卸载后记得一并删掉 `.claude/settings.json` 里的两处 `ppt-master` 配置。
