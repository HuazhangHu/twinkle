### WTForms支持的HTML标准字段 
- StringField	文本字段  
- TextAreaField	多行文本字段 
- PasswordField	密码文本字段 
- HiddenField	隐藏文件字段 
- DateField	文本字段，值为 datetime.date 文本格式 
- DateTimeField	文本字段，值为 datetime.datetime 文本格式 
- IntegerField	文本字段，值为整数 
- DecimalField	文本字段，值为decimal.Decimal 
- FloatField	文本字段，值为浮点数
- BooleanField	复选框，值为True 和 False  
- RadioField	一组单选框 
- SelectField	下拉列表  
- SelectMutipleField	下拉列表，可选择多个值  
- FileField	文件上传字段  
- SubmitField	表单提交按钮  
- FormField	把表单作为字段嵌入另一个表单  
- FieldList	一组指定类型的字段  

### WTForms常用验证函数
- DataRequired	确保字段中有数据  
- EqualTo	比较两个字段的值，常用于比较两次密码输入  
- Length	验证输入的字符串长度  
- NumberRange	验证输入的值在数字范围内  
- URL	验证URL  
- AnyOf	验证输入值在可选列表中
- NoneOf	验证输入值不在可选列表中  
