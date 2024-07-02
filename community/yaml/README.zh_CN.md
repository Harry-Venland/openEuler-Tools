# yaml解析

## 使用方法：

- 运行程序。
- 程序将自动在当前目录及其子目录中搜索所有YAML文件。
- 程序将解析每个YAML文件中的`name`和`upstream`字段。
- 程序将把解析出的数据写入到一个名为`yaml_data.xlsx`的XLSX文件中。
- 程序将在控制台输出一条消息，指示数据已经写入到XLSX文件。

### 注意事项：

- 该程序假设所有YAML文件都包含`name`和`upstream`字段。如果某些文件不包含这些字段，则相应的单元格将保留为空。
- 该程序使用`openpyxl`库来操作XLSX文件。如果您尚未安装该库，请先使用`pip install openpyxl`命令进行安装。
- 该程序使用`yaml`库来操作yaml文件。如果您尚未安装该库，请先使用`pip install yaml`命令进行安装。
- 该程序将生成的XLSX文件保存在当前工作目录下，文件名为`yaml_data.xlsx`。如果需要在其他位置保存文件，请修改`output_file`变量的值。
