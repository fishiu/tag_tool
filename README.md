# 关键短语功能分类

创建于20210413

## 1 数据标注模块

### 标注内容

本项目数据集为 WoS 17万篇 Big Data 相关的题录数据。我们使用全集的关键短语词典（去除了高频的 Single Word）来查找一篇文章并圈出候选关键短语。我们现在需要对给每个词打上T、M、P功能分类标签，之后用于训练模型来自动标记关键短语。下面是分类说明。

| 分类简称 | 分类全称 | 功能具体说明           |
| -------- | -------- | ---------------------- |
| T        | Task     | 任务、目的、应用       |
| M        | Material | 材料、数据、资料       |
| P        | Process  | 过程、方法、技术、手段 |

### 1.1 标注系统使用说明

#### 键盘标注

- `T、M、P` 按键分别对应相应内容
- `1、2、3` 按键分别对应 `T、M、P`
- `Backspace` 清空当前标注

#### 鼠标标签

- 点击 `1、2、3、4` 分别对应 `T、M、P、清除`

#### 保存

- 只有在进行翻页动作（包括跳转）时才会进行保存

### 1.2 TODO
- [ ] 增加保存按钮
- [ ] 调整分页模块的UI
- [ ] 实现 Keyphrase 选中（目前因为和鼠标动作冲突，禁用了选中）

## 2 数据预处理模块

处理标注数据，生成需要的数据格式。

数据来源包括两部分

## 3 模型数据模块

- 模型配置（每一次训练都要创建一个模型）

- 公用数据（比如预训练模型）

## 4 训练和评估模块

- 数据读取 `Dataloader`
- 模型构建