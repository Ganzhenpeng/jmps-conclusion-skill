# 结论的句子语言与衔接

以下是围绕原文可观察写法的编辑决策；例句为原创虚构写作材料，不是本项目计算结果，也不是论文原句。语言自然应服从物理对象、关系与证据，不能由词频、句长或避用某个词单独判断。

## 选择能够推进结论的主语

先决定本句要让读者记住什么：方法、控制量、现象或比较结果。当重点是物理响应，让响应或其决定因素作主语；当贡献就是模型构造，作者或模型可以作主语。当执行者无关紧要而处理对象重要时，被动语态也可自然。避免每句都用 The proposed method 或 This study 起头；也不要强制每个句子都以物理量起头。

虚构输入：在平均刚度固定时，增大材料反差，模型显示第一带隙的上边界降低；下边界基本不变。

> A numerical investigation was carried out to examine the effects of the contrast on the variation of the first band gap. The results demonstrate that an increase in the contrast results in a reduction of its upper edge when the average stiffness is fixed.

> At fixed average stiffness, the model predicts that increasing the material contrast lowers the upper edge of the first band gap, while its lower edge remains nearly unchanged.

第二版把控制条件放在读者解释趋势之前，用 the model predicts 表明证据角色，以 contrast 的变化对应上边界响应，保留不变的下边界以说明带隙变化的来源。这里“lowers”只有在受控结果支持该方向时才能用；若只有相关性或机制未隔离，应写观察关系并保留不确定性。原始输入没给模型名称、区间或单位时不得补造。

## 用主句承载新认识，用从句界定关系

主句优先承载想让读者带走的发现；条件、比较、让步或原因按照其物理作用放在可理解的位置。限制主句成立的条件要靠近该主张；确切解释机制时才用 because/as a result of。长句如果含两项互不依赖的新发现、多个从句使对象不清或条件作用域不明，应拆开；若同一主张的条件与响应紧密相连，一句话可以较长。

虚构输入：仅在三组测试材料的第二传播支中，相对频率误差小于1%；第一带隙未检验。

> The model predicts all branches accurately, and the errors are below 1%.

> For the second propagating branch of the three tested materials, the relative frequency error remains below 1%; the first band gap was not assessed.

限制也可以单独成句，以减少一个主句的拥挤。不要因为缩短而删掉第二传播支、三组材料或相对频率误差；没有对比数据不能写 superior 或 universally accurate。

## 让相邻句围绕可追踪的对象展开

先确认上一句的真正新信息，再决定它在下一句承担什么角色：继续解释其物理机制、比较另一状态、说明范围，或由它引出有证据的意义。下一句可重复必要名词、用明确的代词或换成对应的物理量；代词指代不清时重复术语比用 This effect 更自然。句间因果只有在证据成立时才能表示为因果，不把时间先后、数值同时变化或参考曲线吻合自动升级为因果。

虚构输入：特定工况下位移误差很小，而曲率误差较大；在同一给定宏观状态下加入胞元校正后曲率误差降低。

> The displacement is accurate. The method is effective. The cell field is also accurately reconstructed.

> A small displacement error does not ensure accurate curvature in the tested state. At the same prescribed macroscopic state, cell corrections reduce the curvature error.

第一句的 curvature error 成为第二句继续讨论的对象，第二句增加“给定同一宏观状态”的限定。它说明条件重构改善了什么，不宣称独立模态预测成功；若没有可靠误差大小，不能自行增加百分数。

## 拆解名词串，保留修饰关系

当三个以上名词叠在一起，先识别被修饰对象、动作、作用对象和条件。例如“field reconstruction accuracy improvement”可能指场重构更准确，也可能指用重构提升别的量的准确度；回到原文判断，再用动词或介词恢复方向。领域内已约定的固定术语可以保留，不应把每个复合词都拆散。

虚构输入：位移均值用于确定宏观状态，胞元校正用于恢复局部曲率。

> The macroscopic displacement mean based cell curvature reconstruction improvement is demonstrated.

> The mean displacement defines the macroscopic state, and cell corrections improve the reconstruction of local curvature.

第二版把“定义状态”和“改善曲率重构”分成两个可核查动作。它不暗示均值直接决定唯一微观场；若后者需要额外边界或正则性条件，须保留。

## 对照样本时的范围

文献例证须记录DOI、来源版本和句子位置；分析句法功能，不将他人的句子直接拼进用户论文。引用文章的措辞与结论，只在原文上下文支持的范围内解释。相近构造可以承载不同科学对象；写入新稿前重新核对控制变量、量纲、比较方向与确定性。单篇或同一研究家族的用法是案例，不直接认定为全刊规范。用户偏好的中文句子先以自然中文建立关系，再翻译成英文，不把英文语序机械倒入中文。

### 已读原文的两个例子

- [Pernas-Salomón 与 Shmuel，2018](https://arxiv.org/abs/1804.08701)，作者稿第5节。作者先陈述低频界面阻抗匹配，后一句以“As frequency increases”转换条件，再交代阻抗不匹配及反射。这里的频率短语让读者知道比较条件变了，后半句给出实际响应；并不是所有结果都需要以时间或条件状语开头。后续有限结构的透射讨论仍保留频带及模型对象，不能从这个例子推出任意模型的失效规律。
- [Pernas-Salomón 与 Shmuel，2020](https://arxiv.org/abs/1904.09180)，作者稿第5节。作者先说所建方法揭示的耦合，随后以“We conjecture”明确转入对必要性的猜想，再用具体耦合对象继续讨论能量转换。可学的是承接同一科学对象并区分证据强度；不能把猜想改成已证明的定理，也不将其词句复制到其他论文。
- [Gardner 等，Nature，2022](https://doi.org/10.1038/s41586-021-04268-7)，Discussion 第14–15段。前文引入观测到的拓扑结构，后文将该结构在不同环境中的不变性作为主语；让步从句说明两类模型的共同预测，主句指出能区分模型的现象，另一从句保留共存机制。比较和限定分担不同句法职责，须保留共存可能性。
- [Yang 等，Nature Communications，2015](https://doi.org/10.1038/ncomms7649)，Results 第18–19段。先列举与裂纹扩展相关的胶原行为，下一句用这些机制作主语，说明其中几项对变形和裂纹钝化的作用。由上句新引入的对象转为下句主语，使机制清单进入解释；若有多个可能的指代对象，应重复具体名称。
- [Zhao 等，Science Advances，2016](https://doi.org/10.1126/sciadv.1501297)，无标题正文末段。两个网络结构特征先并列命名，相邻句用 former/latter 将其分别连接到弹性和塑性作用，后置短语说明具体机制。只有先行项恰有两个且顺序、对应关系明确时才使用这一压缩方式；否则写出两个对象。
