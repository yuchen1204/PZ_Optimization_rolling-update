# -*- coding: utf-8 -*-
"""Visual Enhancements options: Upscaling, DynRes, SpriteFilter, HDR, AO, Shadows, Reflections, Glass, Outlines, Wet Blood, God Rays, Sway, Tone, Per-Pixel Light, Relief."""

VIS_ZH = {
    "upscalerQuality": {
        "label": "超分辨率画质档位 (渲染尺寸)",
        "tip": "quality = 轴向 67% (44% 像素)；balanced = 58%；performance = 50% (仅 25% 像素)；ultra = 33%；native = 100% (仅启用原生抗锯齿)。"
    },
    "upscalerScalePct": {
        "label": "超分辨率自定义分辨率缩放比例 (%)",
        "tip": "自定义输入渲染分辨率占屏幕目标分辨率的百分比。可精确微调以兼顾帧率与画质锐度。"
    },
    "fsrSharpnessPct": {
        "label": "AMD FSR 1.0 边缘锐化程度 (%)",
        "tip": "AMD FidelityFX Super Resolution 1.0 空间放大后的自适应边缘锐化强度。50% 即可获得极佳的清晰感。"
    },
    "dlssPreset": {
        "label": "NVIDIA DLSS 模型预设配置文件",
        "tip": "选择 NVIDIA 深度学习超采样（DLSS）的模型配置文件预设（Preset C / D / E / F 等），针对不同场景优化鬼影与细线边缘稳定性。"
    },
    "dlssOutputPct": {
        "label": "NVIDIA DLSS 目标输出分辨率比例 (%)",
        "tip": "DLSS 最终图像输出大小占当前窗口分辨率的百分比。"
    },
    "dlssOutputFilter": {
        "label": "NVIDIA DLSS 输出滤波抗锯齿处理",
        "tip": "DLSS 放大输出后的次级后处理滤波模式，改善像素边缘在高对比度下的平滑表现。"
    },
    "dlssSharpen": {
        "label": "NVIDIA DLSS 官方自适应锐化",
        "tip": "通过 DLSS NVSDK 内部集成的高性能锐化滤镜增强物体轮廓细节。"
    },
    "upscalerObjectMv": {
        "label": "超分辨率：角色与车辆动态运动矢量",
        "tip": "为运动中的人物、僵尸与车辆生成高精度屏幕空间运动矢量（Motion Vectors），彻底消除时间序列超分（DLSS/TAAU）中的拖影与重影。"
    },
    "dlssWaterCurrent": {
        "label": "NVIDIA DLSS 水流表面实时动态矢量补偿",
        "tip": "在 DLSS 渲染时将水流表面的流动方向注入运动矢量通道，确保奔流河水与湖泊倒影依然锐利不模糊。"
    },
    "dlssWaterHistoryPct": {
        "label": "NVIDIA DLSS 水体历史帧时间平滑权重 (%)",
        "tip": "控制水面波纹倒影在时间维度上混合上一帧结果的比率，有效抑制水面高频闪烁噪点。"
    },
    "dynRes": {
        "label": "动态分辨率缩放 (Dynamic Resolution)",
        "tip": "根据实时显卡负载和当前帧率，自动在设定的范围内动态无级缩放渲染分辨率，在激战尸潮和暴风雨中死死咬住目标帧率。"
    },
    "dynResUpscaler": {
        "label": "动态分辨率配套放大算法",
        "tip": "当未开启常驻超分时，动态分辨率所使用的配套后处理放大重建算法（如快速双线性插值或 Lanczos 锐化）。"
    },
    "dynResTargetPct": {
        "label": "动态分辨率基准目标渲染比例 (%)",
        "tip": "系统无负载压力时默认维持的标准渲染分辨率百分比。"
    },
    "dynResMinPct": {
        "label": "动态分辨率允许下调的最低渲染比例 (%)",
        "tip": "在极端掉帧时允许自动降低到的最低渲染分辨率比例（如 50%），设置防线防止画质过度模糊。"
    },
    "dynResMaxPct": {
        "label": "动态分辨率允许上调的最高渲染比例 (%)",
        "tip": "当显卡算力极其充裕时允许自动超分辨率渲染的最高上限。"
    },
    "dynResFps": {
        "label": "动态分辨率维持的目标帧率 (FPS)",
        "tip": "动态分辨率调节算法竭力维持的目标基准帧率（如 60 或 120 FPS）。"
    },
    "dynResController": {
        "label": "动态分辨率 PID 控制器响应速度",
        "tip": "控制分辨率根据帧耗时调整的平滑阻尼速度，避免分辨率在几帧之内大幅忽高忽低频繁跳变。"
    },
    "spriteFilter": {
        "label": "2D 图元抗锯齿过滤 (Sprite Filtering)",
        "tip": "sharp = 锐利抗锯齿（消除锯齿同时保留纹理清晰度）；smooth = 双线性平滑过渡；off = 原版近邻像素采样。"
    },
    "spriteFilterMin": {
        "label": "小尺寸图元抗锯齿过滤触发阈值",
        "tip": "控制在视口缩放多大时对细小图元激活抗锯齿过滤，防止远距离细小文字图标模糊。"
    },
    "spriteFilterSharpnessPct": {
        "label": "图元拉近视口时的边缘自适应锐度 (%)",
        "tip": "在镜头滚轮放大拉近视野时，图元边缘保持锐利对比度的百分比。"
    },
    "spriteFilterSprites": {
        "label": "对每帧动态图元一并应用抗锯齿",
        "tip": "除烘焙静态建筑外，对人物行走图元、掉落物品等所有逐帧绘制对象也一并应用平滑抗锯齿。"
    },
    "hdrAuto": {
        "label": "自动检测并匹配 HDR 显示器",
        "tip": "自动通过操作系统与显示接口查询主显示器是否支持 HDR10，并在支持时自动激活 10-bit HDR 高动态渲染通道。"
    },
    "hdrLightPct": {
        "label": "HDR：环境光高光亮度增益 (%)",
        "tip": "控制光源照亮物体时高光亮度的扩展范围，让被路灯和车灯照亮的物体更加通透鲜活。"
    },
    "hdrBloomPct": {
        "label": "HDR：强光高光辉光辉映增益 (%)",
        "tip": "手电筒、篝火和车灯周围泛光高斯光晕（Bloom）的高动态亮度增益比例。"
    },
    "hdrSunPct": {
        "label": "HDR：直射太阳光高动态亮度增益 (%)",
        "tip": "正午直射阳光的高动态亮度放大比例，营造真实刺眼的明亮艳阳天沉浸感。"
    },
    "hdrGlintPct": {
        "label": "HDR：水面与水洼闪耀微光亮度 (%)",
        "tip": "雨后积水表面反射阳光时微小镜面闪烁高光的峰值亮度。"
    },
    "hdrPaperPct": {
        "label": "HDR：漫反射白色基准亮度 (% 桌面白)",
        "tip": "世界中纯白漫反射物体相对于桌面标准白色的亮度基准（默认 100%）。"
    },
    "hdrItmPct": {
        "label": "HDR：夜间明亮像素高动态映射强度 (%)",
        "tip": "在深夜漆黑环境中，微弱光点向 HDR 高亮区间映射的敏感度比例。"
    },
    "hdrSaturationPct": {
        "label": "HDR：广色域饱和度微调 (%)",
        "tip": "在 BT.2020 / DCI-P3 广色域空间中微调色彩浓郁程度。"
    },
    "hdrPeakNits": {
        "label": "HDR 显示器硬件最大峰值亮度 (Nits)",
        "tip": "设置你使用的显示器的真实峰值亮度（如 400、600、1000 Nits），确保游戏色调映射严格适配屏幕物理极限。"
    },
    "hdrUiNits": {
        "label": "HDR：用户界面 (UI) 目标参考亮度 (Nits)",
        "tip": "游戏文字、物品栏与小地图等 UI 元素的亮度上限（通常 150~250 Nits），防止界面在黑夜中亮得刺瞎双眼。"
    },
    "ambientOcclusion": {
        "label": "环境光遮蔽 (Ambient Occlusion)",
        "tip": "在墙角、家具底部、楼梯与植被边缘生成极其写实柔和的 3D 地平线接触阴影，且几乎不增加性能开销。"
    },
    "aoStrengthFloorPct": {
        "label": "环境光遮蔽：地面接触阴影强度 (%)",
        "tip": "控制墙根、家具与地面接触处的暗角深浅程度。"
    },
    "aoStrengthWallPct": {
        "label": "环境光遮蔽：墙角与建筑转角阴影强度 (%)",
        "tip": "控制两面墙相交的夹角内凹暗影强度。"
    },
    "aoStrengthObjectPct": {
        "label": "环境光遮蔽：物品与小物件接触阴影强度 (%)",
        "tip": "桌上杂物、箱子、垃圾桶等环境道具底部的遮挡阴影强度。"
    },
    "aoStrengthVegetationPct": {
        "label": "环境光遮蔽：树冠与高大植被深处阴影 (%)",
        "tip": "大树内部树冠深处与地面的光线遮挡变暗程度。"
    },
    "aoStrengthPlantPct": {
        "label": "环境光遮蔽：地被草丛花卉柔和阴影 (%)",
        "tip": "草丛、灌木丛在地面形成的轻柔环境光遮蔽程度。"
    },
    "aoRadiusPct": {
        "label": "环境光遮蔽：阴影投射半径范围 (% 地块)",
        "tip": "接触阴影向外扩散羽化的地块比例半径。数值越大阴影越柔和宽广。"
    },
    "aoScalePct": {
        "label": "环境光遮蔽：计算缓冲区精细度比例 (%)",
        "tip": "环境光遮蔽贴图的分辨率比例。50% 即可获得极高画质且节省显存算力。"
    },
    "sunShadowStrengthPct": {
        "label": "动态太阳阴影：投影深浅浓度 (%)",
        "tip": "太阳长阴影的整体明暗对比深浅度。调大让阴影更加深邃分明。"
    },
    "sunShadowCharacters": {
        "label": "动态太阳阴影：角色与僵尸投射长阴影",
        "tip": "让视野内的玩家、联机同伴与僵尸随太阳角度在地面投下长长的斜阳投影。"
    },
    "sunShadowMeshes": {
        "label": "动态太阳阴影：基于 3D 真实骨骼轮廓投射",
        "tip": "阴影严格根据角色真实的 3D 骨骼动作与姿态生成，奔跑摆臂时投影栩栩如生。"
    },
    "sunShadowRate": {
        "label": "动态太阳阴影：更新计算比率",
        "tip": "太阳阴影几何重新计算的帧率频率。隔帧更新即可保持极致平滑且节省算力。"
    },
    "sunShadowAnimals": {
        "label": "动态太阳阴影：家禽与动物投射长阴影",
        "tip": "为牛、羊、鹿等动物一并启用真实的太阳长阴影投射。"
    },
    "entityShadows": {
        "label": "实体接触软阴影 (角色的软椭圆接触阴影)",
        "tip": "即便在无太阳直射的阴天或室内，也根据角色朝向在脚底投射柔和的定向接触阴影。"
    },
    "entityShadowFormPct": {
        "label": "实体接触阴影：朝向椭圆形态清晰度 (%)",
        "tip": "控制脚底接触阴影随角色身体朝向拉长或圆润的形态明显度。"
    },
    "entityShadowCasters": {
        "label": "投射接触软阴影的实体类型筛选",
        "tip": "all = 所有人物与僵尸；close = 仅视野近处角色；cars = 包含车辆。"
    },
    "entityShadowSelf": {
        "label": "实体接触阴影：身体自身投射自阴影",
        "tip": "角色手臂、背包和前胸在自身躯干上产生的微弱接触自阴影。"
    },
    "entityShadowImpostors": {
        "label": "远距离假人与远方僵尸投射软阴影",
        "tip": "在远距离僵尸进入降频模拟时，依然保持其脚下轻量软阴影绘制。"
    },
    "entityShadowTorches": {
        "label": "手电筒与车灯光照下产生实体阴影",
        "tip": "在夜间手电筒和汽车大灯强光扫过时，角色和僵尸背后投射出被强光拉长的动态暗影。"
    },
    "entityShadowAoPct": {
        "label": "实体阴影：脚下与邻近尸体的环境遮蔽 (%)",
        "tip": "尸体堆积处互相遮蔽产生的更加深邃的接触阴影强度。"
    },
    "entityShadowClouds": {
        "label": "实体阴影：多云遮日时阴影自动柔化衰减",
        "tip": "天空云层遮挡太阳时，所有角色的投影自动变淡并柔化，与真实天气变化融为一体。"
    },
    "sunShadowVehicles": {
        "label": "动态太阳阴影：车辆投射庞大长投影",
        "tip": "车辆在阳光照射下根据车身 3D 几何模型在路面上投下宏伟逼真的长阴影。"
    },
    "sunShadowTreeCards": {
        "label": "动态太阳阴影：树木使用真实树形面片投射",
        "tip": "树木不再投射单调圆形阴影，而是根据具体树种的枝叶轮廓投射错落有致的树荫投影。"
    },
    "sunShadowStockFadePct": {
        "label": "太阳阴影：原版角色脚底圆点阴影淡出比例 (%)",
        "tip": "淡出并隐藏原版游戏自带的粗糙黑圆圈假阴影，让真实的动态长投影取而代之。"
    },
    "sunShadowTorches": {
        "label": "手电筒与车灯点光源阴影投射",
        "tip": "手电筒射出的光束能够被墙角、门框和大型家具真实阻挡并投射背光阴影。"
    },
    "sunShadowSoftnessPct": {
        "label": "动态太阳阴影：边缘半影柔化程度 (%)",
        "tip": "阴影离物体越远边缘越柔和扩散（半影 PCF 柔化），模拟真实大气的漫反射散射现象。"
    },
    "moonShadows": {
        "label": "月夜动态月光阴影 (Moon Shadows)",
        "tip": "在晴朗夜晚满月当空时，冷色调的月光在地面投下清幽静谧的月影。"
    },
    "moonShadowPct": {
        "label": "月光阴影：相对于日光阴影的可见强度 (%)",
        "tip": "月光投影的浓度深浅比例，烘托末日黑夜的绝美月色氛围。"
    },
    "cloudShadows": {
        "label": "天空云层流动暗影 (Cloud Shadows)",
        "tip": "高空漂移的云层在地面投下的巨大柔和阴影，随风在森林和田野上缓缓掠过。"
    },
    "cloudOpacityPct": {
        "label": "云层地面暗影深浅不透明度 (%)",
        "tip": "云朵暗影在地面上的减光遮蔽程度。"
    },
    "cloudSpeedPct": {
        "label": "云层掠过漂移速度百分比 (%)",
        "tip": "云影随风在地面掠过的移动速度。"
    },
    "cloudScalePct": {
        "label": "云朵投影尺寸比例 (%)",
        "tip": "地面云影的大小比例，调大可呈现庞大的大朵积雨云暗影。"
    },
    "reflections": {
        "label": "屏幕空间反射 (Screen-space Reflections)",
        "tip": "为水面、积水、浴室镜子、玻璃窗、车窗以及金属表面带来现代写实的屏幕空间环境倒影。"
    },
    "reflectionStrengthPct": {
        "label": "屏幕空间反射：整体清晰度与强度 (%)",
        "tip": "反射图像的对比度与不透明度整体增益。"
    },
    "reflectionPuddles": {
        "label": "雨天地面积水与水洼写实环境倒影",
        "tip": "暴雨后路面积水中清晰倒映出天空、路旁电线杆、房屋和走过的僵尸。"
    },
    "carGlassReflectPct": {
        "label": "车窗玻璃：反光清晰度与强度 (%)",
        "tip": "车辆挡风玻璃与侧窗玻璃反射天空和周围环境的明亮程度。"
    },
    "carGlassInteriorPct": {
        "label": "车窗玻璃：车厢内透光率 (%)",
        "tip": "阳光或外界光线穿透车窗照亮车厢内部座位的透光程度。"
    },
    "carGlassSunPct": {
        "label": "车窗玻璃：日月直射强烈耀斑反光 (%)",
        "tip": "阳光直射角度照向车窗玻璃时产生的真实炫目镜面耀斑强度。"
    },
    "carGlassRainPct": {
        "label": "车窗玻璃：雨水水滴模糊反光 (%)",
        "tip": "下雨天车窗被雨水打湿后的水膜漫反射与模糊感比例。"
    },
    "carOccupant": {
        "label": "车窗玻璃：清晰看清车内驾驶员与乘客",
        "tip": "透过透明车窗玻璃清晰观察车内坐姿、角色动作以及僵尸扒车时的车内视角。"
    },
    "carOccupantOcclusion": {
        "label": "车窗玻璃：车门框与座椅真实遮挡车内人员",
        "tip": "车身立柱、车顶与座椅靠背对车内乘员产生严丝合缝的物理透视遮挡。"
    },
    "carOccupantLightPct": {
        "label": "车窗玻璃：车内乘员受光强度 (%)",
        "tip": "车厢内部人员接收外界环境光线的明亮程度。"
    },
    "occludedZombieOutlines": {
        "label": "受遮挡僵尸视觉轮廓描边 (Occluded Outlines)",
        "tip": "当玩家视线已确认僵尸存在但其身躯被墙壁、门或高大家具局部遮挡时，显示高科技柔和发光描边。"
    },
    "occludedOutlineIgnorePlants": {
        "label": "遮挡描边：被草丛或灌木遮挡时不触发",
        "tip": "被茂密草地遮挡的爬行僵尸不显示发光轮廓，保留草丛遇袭的恐怖惊悚感。"
    },
    "occludedOutlineWidth": {
        "label": "受遮挡僵尸轮廓描边粗细 (像素)",
        "tip": "遮挡发光轮廓线的物理像素宽度。"
    },
    "occludedOutlineColour": {
        "label": "受遮挡僵尸轮廓描边发光色彩",
        "tip": "轮廓发光的颜色主题（如警示红、幽灵白、潜行绿或亮橙）。"
    },
    "occludedOutlineOpacityPct": {
        "label": "受遮挡僵尸轮廓描边透明度 (%)",
        "tip": "发光描边的不透明度程度。"
    },
    "mirrorsWindows": {
        "label": "建筑窗户玻璃反射室外倒影",
        "tip": "城镇建筑临街的商店橱窗和住家玻璃窗清晰倒映出街景与路人。"
    },
    "mirrorsWindowPct": {
        "label": "建筑窗户玻璃倒影反射率 (%)",
        "tip": "建筑窗户玻璃的镜面反射强度比例。"
    },
    "mirrorsProps": {
        "label": "电视屏幕、柜台金属台面等道具反射",
        "tip": "关闭的电视机黑镜屏幕、金属厨具台面、光洁地砖均能映射出室内倒影。"
    },
    "mirrorsPropGlassPct": {
        "label": "玻璃与金属道具表面反射率 (%)",
        "tip": "道具物体反射环境图像的清晰度与反射率。"
    },
    "mirrorsGeometry": {
        "label": "镜面中反射周围 3D 建筑几何体",
        "tip": "在镜面中不仅反射角色，还完整映射镜子前方的墙壁、房门和走廊空间。"
    },
    "mirrorsCutawayHoldMs": {
        "label": "离开房间时镜面反射保持时间 (ms)",
        "tip": "玩家走出房间导致墙体剖面隐藏时，镜中倒影保持平稳不跳变的时间。"
    },
    "mirrorsModels": {
        "label": "镜面中反射角色 3D 骨骼模型",
        "tip": "走到浴室镜子前梳妆打扮，镜中能够毫发毕现地倒映出自己的 3D 人物形象与服装！"
    },
    "mirrorsViewLateralPct": {
        "label": "镜面侧向视差倾斜角度修正 (%)",
        "tip": "根据玩家相对于镜面的观察夹角，实时微调倒影在镜面中的侧向偏移。"
    },
    "mirrorsViewDropPct": {
        "label": "镜面垂直视差俯仰角度修正 (%)",
        "tip": "微调倒影在镜面中的垂直高度视差。"
    },
    "bloodWet": {
        "label": "湿润新鲜血迹水光反射 (Wet Blood)",
        "tip": "刚喷溅在地面或墙上的新鲜血迹呈现出逼真的湿润光泽与水洼镜面反射。"
    },
    "bloodWetMinutes": {
        "label": "血迹保持湿润反光的游戏内时间 (分钟)",
        "tip": "血迹在地面保持湿润发光的游戏分钟数。随后血液将自然风干凝固，失去反光特性。"
    },
    "bloodReflectPct": {
        "label": "湿润血迹表面反射清晰度 (%)",
        "tip": "新鲜血洼表面倒映天空与四周景象的反射清晰度。"
    },
    "bloodSheenPct": {
        "label": "湿润血迹表面高光微光光泽度 (%)",
        "tip": "血液表面特有的粘稠微光与光照散射强度。"
    },
    "bloodGlintPct": {
        "label": "湿润血迹边缘高光闪耀程度 (%)",
        "tip": "手电筒扫过血洼时边缘闪烁的高光敏感度。"
    },
    "godRaysStrengthPct": {
        "label": "丁达尔体积光 (God Rays) 整体明亮强度 (%)",
        "tip": "清晨与黄昏时分穿透树冠与窗棂的体积光束的可见明亮程度。"
    },
    "godRaysDustPct": {
        "label": "体积光中室内漂浮微尘光斑效果 (%)",
        "tip": "当阳光从窗户透入废弃室内时，光束中慢速漂浮的微小尘埃光斑效果强度。"
    },
    "godRaysPatchPct": {
        "label": "体积光斑块噪声混合度 (%)",
        "tip": "模拟真实大气尘埃团块的非均匀噪声混合度，让光束富有层次感。"
    },
    "godRaysSoftPct": {
        "label": "体积光射线边缘羽化柔和度 (%)",
        "tip": "光束边缘的柔和漫射羽化程度，防止光线显得像死板的硬线。"
    },
    "godRaysGlintPct": {
        "label": "穿透树叶缝隙的微光闪烁度 (%)",
        "tip": "在森林中行走时穿透树叶空隙的光束闪烁活跃度。"
    },
    "godRaysHazePct": {
        "label": "户外早晨薄雾散射朦胧度 (%)",
        "tip": "林间与田野清晨水汽薄雾对阳光的整体漫散射程度。"
    },
    "godRaysLocal": {
        "label": "手电筒、车灯与室内灯具体积光",
        "tip": "在浓雾或昏暗室内，手电筒光锥与车灯投射出可见的真实体积光柱效果！"
    },
    "godRaysLocalPct": {
        "label": "手电筒与车灯局部体积光亮度 (%)",
        "tip": "人造光源局部体积光柱的可见明亮强度。"
    },
    "foliageSwayPct": {
        "label": "植被风动摇曳：摆动幅度强度 (%)",
        "tip": "草地与树木随风力自然摆动弯曲的物理振幅比例。"
    },
    "foliageSwayTaps": {
        "label": "植被风动摇曳：顶点变形采样品质",
        "tip": "着色器在计算风动波动时的多阶采样质量。high = 最丝滑自然的微风波浪。"
    },
    "darknessFloorPct": {
        "label": "黑夜最低环境光亮度保底 (%)",
        "tip": "设置纯黑环境下最低环境可见度保底（如 3%~8%）。彻底解决原版黑夜哪怕站在空地上也纯黑一片、人眼伸手不见五指的痛苦体验。"
    },
    "darknessFloorBasements": {
        "label": "地下室与密封暗室一并应用最低亮度保底",
        "tip": "关闭时地下室保持绝对纯黑；开启时地下室也能隐约看清粗略墙壁轮廓。"
    },
    "memoryTint": {
        "label": "已知记忆区域淡色提示 (Remembered Places)",
        "tip": "当角色离开房间或背对某处时，曾经探索过的已知视野区域以优雅的淡灰暗影显示，而非突兀地沦为黑幕。"
    },
    "memoryTintPct": {
        "label": "记忆区域色彩饱和度衰减程度 (%)",
        "tip": "记忆区域相对于当前视线内真实区域的去饱和淡化程度。"
    },
    "memoryLightPct": {
        "label": "记忆区域最低保留亮度保底 (%)",
        "tip": "记忆区域在夜间依然保留的轮廓微弱亮度。"
    },
    "colorGrading": {
        "label": "电影感色彩分级与色调映射 (ACES Grading)",
        "tip": "为游戏世界注入现代电影工业级别的 ACES 色调映射，亮部柔和不过曝，暗部深邃有层次，氛围感拉满。"
    },
    "colorGradingPct": {
        "label": "色彩分级全局滤镜强度 (%)",
        "tip": "色彩分级效果在画面中的整体混合权重。"
    },
    "colorGradingNightPct": {
        "label": "夜晚专用夜视色彩分级偏移 (%)",
        "tip": "深夜时分将色温自然微移向幽蓝冷色调，强化恐怖求生的压迫氛围。"
    },
    "pixelLight": {
        "label": "逐像素点光源光照 (Per-pixel Lighting)",
        "tip": "将蜡烛、壁灯、火把等光源从原版粗糙的 2D 贴图格子光照升级为现代游戏标准的逐像素点光源计算，光影细腻逼真！"
    },
    "pplAnalytic": {
        "label": "点光源光照：平滑物理衰减模型",
        "tip": "使用基于物理的精确平滑距离衰减曲线，消除原版光照在格子边缘的生硬切断棱角。"
    },
    "pplPointLights": {
        "label": "蜡烛、油灯、营火等所有灯具启用逐像素光照",
        "tip": "使世界中每一个独立发光的小道具均散发出高质量动态光芒。"
    },
    "pplNormals": {
        "label": "地面与墙体法线参与光照明暗起伏计算",
        "tip": "光线照射在砖墙、木地板上时，根据表面材质凹凸法线呈现细腻的受光面与背光面。"
    },
    "pplWrapPct": {
        "label": "漫反射表面光线环绕漫透率 (%)",
        "tip": "模拟粗糙表面微小次表面散射，让背光面过渡极其自然柔和。"
    },
    "pplSmooth": {
        "label": "逐像素光照地块接缝平滑过渡抗走样",
        "tip": "彻底消除不同建筑地块网格接缝处的光照明暗撕裂线。"
    },
    "pplWetSpecular": {
        "label": "潮湿雨天地面的点光源高光镜面反射",
        "tip": "在雨天地面被水浸湿时，路灯与车灯在地面映射出长条状湿润高光。"
    },
    "pplSpecPct": {
        "label": "点光源高光反射强度比例 (%)",
        "tip": "金属与潮湿表面对点光源镜面反射的明亮程度。"
    },
    "pplShadows": {
        "label": "点光源在家具与小物件背后产生微阴影",
        "tip": "手提灯与火把能够照出室内桌椅背后的柔和背光阴影。"
    },
    "pplTorchFeetGlow": {
        "label": "手电筒光晕在玩家脚下地面的漫射泛光",
        "tip": "拿着手电筒时脚边地面自然受光漫射，无需将光线完全对准脚下也能看清近处地砖。"
    },
    "torchSource": {
        "label": "手电筒真实物理光源点 (光线从手中射出)",
        "tip": "修复原版手电筒光束凭空从身体中央散发的违和感，光束严格从角色手中的手电筒或枪灯灯头精准射出！"
    },
    "torchSourceAim": {
        "label": "手电筒光束随瞄准手势精准指向",
        "tip": "手电筒光柱随角色的持枪瞄准手臂姿势与高低角度完全同频转向。"
    },
    "torchSourceSelfShadow": {
        "label": "手电筒光线被玩家自身身体遮挡自阴影",
        "tip": "手电筒朝前照射时，玩家背部和身后地面自然保持在阴影中，极具真实感。"
    },
    "relief": {
        "label": "2D 地块法线视差立体浮雕 (Relief Textures)",
        "tip": "在不改变任何原生贴图的前提下，通过着色器算法为砖墙、瓦顶和碎石路生成触手可及的 3D 浮雕凹凸立体感！"
    },
    "reliefDepthPct": {
        "label": "浮雕立体凹凸深度百分比 (%)",
        "tip": "控制视差贴图凹凸视差的下陷深度感。"
    },
    "reliefSunPct": {
        "label": "直射阳光与月光下的浮雕阴影对比度 (%)",
        "tip": "阳光照射砖石凹陷缝隙时投射的微小阴影对比度。"
    },
    "reliefTorchShadowSteps": {
        "label": "手电筒强光近距离照射下的浮雕步进精度",
        "tip": "手电筒斜照墙壁时微阴影视差光线追踪步进层级数。"
    },
}
