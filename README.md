# RenderFlow
加速Cinema 4D渲染工作流程
> 当前版本 ：1008
# Render Engine Support--渲染器支持
- Octane 
- Redshift
- Arnold
# Main Function--主要功能
- 根据当前选择渲染引擎切换对应的优化功能，支持Octane，Redshift，Arnold三款主流渲染器
- 以全新的Standard Surface为标准,支持Node Editor材质
- 智能材质编辑器：根据所选对象或材质激活对应的材质编辑器
- 根据所选对象智能创建材质 、灯光、 标签
- 统一的工程管理工具
- 快捷管理器(WIP)
- 建模/MG/标签/材质等相关小工具
​
# How to Use--使用
在可读写路径中安装插件(%AppData%\Maxon\Maxon Cinema 4D R2x_xxxxxxxx\plugin)
默认快捷键为 ~ 飘号键(Tab上方键)
如果快捷键失效，切换中英文输入法
仍然无效，检查是否安装正常，检查是否有快捷键冲突(Shift + F12,输入RenderFlow查看)
仍然无效，按Shift + F10，唤出Console控制台查看Python部分报错


### 由于使用NodeAssetInterface api ，R25以下版本会报错, 暂时没有做低版本兼容
