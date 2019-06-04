# 命令行外挂程序
![image](https://github.com/ustcfjh/CommandLine-tag-on-service/blob/master/interface.png)

## 程序功能
![image](https://github.com/ustcfjh/CommandLine-tag-on-service/blob/master/img.png)

* 1)命令行模板
定义命令行的格式及相应必要元素。
使用者只要按照命令行模板的格式修改就可以增删改命令行，启动时供命令行外挂程序读取。
* 2)命令行外挂程序
启动时从命令行模板读入所有的命令行，作为用户可输入的命令行列表。
命令行外挂程序负责从终端读取输入，进行解析匹配到对应的命令行，并且可以获取执行结果并输出到终端上。
* 3)主体c程序
主体c程序负责接收命令行外挂程序的输入，进行内部处理后将结果返回给外挂程序。


## 使用方法

运行环境： Window

只需额外安装 prompt_toolkit 工具库，命令行输入 python main.py 运行 

CommandTemplate.docx 文件中存放命令行模板，模板的定义在“嵌入式系统的命令行系统.docx”中的附加word文档“数通命令参考写作模板&样例”中

