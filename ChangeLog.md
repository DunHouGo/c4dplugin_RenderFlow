###  ==========  UPDATE LIST  ==========  ###
# For RenderFlow

# 1000
- 旧版脚本 ：https://community.boghma.com/d/22
- RenderFlow插件化，更完善和封闭
- 全新界面，支持Octane，Redshift，Arnold三大主流渲染器
- 统一默认Standard Surface，迁移到Node Editor工作流程，弃用传统xpresso界面
- 新增Basic Flow，增加通用功能
 
# 1001
- 2022.08.20 fix
- 增加不自动指认快捷键版本
- 全面支持撤销
- 增加细化的使用文档和gif示意图
- Scatter 显示bug ==》 调用BaseDocument.SetActiveObject解决

# 1002
- 自动添加GSG link标签
- 目标灯光现在会自动指认一张灯光贴图和HDR link （Arnold自动指认tx）
- HDR（Dome Light）在会自动指认一张HDR和HDR link （Arnold自动指认tx）
- HDR link默认不指认任何贴图，保持工程整洁
- 新增合并材质，新建材质替换所有选择材质的指认，Alt可删除原材质
- 优化RS proxy和BakeSet流程
- 
# 1003
- 2022.12.03 fix
- 更新文件夹结构，适配标准插件结构
- 更新注册名，适配标准插件结构 ==》 "LighSolo"
- 新增符号 4d.Orslight ，c4d.Olight
- 新增工作流程管理，Root Space，NewProject，Make Preview(暂未开放)等

# 1004
- 修复中文排版
- Move to Top修复全局坐标错误
- Add Folder会自动添加图标tex到全局纹理路径，避免卡顿
- Add Folder加入初始相机绑定，更换为高级绑定
- Add Folder：特定文件夹会自动重命名对应层，子集为同一层（可关闭）
- 合并材质的新材质类型现在会参照第一个选择的材质

# 1005
- 新建目录更新到 v1.1
- 修复缺失文件夹bug
- 新建工程更新到 v1.2
- 增加当前工程关闭(新建工程)
- 增加当前工程移动到过程文件夹中（Process）
- 合并材质按住Ctrl会清除未使用的材质（不合并材质)

# 1006
- 更改文件夹结构为标准结构(适配插件管理器)
- 多通道EXR默认为DWAB格式,节省磁盘空间
- Octane Tag现在会自动跟随对象名称(Alt执行模式)
- 跟随custom Shortcut api更新

# 1007
- 适配PluginManager细微调整
- 全面使用2023.1.0 sdk符号,不再兼容2023之前版本
- 更新相机绑定,激活时只更改渲染视口的相机

# 1008
- 更改Folder结构，删除绑定的默认相机
- 修复Folder自动图层Bug

# 1009
- RenderPath：当渲染器为Octane时，设置info sampleing mode为without filtering（对Alpha取消AA）
- 注意：这个设置会禁用DOF和运动模糊（为了Z Depth通道更完美），如果需要，改回Distributed Rays即可
- 可编辑对象的材质默认为UVW projection（修复默认球形投射）