# argparse
> argparse是一个Python模块：命令行选项、参数和子命令解析器，命令行参数解析器  
主要有三个步骤：
* 创建 ArgumentParser() 对象  
ArgumentParser()对象将命令行解析成 Python 数据类型  
` parser = argparse.ArgumentParser(description='Process some integers.')`   
* 调用 add_argument() 方法添加参数  
add_argument() 方法   
`ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])`   
参数说明：   
name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。  
action - 当参数在命令行中出现时使用的动作基本类型。  
nargs - 命令行参数应当消耗的数目。  
const - 被一些 action 和 nargs 选择所需求的常数。  
default - 当参数未在命令行中出现时使用的值。  
type - 命令行参数应当被转换成的类型。  
choices - 可用的参数的容器。  
required - 此命令行选项是否可省略 （仅选项可用）。  
help - 一个此选项作用的简单描述。  
metavar - 在使用方法消息中使用的参数值示例。  
dest - 被添加到 parse_args() 所返回对象上的属性名  

* 使用 parse_args() 解析添加的参数   
`parser.parse_args()` 

for example:  
```
parser = argparse.ArgumentParser()
parser.add_argument("hosts")
parser.add_argument("ports")
parser.add_argument("-u", "--UDP", help="Perform a UDP scan on the ports specified", action="store_true")
parser.add_argument("-t", "--traceroute", help="Use traceroute with the scan", action="store_true")
args = vars(parser.parse_args())
```
