# AgenticSociety

#### Description
This repo is to support our work in applying language model agents in the research of social and economic discipline. 

#### 软件架构
为了便于进行小规模的数据实验与结果观察分析，开发了一个studio桌面，总的原则是，小规模的实验，方便用studio定义，节省资源。大批量作业专门开发python脚本完成。其功能如下：
1. 生成persona采样
2. 定义persona group
3. 定义question group
4. 选取persona group和question group，定义experiment
5. 执行experiment
实验结果的提取分析目前，目前主要支持personality traits test， 不同experiment中对同一个persona的实验结果，在personality表中会覆盖，这一点需要引起注意。但是这仅仅是“实验结果提取分析”目前的一个临时安排，personality表也是一个综合提取personality traits test实验结果用的临时表，experiment本身的实验结果的原始数据quest-answer和quize-answer表本身，不同experiment的结果是互相不干扰的
#### 数据结构设计
目前数据存放于data/db/agent-society.db中，sqlite数据库文件

![alt text](doc/image.png)

如上图所示：
1. persona表是采样结果，附加了persona_desc是LLM根据skeletal feature vector进行enrich的结果
2. question表，存放问卷问题。问题划分为问题集question_set
3. question_group是studio定义的，相当于一个问卷
4. persona_group是studio定义的，控制一次实验于较小的可控的规模
5. question_answer. 如果执行模式是一个问题一个request，结果放在这个表中
6. quiz_answer. 如果执行模式是组卷，一个卷子是一个quiz，结果放在这个表中


#### Installation

poetry install即可


#### Instructions

1.  人口普查数据在data/census/csv中
2.  IPIP-NEO数据在data/IPIP-NEO中
3.  prompt在prompts中
4.  asociety是引擎部分，而tools中是UI和工具脚本，包括问题集导入。问题集jaonl文件在data/test中，用工具导入sqlite

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request


#### dataset
   

#### misc
问题：我们已经知道LLM有了数学能力，其他各种能力。我们的问题是：agent被endowed with a persona之后，背后的那个LLM会在角色扮演中，比如在扮演一个小学生时“装作”缺少高数能力吗？这非常intrigue，其实把这个问题reframe一下是：这个能力，没有任何形而上的含义，它就是概率的结果，就是图灵模仿；persona中的关于教育程度的文本token，就是能够降低“正确答案”出现的概率而已