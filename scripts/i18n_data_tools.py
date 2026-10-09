# -*- coding: utf-8 -*-
"""Tools and Profiler options: Overlay, Sampling, Graph, Flame chart, FPS Colors, Console."""

TOOLS_ZH = {
    "overlaySampling": {
        "label": "性能数据动态采样开关 (F9 覆盖层依赖项)",
        "tip": "开启后后台才会采集帧时间与硬件利用率。关闭 = 彻底停止任何性能监控开销，按 F9 键会提示需开启此项。"
    },
    "overlay": {
        "label": "游戏启动时默认显示性能覆盖层",
        "tip": "每次启动进入游戏后自动开启屏幕下方的性能监控覆盖层，无需手动按快捷键 F9。"
    },
    "overlayLog": {
        "label": "将每一帧耗时与卡顿事件写入日志文件",
        "tip": "在 Zomboid/pzopt/frame-log.csv 中记录每一帧的呈现耗时、CPU/GPU 占用与卡顿元凶，供性能分析。"
    },
    "overlayStats": {
        "label": "监控层显示硬件详细负载统计信息",
        "tip": "在屏幕上实时查看帧率、1% Low 最低帧、CPU 主频、GPU 占用率、显存使用量与 JVM 堆内存变化。"
    },
    "overlayPower": {
        "label": "监控层显示 CPU 与 GPU 实时预估功耗",
        "tip": "在屏幕监控层展示当前处理器与独立显卡的实时功耗瓦数 (Watts)（Linux 与部分 Windows 硬件支持）。"
    },
    "overlayTree": {
        "label": "监控层显示游戏主线程子系统耗时层级树",
        "tip": "实时按百分比拆解游戏主线程消耗：动画占多少、光照占多少、Lua UI 占多少、物理引擎占多少，一目了然！"
    },
    "overlayVerdict": {
        "label": "监控层显示性能瓶颈智能诊断结论",
        "tip": "自动根据当前硬件指标输出智能诊断标签（如：CPU 瓶颈、GPU 限制、内存垃圾回收停顿、或垂直同步等待）。"
    },
    "overlayGraph": {
        "label": "在屏幕底部显示实时帧时间曲线波动图",
        "tip": "以毫米波形式绘制最近数百帧的帧时间平稳度曲线，任何一次轻微掉帧卡顿均无所遁形。"
    },
    "overlayGraphHz": {
        "label": "帧时间曲线图表重绘采样频率 (Hz)",
        "tip": "底部曲线图表的刷新频率。60 Hz 即可保持丝滑顺畅且不占用额外绘图开销。"
    },
    "overlayFlame": {
        "label": "显示游戏主线程实时微观火焰图 (Flame Graph)",
        "tip": "在屏幕上实时展开主线程调用栈火焰图，深度剖析毫秒级函数调用耗时。"
    },
    "overlayFlameDepth": {
        "label": "游戏主线程火焰图展开最大层深",
        "tip": "火焰图允许向下追踪展示的 Java / Native 函数调用栈最大层级数。"
    },
    "gameThreadProfileHz": {
        "label": "游戏主线程分析器栈采样频率 (Hz)",
        "tip": "主线程性能探针每秒抓取调用栈样本的次数（默认 200 Hz）。"
    },
    "overlayTexture": {
        "label": "监控层图表合批单纹理渲染",
        "tip": "将整个监控覆盖层的所有文字与图表整合为单张离屏纹理一次性绘制，绝不增加游戏主画面 Draw Call。"
    },
    "overlayRefreshMs": {
        "label": "监控层数值文本刷新间隔 (ms)",
        "tip": "屏幕上 FPS 和各项硬件数字的数值跳动刷新间隔（默认 100 ms）。防止数字疯狂抖动影响肉眼阅读。"
    },
    "overlayCorner": {
        "label": "性能覆盖层在屏幕上的停靠角落位置",
        "tip": "选择监控层停靠在屏幕的哪个边缘角落（bottom-left 左下角、bottom-right 右下角、top-right 右上角等）。"
    },
    "overlayFont": {
        "label": "性能覆盖层文字显示的字体字号",
        "tip": "选择小号、中号或大号字体，根据你的显示器分辨率与视距选择最舒服的大小。"
    },
    "overlayFpsColor": {
        "label": "FPS 字体颜色随帧率状态动态着色",
        "tip": "根据当前帧率的高低优劣自动变化文字颜色：满帧高刷显示为蓝色，稳定良好显示为绿色，轻微掉帧黄色，严重卡顿红色。"
    },
    "overlayFpsFollowCap": {
        "label": "动态着色阈值自动跟随设定的帧率上限",
        "tip": "动态着色阈值自动关联游戏设定的最大帧率。例如设定限帧 60 时，达到 60 即可呈现优异蓝色。"
    },
    "overlayFpsCapBluePct": {
        "label": "限帧模式下显示为蓝色的满帧比例阈值 (%)",
        "tip": "当前帧率达到设定限帧的该比例时（如 99%），着色为极致满帧蓝色。"
    },
    "overlayFpsCapGreenPct": {
        "label": "限帧模式下显示为绿色的良好帧率阈值 (%)",
        "tip": "当前帧率达到设定限帧的该比例时（如 90%），着色为健康绿色。"
    },
    "overlayFpsCapYellowPct": {
        "label": "限帧模式下显示为黄色的警告帧率阈值 (%)",
        "tip": "当前帧率跌落至此比例时，着色为黄色警告。"
    },
    "overlayFpsBlueAbove": {
        "label": "不锁帧模式下显示为蓝色的绝对帧率阈值 (FPS)",
        "tip": "当帧率无限制时，超过该具体数值即显示为优秀蓝色（如 140 FPS）。"
    },
    "overlayFpsGreenAbove": {
        "label": "不锁帧模式下显示为绿色的健康帧率阈值 (FPS)",
        "tip": "不锁帧模式下维持健康绿色的帧率下限（如 60 FPS）。"
    },
    "overlayFpsYellowAbove": {
        "label": "不锁帧模式下显示为黄色的警告帧率阈值 (FPS)",
        "tip": "不锁帧模式下跌入警告黄色的帧率分界点（如 30 FPS）。"
    },
    "overlayFpsColorBlue": {
        "label": "极佳档位 (Tier 1) 颜色定制",
        "tip": "最高优异表现时的字体颜色（默认蓝色，支持 green / yellow / cyan / #RRGGBB）。"
    },
    "overlayFpsColorGreen": {
        "label": "良好档位 (Tier 2) 颜色定制",
        "tip": "常规稳定表现时的字体颜色（默认绿色）。"
    },
    "overlayFpsColorYellow": {
        "label": "警告档位 (Tier 3) 颜色定制",
        "tip": "发生轻度掉帧波动时的字体颜色（默认黄色）。"
    },
    "overlayFpsColorRed": {
        "label": "严重掉帧档位 (Tier 4) 颜色定制",
        "tip": "跌破严重卡顿警戒线时的字体颜色（默认红色）。"
    },
    "consoleLog": {
        "label": "终端控制台无害警告日志智能静音过滤",
        "tip": "过滤 Project Zomboid 控制台中无害的频繁报错与垃圾日志刷屏（如缺失贴图、无害音频警告），减轻后台磁盘写入负荷。"
    },
}
