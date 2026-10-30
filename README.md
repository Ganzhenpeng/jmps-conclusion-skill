# JMPS Conclusion Skill

面向 **Journal of the Mechanics and Physics of Solids（JMPS）研究论文结论**的生成、压缩、翻译与审阅。核心是选出有证据的科学发现，让方法、机制、比较和范围形成自然收束；不通过固定句数、段数、压缩率或宣传性措辞模拟顶刊风格。

入口：[jmps-conclusion/SKILL.md](jmps-conclusion/SKILL.md)。使用示例：

> 使用 $jmps-conclusion，根据当前稿件的主要结果生成一版精炼中文结论，并说明保留哪些发现、删去了哪些重复。不要增加正文没有支持的数据或因果。

> 使用 $jmps-conclusion，将这段结论改成自然英文，保留模型假设、数值、比较方向和证据强度。

v0.2新增[句子语言与衔接](jmps-conclusion/references/sentence-language.md)：针对主语选择、主句与条件从句、相邻句的信息承接及名词串压缩给出可核源文观察和原创对照。相关记录见 `evidence/sentence_language_*`；原v0.1评测记录保留，新增研究和测试另见 `evidence/SENTENCE_LANGUAGE_EVALUATION.json`。

本轮完成 **180篇百次累计引用样本**：JMPS 60、Nature主刊60、其他刊60（Nature Communications 25、Science Advances 31、PNAS 4）；另外保留25篇JMPS相关性锚点，共 **205篇**。研究对象是结论、Discussion末段及必要局部上下文，**不是205篇全文科学评审，也没有训练基础模型**。

高引用以公开数据库2026-10-30快照记录，≥100次是本轮操作口径，并非学科归一化认证或全刊最高引排名。初始JMPS60篇只有35篇达到门槛，因此另补25篇高引论文，保留初始25篇较低引锚点。原始三组各48篇归纳/12篇留出，补样20篇归纳/5篇留出；共164篇归纳和41篇冻结留出。归纳样本独立抽查35篇，实际生成测试与家族独立性限制分别报告。方法与偏差见[证据范围](jmps-conclusion/references/evidence-scope.md)，逐篇记录在[evidence/](evidence/)。

公开包不含论文全文、未发表原稿、批注、聊天记录、私人路径或凭据。反例为脱敏问题说明和原创合成示例。已发表文章的某种写法只作可定位观察，不因其高引就照单全收。

可直接查阅[180篇百次引用清单](evidence/HIGH_CITATION_180.json)、[35篇独立抽查摘要](evidence/INDEPENDENT_REVIEW.json)、[11个真实文献双语示范与3个合成反例](evidence/BEHAVIOR_EXAMPLES.json)。原始41篇冻结留出中，两篇确认家族泄漏、两篇独立性存疑已排除；37篇仅表示在本轮审查范围内未发现这些问题，不能写成37个生成测试全部通过。

将 `jmps-conclusion` 文件夹放入使用环境的Skills目录即可使用；本仓库不自动安装、不替换其他技能，也不改动论文。技能本身没有运行时依赖。开发检查可运行：

```sh
python tests/validate_bundle.py
```

结构检查、独立抽查与实际生成测试是不同证据；实测范围和保留问题见 `evidence/EVALUATION.json`。没有盲测或统计证据证明本技能优于其他技能，也不承诺任何期刊录用结果。
