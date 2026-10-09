# -*- coding: utf-8 -*-
"""Performance options chunk 3: VBO, Input, Low-latency, UI, Map, Lua, Cores, Audio, GC, Updates."""

PERF3_ZH = {
    "persistentVboFrameSync": {
        "label": "持久化 VBO：显卡帧同步围栏",
        "tip": "在每一帧持久化映射顶点缓冲区写入完成时插入 OpenGL 同步围栏（Sync Fence），确保 GPU 消费前 CPU 不会覆写环形缓冲。"
    },
    "persistentVboSlots": {
        "label": "持久化 VBO：环形缓冲存储槽位数量",
        "tip": "持久化映射缓冲区内部划分的槽位数（默认 3 槽），允许多达数帧的图元数据互不干扰地流式上传到显存中。"
    },
    "vboBatchKb": {
        "label": "顶点缓冲区合批提交大小上限 (KB)",
        "tip": "几何线段与粒子图元合批缓冲区的最大字节数。调大可减少图元批次提交次数，降低驱动层 CPU 负担。"
    },
    "vboFastQuads": {
        "label": "快速矩形图元四边形流式装配",
        "tip": "针对雨滴、雪花、光晕等标准四边形图元使用预置索引快速装配，消除原版每绘制一个粒子就要计算四个顶点索引的开销。"
    },
    "keyboardFresh": {
        "label": "当帧即时采集键盘按键状态",
        "tip": "在当前渲染帧开始时即时读取并锁存真实的物理键盘状态，彻底根除原版游戏落后一帧的键盘轮询延迟。"
    },
    "reflexCapFps": {
        "label": "超低延迟模式专用微幅限帧",
        "tip": "将最大帧率限制在显示器刷新率稍低处（如 144Hz 限制在 141fps），防止显卡预渲染队列积压，保持输入延迟处于最低极限。"
    },
    "vblankLock": {
        "label": "垂直消隐信号硬锁 (VBlank Lock)",
        "tip": "在垂直消隐信号到来前的固定微秒精准启动下一帧渲染，使操作输入与画面显示的端到端延迟达到物理最短。"
    },
    "gpuMaxFrames": {
        "label": "显卡驱动预渲染帧队列深度上限",
        "tip": "限制显卡驱动允许在后台排队的最大未呈现帧数（1 = 极致低延迟；2 = 略微容忍波动）。消除严重的按键跟手延迟。"
    },
    "frameStartGate": {
        "label": "帧起始排队等待空间门控",
        "tip": "在确认显卡渲染管线有空闲承接新帧之前，暂缓读取用户输入，确保按键采样点尽可能紧贴实际渲染时刻。"
    },
    "vsyncAdaptive": {
        "label": "自适应垂直同步 (Adaptive VSync)",
        "tip": "在帧率达到显示器刷新率时保持垂直同步以防撕裂；一旦帧率低于刷新率则立即临时解除同步，避免传统垂直同步暴跌至半帧（如 60 跌至 30）的严重顿挫。"
    },
    "cursorLatch": {
        "label": "硬件光标即时坐标更新",
        "tip": "在渲染帧开始时直接锁存操作系统最新的硬件鼠标绝对坐标绘制游戏内准星，消除鼠标指针的视觉拖尾与操作延迟。"
    },
    "aimHoldMs": {
        "label": "右键瞄准防抖缓冲时间 (ms)",
        "tip": "按下鼠标右键进入瞄准姿态前的微小防抖判定时长，防止快速点击移动时误触瞄准转向动作。"
    },
    "uiRetained": {
        "label": "保留模式 UI 渲染 (Retained UI)",
        "tip": "仅在界面内容发生改变的那一瞬间重绘变化的控件（如物品栏变动、血量变化），而非每帧全屏无脑重绘所有打开的窗口。"
    },
    "uiRetainedChildren": {
        "label": "子控件继承保留模式状态",
        "tip": "将窗口内的子按钮、滑动条和列表面板一并纳入保留模式缓存体系，在打开复杂物品栏时将主线程消耗从 12% 压制至 2% 以下。"
    },
    "uiTickStagger": {
        "label": "复杂 UI 逻辑定时器错峰打散",
        "tip": "将多个打开窗口的内部定时逻辑检查（如保鲜度刷新、耐久度计算）分散到不同的帧中错峰执行，避免周期性微卡顿。"
    },
    "uiLuaFast": {
        "label": "Lua UI 快速事件分发与边界加速",
        "tip": "优化 Lua 侧 UIElement 的鼠标移动悬停与边界求交算法，使得在物品栏中滑动浏览数百件物品时丝滑流畅。"
    },
    "hotsaveWarmup": {
        "label": "进世界预热存档数据传输管道",
        "tip": "在进入世界的读条阶段预先初始化并热身后台存档工作流，消除游戏开局前几分钟因初次热存档造成的突发掉帧。"
    },
    "mapStreetMemo": {
        "label": "世界地图街道图元单次解算布局",
        "tip": "在打开大地图时，将当前视口范围内的街道名称和路线图元一次性解算并缓存，平移地图时无需每帧重复几何排版。"
    },
    "mapStreetCache": {
        "label": "世界地图街道渲染纹理持久化缓存",
        "tip": "将大地图街道渲染结果持久化保存在后台纹理缓存中，只要视口缩放未变，完全跳过数千条道路名称的重绘。"
    },
    "mapVisitedFast": {
        "label": "大地图已探索迷雾快速位图标记",
        "tip": "采用高效的按行打包位图算法快速构建和渲染大地图上的已探索区域迷雾，消除每次按 M 键打开地图时的卡顿。"
    },
    "luaIndexCache": {
        "label": "Lua 全局索引与类名查找缓存",
        "tip": "缓存 Lua 脚本对 Java 类和全局元表的反射查找结果，大幅削减大量模组运行时反复调用 getField 的反射开销。"
    },
    "luaInternConstants": {
        "label": "Lua 常用常量字符内存驻留优化",
        "tip": "将 Lua 脚本中最常出现的属性名、状态名进行符号驻留（String Interning），把字符串比较加速为指针整数比较。"
    },
    "luaSkipEmpty": {
        "label": "Lua 空回调函数与无操作事件快速跳过",
        "tip": "当游戏或模组注册了空的 OnTick、OnRender 等钩子事件时，直接在底层跳过 JNI 调用，避免无效穿越 Java/Lua 边界。"
    },
    "modProfile": {
        "label": "模组兼容性策略模式",
        "tip": "performance = 最大性能模式（保留全部优化）；compatibility = 最大兼容模式（自动关闭与其他已安装 Java 模组冲突的补丁）。"
    },
    "modCompat": {
        "label": "模组冲突智能检测与协调",
        "tip": "在游戏启动时智能扫描已启用的 Java 模组，自动协调并应用针对已知模组的兼容性补丁。"
    },
    "uiRetainedMods": {
        "label": "模组自定义 UI 兼容模式",
        "tip": "允许第三方模组绘制的非原生 UI 窗口也能享受保留模式渲染带来的性能飞跃，且不破坏模组的正常显示。"
    },
    "luaWorkerGate": {
        "label": "多线程工作池安全隔离保护门",
        "tip": "确保工作线程在计算过程中若触发了非线程安全的 Lua 回调，安全调度回主线程执行，防止游戏闪退。"
    },
    "driveCameraLate": {
        "label": "行车镜头在车辆移动后计算定位",
        "tip": "将跟随镜头的计算放在车辆物理刚体位移完全结算之后执行，彻底消除行车时镜头与车身之间的视差拉扯与抖动。"
    },
    "driveLookSmooth": {
        "label": "行车视线平滑阻尼过渡",
        "tip": "对高速行车时镜头前探（Look-ahead）的位移进行平滑阻尼滤波，让高速过弯和加速时的视野平稳顺滑。"
    },
    "cameraScreenPixels": {
        "label": "近景缩放时镜头屏幕亚像素对齐",
        "tip": "在视口拉近至 100% 或更近时，将镜头坐标精准对齐到物理屏幕像素网格，消除行走时的微弱锯齿抖动。"
    },
    "frameClockSmooth": {
        "label": "游戏物理时钟基于显示器刷新率平滑滤波",
        "tip": "消除由于系统纳秒级计时器抖动导致的每帧 deltaTime 微小波动，使行车和角色位移与显示器刷新时钟完全同频。"
    },
    "physicsStepHz": {
        "label": "车辆物理引擎模拟频率 (Hz)",
        "tip": "车辆物理 Bullet 模拟的计算频率（原版为 100 Hz）。保持 100 Hz 可获得最平稳的操控与碰撞表现。"
    },
    "physicsStepMode": {
        "label": "车辆物理模拟每帧步长策略",
        "tip": "fixed = 固定时间步长；adaptive = 随实际帧率动态细分。有效解决掉帧严重时车辆弹跳飞天或穿模的物理引擎 Bug。"
    },
    "vrrCap": {
        "label": "将帧率限制在显示器 VRR 刷新窗口以内",
        "tip": "自动将最大帧率限制在当前显示器刷新率上限的 97%（如 144Hz 显示器限制在 140fps），防止超出 VRR 窗口导致突然撕裂。"
    },
    "borderlessFullscreen": {
        "label": "无边框窗口伪装独占全屏 (激活 VRR)",
        "tip": "向桌面合成器报告独占全屏标志，使 Windows DWM 或 Linux Wayland 在无边框窗口下能够完美激活 G-SYNC / FreeSync。"
    },
    "macGlCore": {
        "label": "macOS：强制开启 OpenGL 4.1 核心配置",
        "tip": "在苹果 macOS 系统上强制启用现代 OpenGL 4.1 Core Profile，以便支持画质增强中的着色器特性。"
    },
    "macGlTimerQueries": {
        "label": "macOS：启用 OpenGL 计时器查询",
        "tip": "在 macOS 上支持精确的 GPU 耗时测量，为性能监控覆盖层提供真实的显卡负载数据。"
    },
    "macPresent": {
        "label": "macOS：基于 Metal 底层的 ProMotion 自适应帧交换",
        "tip": "在苹果 Mac 设备上通过 Metal 表面提交帧，完美匹配 MacBook Pro 的 120Hz ProMotion 自适应高刷屏幕。"
    },
    "limiterSleep": {
        "label": "帧率限制器微秒级精准休眠",
        "tip": "使用高精度混合等待策略替代原版开销极大的忙等待死循环（Spin-lock），在限制帧率时大幅降低 CPU 占用与发热。"
    },
    "gpuPstate": {
        "label": "限制 GPU 电源状态 (防止突发降频卡顿)",
        "tip": "在 Linux 系统上锁定 AMD/NVIDIA 显卡的电源层级，防止显卡在游戏负载暂时减轻时过激降频导致的突发严重卡顿。"
    },
    "jitSteady": {
        "label": "Java JIT 编译器稳定优化层级",
        "tip": "在进入世界后指示 Java 虚拟机 JIT 编译器停止激进的推测性去优化（Deoptimization），消除突发的长时间微卡死。"
    },
    "lightingSyncPark": {
        "label": "光照同步线程低功耗自旋休眠",
        "tip": "在光照计算间隙使专有光照同步线程进入节能休眠，降低多核处理器的空载功耗与发热。"
    },
    "gcHeap": {
        "label": "Java 堆内存分配上限 (Heap Size)",
        "tip": "为游戏进程配置的 JVM 初始与最大堆内存大小。适当调大可有效延缓垃圾回收触发频率。"
    },
    "luaGcNoop": {
        "label": "忽略模组主动发起的全局垃圾回收请求",
        "tip": "彻底屏蔽部分模组在脚本中恶意调用 collectgarbage() 导致的游戏瞬间卡死停顿数秒的流氓行为。"
    },
    "gcHeapFixed": {
        "label": "启动时固定分配全部 JVM 堆内存",
        "tip": "将 -Xms 与 -Xmx 设为相同数值，避免 Java 虚拟机在运行过程中动态向操作系统申请/归还内存导致的频繁停顿。"
    },
    "gcPreTouch": {
        "label": "启动阶段预先触碰分配全部内存物理页",
        "tip": "在游戏启动时预先触碰所有堆内存页，将可能发生的操作系统内存缺页异常（Page Fault）完全移到游戏进入世界之前。"
    },
    "gcPauseMs": {
        "label": "G1 垃圾回收目标停顿时间上限 (ms)",
        "tip": "指示 G1GC 尽量将单次垃圾回收的 STW 停顿时间控制在该毫秒数值以内，避免肉眼可见的卡死。"
    },
    "audioLimiterCeilingDb": {
        "label": "音频限幅器最大输出电平天花板 (dB)",
        "tip": "音频信号通过限幅器时的硬上限（默认 -0.5 dB），彻底留出安全裕量，防止在声卡 DAC 转换时产生数码破音。"
    },
    "soundTickHz": {
        "label": "FMOD 音频系统心跳更新频率 (Hz)",
        "tip": "游戏向底层 FMOD 音频引擎提交状态更新的频率。60 Hz 即可保持声音空间定位绝对平滑。"
    },
    "emitterIdleSkip": {
        "label": "静止无声发生器跳过每帧计算",
        "tip": "跳过对周围数百个无声或静止的 3D 声音发射器的多余空间矩阵更新，减轻音效密集场景下的 CPU 负担。"
    },
    "worldSoundCleanupFast": {
        "label": "过期世界声音实例快速回收",
        "tip": "使用环形队列快速回收已经衰减完毕的过期世界声音对象，避免列表频繁挪动开销。"
    },
    "hearingHoist": {
        "label": "僵尸听觉感知计算外提循环优化",
        "tip": "将僵尸听力范围与阻挡因子的公用不变参数外提至内层循环之外，大幅加速僵尸听觉索敌性能。"
    },
    "luaChecksumExempt": {
        "label": "将优化专用 Lua 文件排除在服务器校验之外",
        "tip": "防止部分严格校验客户端 Lua 哈希的联机多人服务器因 PZ Optimization 的客户端优化脚本而误报拒绝加入。"
    },
    "updateCheck": {
        "label": "在主菜单展示新版本可用更新",
        "tip": "当 GitHub 或创意工坊发布适合当前游戏版本的新优化版本时，在游戏主菜单展示更新提示。"
    },
    "updatePrefetch": {
        "label": "后台预先拉取新版本更新说明",
        "tip": "在检测到可用更新时，后台预先下载更新日志与变更说明，以便在点击更新弹窗时即刻秒开。"
    },
    "updateFromWorkshop": {
        "label": "优先从 Steam 创意工坊同步更新",
        "tip": "直接从本模组在 Steam 创意工坊本地下载的最新文件中复制安装，无需通过网络重新下载 release zip。"
    },
}
