# 知识工程数据标注大作业脚本

一个简单脚本，功能为：

- 打开json文件，按顺序依次自动在百度百科搜索entity词语
- 显示处理好的文本，高亮entity词语
- 监听剪贴板，自动处理并写入复制的url
- 长按Rshift跳过（写入None）

## 如何使用

应该不用打包可运行文件了，下载py，将BroswerPath和Json_file_path改为自己的，运行

复制该词语在百度百科上的URL，如果复制的URL与剪贴板的上一个复制不同将自动检测，在程序中按下enter自动处理剪贴板中的URL并写入

如果该词语对应None，长按Rshift跳过该句子

> 没有写存档功能，一次弄完吧，孩子( ﾟ∀。)
