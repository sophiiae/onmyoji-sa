# OSA.exe 使用说明

## 快速开始

1. **运行程序**
   - 双击项目根目录下的 `OSA.exe` 启动程序
   - 或者双击 `启动OSA.bat` 启动程序（推荐）
   - 或者双击 `快速启动OSA.bat` 快速启动
   - 程序会自动加载 `configs` 目录下的所有配置文件

**注意：** 首次启动可能需要30-60秒，这是正常现象。后续启动会更快。

2. **编辑配置**
   - 在左侧面板中编辑各种配置选项
   - 配置会自动保存
   - 使用快速导航按钮快速跳转到不同配置部分

3. **运行脚本**
   - 点击右上角的"运行"按钮
   - 程序会根据当前选中的配置文件运行相应的脚本
   - 运行状态和日志会显示在右侧面板中

## 界面说明

### 左侧配置区域
- **快速导航栏** - 快速跳转到不同配置部分
- **配置编辑区** - 编辑各种配置选项
- **自动保存** - 所有修改都会自动保存

### 右侧日志区域
- **运行按钮** - 启动/停止脚本运行
- **日志窗口** - 显示脚本运行状态和日志信息
- **实时更新** - 日志会实时更新

## 配置文件

### 默认配置
- `configs/osa.json` - 默认配置文件（优先显示）

### 其他配置
- `configs/1qian.json` - 千寻配置
- `configs/2nian.json` - 念配置
- `configs/3yu.json` - 雨配置
- 等等...

## 配置部分说明

### 脚本设置
- 设备连接配置
- 区域设置

### 日常任务
- 自动签到
- 邮件领取
- 御魂整理
- 体力领取

### 探索
- 自动探索
- 御魂清理
- 式神备份

### 结界突破
- 自动突破
- 门票管理

### 御灵
- 御灵挑战
- 等级设置

### 式神活动
- 活动挑战
- 门票管理

### 地域鬼王
- 鬼王挑战
- 奖励设置

## 使用技巧

1. **配置切换**
   - 点击不同的配置标签页切换配置文件
   - 每个配置文件都是独立的

2. **运行控制**
   - 点击"运行"开始执行脚本
   - 再次点击"停止"停止执行
   - 运行状态会实时显示

3. **日志查看**
   - 右侧日志窗口显示详细的运行信息
   - 可以查看错误信息和运行状态

4. **配置备份**
   - 配置文件会自动保存
   - 建议定期备份 `configs` 目录

## 注意事项

1. **首次运行**
   - 确保 `configs` 目录存在且包含配置文件
   - 程序会自动创建必要的目录

2. **权限要求**
   - 某些功能可能需要管理员权限
   - 如果遇到权限问题，尝试以管理员身份运行

3. **杀毒软件**
   - 某些杀毒软件可能会误报
   - 需要将程序添加到信任列表

4. **文件大小**
   - exe文件较大（约1GB），这是正常的
   - 包含了所有必要的依赖库

## 故障排除

### 程序无法启动
1. 检查是否有杀毒软件阻止
2. 尝试以管理员身份运行
3. 确保有足够的磁盘空间

### 配置文件加载失败
1. 检查 `configs` 目录是否存在
2. 确保配置文件是有效的JSON格式
3. 检查文件权限

### 脚本运行失败
1. 查看右侧日志窗口的错误信息
2. 检查配置文件中的设置
3. 确保模拟器或设备已连接

### 日志显示异常
1. 检查日志目录权限
2. 确保有足够的磁盘空间
3. 重启程序尝试

## 技术支持

如果遇到问题，请：
1. 查看右侧日志窗口的错误信息
2. 检查配置文件设置
3. 确保所有依赖文件完整

## 文件结构

```
项目根目录/
├── OSA.exe (主程序)
├── 启动OSA.bat (启动脚本)
├── 构建OSA.bat (构建脚本)
├── build/ (构建工具目录)
│   ├── build_exe.py (构建脚本)
│   ├── build.bat (构建批处理)
│   ├── test_exe.py (测试脚本)
│   └── BUILD_README.md (构建说明)
├── configs/ (配置文件目录)
│   ├── osa.json (默认配置)
│   ├── 1qian.json
│   └── ...
├── tasks/ (任务脚本)
├── module/ (核心模块)
├── data/ (数据文件)
└── logs/ (日志目录)
``` 