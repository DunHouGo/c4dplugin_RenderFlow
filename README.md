### Cinema 4D渲染工作流程插件

<aside>
🔒 当前版本 ：1010

</aside>

文档移植中，源文档可以查看 ： [RenderFlow](https://dunhou.gitbook.io/dh-renderflow/)

# Download--下载

[BOGHMA 社区下载](https://community.boghma.com/)

[Gitee（国内源）](https://gitee.com/DunHouGo/c4dplugin_RenderFlow/repository/archive/master.zip)

[Github（国外源）](https://github.com/DunHouGo/c4dplugin_RenderFlow/archive/refs/heads/master.zip)

# Install--安装

- 推荐使用PluginManager统一管理安装更新：[PluginManager](https://www.notion.so/Plugin-Manager-72c5fe979541467187af2060fe330e80)
- 解压文件夹,复制到C4D的plugin文件夹下

> `%AppData%\Maxon\Maxon Cinema 4D R2x_xxxxxxxx\plugins\CINEMA 4D R2x\plugins\Boghma`
> 

<aside>
⚠️ 不要更改文件夹结构和名称，会导致插件报错

</aside>

# Main Function--主要功能

- 根据当前选择渲染引擎切换对应的优化功能
- 智能材质编辑器：根据所选对象或材质激活对应的材质编辑器
- 根据所选对象智能创建材质 、灯光、 标签
- 统一的流程工具
- 集成的管理器：包括WIP
- 根据渲染引擎的智能散布
- 建模相关小工具
- MG相关小工具
- 标签相关小工具
- 材质相关小工具

# How to use--使用

- 正确安装插件
- 默认快捷键为 ~ 飘号键(Tab上方键)
- 如果快捷键失效，切换中英文输入法
- 仍然无效，检查是否安装正常，检查是否有快捷键冲突(Shift + F12查看)
- 仍然无效，按Shift + F10，唤出Console控制台查看Python部分报错

# Support Engine--支持渲染器

- Octane
- Redshift
- Arnold

# Shortcut--快捷键

- 默认快捷键为 ` ( Tab键上方 )
- 如果不起作用 , 尝试切换英文输入法 , 并且检查是否正确安装
- 快捷键可以按照个人喜好更改( Shift+F12 ) , 更改后默认快捷键失效
- 推荐使用Add添加自定义快捷键 , 而不是Assign

# Video --视频教程

暂无
### 由于使用NodeAssetInterface api ，R25以下版本会报错, 暂时没有做低版本兼容
