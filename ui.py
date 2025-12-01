#!/usr/bin/env python
# -*- coding: gbk -*-
"""
JZ8P2615 代码生成工具 - 用户界面模块
提供图形化配置界面
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext, font
from typing import Optional
import re
import os
from control import ConfigController


class CodeEditor(ttk.Frame):
    """VSCode风格的代码编辑器"""
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        
        # 配置框架
        self.configure(style='CodeEditor.TFrame')
        
        # 行号框架
        self.line_number_frame = tk.Frame(self, bg='#1e1e1e', width=50)
        self.line_number_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.line_number_frame.pack_propagate(False)
        
        # 行号文本
        self.line_number_text = tk.Text(self.line_number_frame, 
                                        width=4, 
                                        bg='#1e1e1e', 
                                        fg='#858585',
                                        font=('Consolas', 11),
                                        padx=5,
                                        pady=5,
                                        state=tk.DISABLED,
                                        wrap=tk.NONE,
                                        relief=tk.FLAT,
                                        borderwidth=0,
                                        highlightthickness=0)
        self.line_number_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 代码文本框架
        text_frame = tk.Frame(self, bg='#1e1e1e')
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 滚动条
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 代码文本
        self.text_widget = tk.Text(text_frame,
                                   bg='#1e1e1e',
                                   fg='#d4d4d4',
                                   font=('Consolas', 11),
                                   padx=10,
                                   pady=5,
                                   wrap=tk.NONE,
                                   relief=tk.FLAT,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   insertbackground='#aeafad',
                                   selectbackground='#264f78',
                                   yscrollcommand=scrollbar.set)
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self._on_scroll)
        
        # 配置标签（用于语法高亮）
        self._setup_tags()
        
        # 绑定事件
        self.text_widget.bind('<KeyRelease>', self._on_text_change)
        self.text_widget.bind('<Button-1>', self._on_click)
        self.text_widget.bind('<MouseWheel>', self._on_mousewheel)
        self.text_widget.bind('<Configure>', lambda e: self._update_line_numbers())
        
        # 初始行号
        self._update_line_numbers()
    
    def _setup_tags(self):
        """设置语法高亮标签"""
        # 关键字（蓝色）
        self.text_widget.tag_config('keyword', foreground='#569cd6')
        # 字符串（橙色）
        self.text_widget.tag_config('string', foreground='#ce9178')
        # 注释（绿色）
        self.text_widget.tag_config('comment', foreground='#6a9955')
        # 数字（浅蓝色）
        self.text_widget.tag_config('number', foreground='#b5cea8')
        # 预处理器（紫色）
        self.text_widget.tag_config('preprocessor', foreground='#c586c0')
        # 函数名（黄色）
        self.text_widget.tag_config('function', foreground='#dcdcaa')
    
    def _on_scroll(self, *args):
        """滚动事件处理"""
        self.text_widget.yview(*args)
        self._update_line_numbers()
    
    def _on_text_change(self, event=None):
        """文本变化事件"""
        self._update_line_numbers()
        self._highlight_syntax()
    
    def _on_click(self, event=None):
        """点击事件"""
        self._update_line_numbers()
    
    def _on_mousewheel(self, event):
        """鼠标滚轮事件"""
        self.text_widget.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self._update_line_numbers()
        return "break"
    
    def _update_line_numbers(self):
        """更新行号"""
        # 获取当前可见行
        first_line = self.text_widget.index("@0,0").split('.')[0]
        last_line = self.text_widget.index("@0,%d" % self.text_widget.winfo_height()).split('.')[0]
        
        # 获取总行数
        total_lines = int(self.text_widget.index('end-1c').split('.')[0])
        
        # 更新行号显示
        self.line_number_text.config(state=tk.NORMAL)
        self.line_number_text.delete(1.0, tk.END)
        
        for i in range(1, total_lines + 1):
            self.line_number_text.insert(tk.END, f"{i}\n")
        
        self.line_number_text.config(state=tk.DISABLED)
        
        # 同步滚动
        self.line_number_text.yview_moveto(self.text_widget.yview()[0])
    
    def _highlight_syntax(self):
        """语法高亮"""
        # 清除所有标签
        for tag in ['keyword', 'string', 'comment', 'number', 'preprocessor', 'function']:
            self.text_widget.tag_remove(tag, 1.0, tk.END)
        
        content = self.text_widget.get(1.0, tk.END)
        lines = content.split('\n')
        
        # 逐行处理
        line_start = 1.0
        for line_num, line in enumerate(lines, 1):
            line_start_index = f"{line_num}.0"
            
            # 高亮注释（单行注释）
            comment_pos = line.find('//')
            if comment_pos != -1:
                comment_start = f"{line_num}.{comment_pos}"
                comment_end = f"{line_num}.end"
                self.text_widget.tag_add('comment', comment_start, comment_end)
            
            # 高亮预处理器指令
            if line.strip().startswith('#'):
                self.text_widget.tag_add('preprocessor', f"{line_num}.0", f"{line_num}.end")
            
            # 高亮字符串
            in_string = False
            string_start = 0
            quote_char = None
            for i, char in enumerate(line):
                if char in ['"', "'"] and (i == 0 or line[i-1] != '\\'):
                    if not in_string:
                        in_string = True
                        string_start = i
                        quote_char = char
                    elif char == quote_char:
                        in_string = False
                        self.text_widget.tag_add('string', f"{line_num}.{string_start}", f"{line_num}.{i+1}")
                elif in_string and i == len(line) - 1:
                    # 字符串跨行（简化处理）
                    self.text_widget.tag_add('string', f"{line_num}.{string_start}", f"{line_num}.end")
            
            # 高亮关键字和数字（在非字符串、非注释区域）
            if '//' not in line or line.find('//') == -1:
                # C语言关键字
                keywords = ['void', 'int', 'char', 'float', 'double', 'if', 'else', 'for', 'while', 
                           'do', 'switch', 'case', 'break', 'continue', 'return', 'include', 'define',
                           'typedef', 'struct', 'enum', 'static', 'extern', 'const', 'volatile',
                           'uint8_t', 'uint16_t', 'uint32_t', 'unsigned', 'signed', 'short', 'long', 'register']
                
                for keyword in keywords:
                    pattern = r'\b' + re.escape(keyword) + r'\b'
                    for match in re.finditer(pattern, line, re.IGNORECASE):
                        start_col = match.start()
                        end_col = match.end()
                        # 检查是否在字符串或注释中
                        if not self._is_in_string_or_comment(line, start_col):
                            self.text_widget.tag_add('keyword', f"{line_num}.{start_col}", f"{line_num}.{end_col}")
                
                # 高亮数字
                for match in re.finditer(r'\b\d+\b', line):
                    if not self._is_in_string_or_comment(line, match.start()):
                        self.text_widget.tag_add('number', f"{line_num}.{match.start()}", f"{line_num}.{match.end()}")
                
                for match in re.finditer(r'\b0x[0-9A-Fa-f]+\b', line, re.IGNORECASE):
                    if not self._is_in_string_or_comment(line, match.start()):
                        self.text_widget.tag_add('number', f"{line_num}.{match.start()}", f"{line_num}.{match.end()}")
                
                # 高亮函数名（单词后跟左括号，且不在字符串中）
                for match in re.finditer(r'\b\w+\s*\(', line):
                    if not self._is_in_string_or_comment(line, match.start()):
                        func_name_end = match.end() - 1  # 不包括左括号
                        self.text_widget.tag_add('function', f"{line_num}.{match.start()}", f"{line_num}.{func_name_end}")
    
    def _is_in_string_or_comment(self, line, pos):
        """检查位置是否在字符串或注释中"""
        # 检查是否在注释中
        comment_pos = line.find('//')
        if comment_pos != -1 and pos >= comment_pos:
            return True
        
        # 检查是否在字符串中（简化版）
        in_string = False
        quote_char = None
        for i, char in enumerate(line):
            if i >= pos:
                break
            if char in ['"', "'"] and (i == 0 or line[i-1] != '\\'):
                if not in_string:
                    in_string = True
                    quote_char = char
                elif char == quote_char:
                    in_string = False
        return in_string
    
    def insert(self, index, text):
        """插入文本"""
        self.text_widget.insert(index, text)
        self._update_line_numbers()
        self._highlight_syntax()
    
    def delete(self, start, end):
        """删除文本"""
        self.text_widget.delete(start, end)
        self._update_line_numbers()
        self._highlight_syntax()
    
    def get(self, start, end):
        """获取文本"""
        return self.text_widget.get(start, end)


class CodeGeneratorUI:
    """代码生成工具主界面"""
    
    def __init__(self, controller: ConfigController):
        """初始化UI"""
        self.controller = controller
        
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("JZ8P2615 代码生成工具 v1.0")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 600)
        
        # 配置样式
        self._setup_styles()
        
        # 创建菜单栏
        self._create_menu()
        
        # 创建工具栏
        self._create_toolbar()
        
        # 创建主界面
        self._create_main_ui()
        
        # 加载默认配置
        self._refresh_ui()
    
    def _setup_styles(self):
        """配置UI样式"""
        style = ttk.Style()
        
        # 尝试使用现代主题
        try:
            style.theme_use('clam')
        except:
            pass
        
        # 配置Treeview样式
        style.configure("Treeview", 
                       background="#ffffff",
                       foreground="#000000",
                       fieldbackground="#ffffff",
                       rowheight=25)
        style.map("Treeview",
                 background=[("selected", "#0078d4")],
                 foreground=[("selected", "#ffffff")])
        
        # 配置按钮样式
        style.configure("Toolbar.TButton", padding=6)
        style.configure("Action.TButton", padding=8)
    
    def _create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="新建配置", command=self._new_config)
        file_menu.add_command(label="打开配置", command=self._open_config)
        file_menu.add_command(label="保存配置", command=self._save_config)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)
        
        # 生成菜单
        generate_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="生成", menu=generate_menu)
        generate_menu.add_command(label="生成初始化代码", command=self._generate_init_code)
        generate_menu.add_command(label="生成主程序", command=self._generate_main_code)
        generate_menu.add_command(label="生成所有代码", command=self._generate_all_code)
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="关于", command=self._show_about)
    
    def _create_toolbar(self):
        """创建工具栏"""
        toolbar = ttk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)
        
        # 快捷按钮
        ttk.Button(toolbar, text="新建", command=self._new_config, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="打开", command=self._open_config,
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="保存", command=self._save_config,
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=2)
        
        # 分隔符
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        # 生成按钮
        ttk.Button(toolbar, text="生成代码", command=self._generate_all_code,
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=2)
        
        # 右侧状态信息
        status_info = ttk.Frame(toolbar)
        status_info.pack(side=tk.RIGHT, padx=5)
        ttk.Label(status_info, text="JZ8P2615", font=("Arial", 9)).pack(side=tk.RIGHT, padx=5)
    
    def _create_main_ui(self):
        """创建主界面"""
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="8")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 配置网格权重（确保中间配置区域有足够空间）
        main_frame.columnconfigure(0, weight=0, minsize=220)
        main_frame.columnconfigure(1, weight=3, minsize=420)
        main_frame.columnconfigure(2, weight=4, minsize=360)
        main_frame.rowconfigure(0, weight=1)
        
        # 左侧：模块选择树形视图
        left_frame = ttk.LabelFrame(main_frame, text="配置模块", padding="8")
        left_frame.grid(row=0, column=0, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 8))
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        
        # 模块树（带滚动条）
        tree_frame = ttk.Frame(left_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        tree_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        self.module_tree = ttk.Treeview(tree_frame, show="tree", yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=self.module_tree.yview)
        
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.module_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 添加模块节点
        modules = [
            ("init", "init.c - 初始化配置"),
            ("main", "main.c - 基础配置"),
            ("adc",  "ADC.c - ADC配置"),
            ("pwm",  "pwm.c - PWM配置"),
            ("sleep", "sleep.c - 睡眠配置"),
            ("isr", "isr.c - 中断服务配置")
        ]
        for module_id, module_name in modules:
            self.module_tree.insert("", tk.END, module_id, text=module_name)
        
        # 绑定选择事件
        self.module_tree.bind("<<TreeviewSelect>>", self._on_module_select)
        
        # 设置默认选中第一个
        if modules:
            self.module_tree.selection_set(modules[0][0])
            self.module_tree.focus(modules[0][0])
        
        # 中间：配置面板
        self.config_frame = ttk.LabelFrame(main_frame, text="配置选项", padding="12")
        self.config_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 8))
        self.config_frame.columnconfigure(0, weight=1)
        self.config_frame.rowconfigure(0, weight=1)
        
        # 配置面板滚动区域
        config_canvas = tk.Canvas(self.config_frame, highlightthickness=0)
        config_scrollbar = ttk.Scrollbar(self.config_frame, orient=tk.VERTICAL, command=config_canvas.yview)
        config_scrollable_frame = ttk.Frame(config_canvas)
        
        config_scrollable_frame.bind(
            "<Configure>",
            lambda e: config_canvas.configure(scrollregion=config_canvas.bbox("all"))
        )
        canvas_window = config_canvas.create_window((0, 0), window=config_scrollable_frame, anchor="nw")
        config_canvas.configure(yscrollcommand=config_scrollbar.set)
        config_canvas.bind(
            "<Configure>",
            lambda e: config_canvas.itemconfig(canvas_window, width=e.width)
        )
        
        config_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        config_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 存储可滚动框架引用
        self.config_scrollable_frame = config_scrollable_frame
        
        # 右侧：代码预览
        right_frame = ttk.LabelFrame(main_frame, text="代码预览", padding="5")
        right_frame.grid(row=0, column=2, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        
        # 代码预览工具栏
        code_toolbar = ttk.Frame(right_frame)
        code_toolbar.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(code_toolbar, text="复制", command=self._copy_code,
                  style="Toolbar.TButton", width=10).pack(side=tk.LEFT, padx=2)
        ttk.Button(code_toolbar, text="导出", command=self._export_code,
                  style="Toolbar.TButton", width=10).pack(side=tk.LEFT, padx=2)
        ttk.Button(code_toolbar, text="刷新", command=self._generate_all_code,
                  style="Toolbar.TButton", width=10).pack(side=tk.LEFT, padx=2)
        
        # 创建VSCode风格的代码编辑器
        self.code_editor = CodeEditor(right_frame)
        self.code_editor.pack(fill=tk.BOTH, expand=True)
        
        # 状态栏
        status_frame = ttk.Frame(self.root)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_label = ttk.Label(status_frame, text="就绪", anchor=tk.W)
        self.status_label.pack(side=tk.LEFT, padx=5)
    
    def _copy_code(self):
        """复制代码到剪贴板"""
        try:
            code = self.code_editor.text_widget.get(1.0, tk.END)
            self.root.clipboard_clear()
            self.root.clipboard_append(code)
            self.status_label.config(text="代码已复制到剪贴板", foreground="#008000")
        except Exception as e:
            self.status_label.config(text=f"复制失败: {e}", foreground="#ff0000")
    
    def _export_code(self):
        """导出代码到文件"""
        if not hasattr(self, 'generated_files') or not self.generated_files:
            messagebox.showwarning("警告", "请先生成代码！")
            return
        
        # 选择导出目录
        export_dir = filedialog.askdirectory(title="选择导出目录")
        if not export_dir:
            return
        
        try:
            exported_count = 0
            for file_name, content in self.generated_files.items():
                file_path = os.path.join(export_dir, file_name)
                with open(file_path, 'w', encoding='gbk') as f:
                    f.write(content)
                exported_count += 1
            
            self.status_label.config(
                text=f"? 已导出 {exported_count} 个文件到: {export_dir}", 
                foreground="#008000"
            )
            messagebox.showinfo("成功", f"已成功导出 {exported_count} 个文件到:\n{export_dir}")
        except Exception as e:
            messagebox.showerror("错误", f"导出文件失败: {e}")
            self.status_label.config(text=f"导出失败: {e}", foreground="#ff0000")
    
    def _on_module_select(self, event):
        """模块选择事件处理"""
        selection = self.module_tree.selection()
        if not selection:
            return
        
        module_id = selection[0]
        self._show_module_config(module_id)
    
    def _show_module_config(self, module_id: str):
        """显示模块配置界面"""
        # 清空配置面板（使用可滚动框架）
        for widget in self.config_scrollable_frame.winfo_children():
            widget.destroy()
        
        # 根据模块ID显示不同的配置界面
        if module_id == "init":
            # init.c 配置 - 使用标签页显示所有配置选项
            self._create_init_all_config_ui()
        elif module_id == "main":
            # main.c / main.h 基础配置
            self._create_main_basic_config_ui()
        elif module_id == "adc":
            # ADC.C / ADC.H 配置（单独模块）
            self._create_adc_init_config_ui()
        elif module_id == "pwm":
            # pwm.c / pwm.h 配置（单独模块）
            self._create_pwm_config_ui()
        elif module_id == "sleep":
            # sleep.c 配置
            self._create_sleep_config_ui()
        elif module_id == "isr":
            # isr.c 配置
            self._create_isr_config_ui()
        else:
            ttk.Label(self.config_scrollable_frame, text="配置界面待实现").pack()
    
    def _create_init_all_config_ui(self):
        """创建init.c的所有配置界面（使用标签页组织）"""
        # 创建主标签页容器
        main_notebook = ttk.Notebook(self.config_scrollable_frame)
        main_notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # GPIO端口配置标签页
        gpio_frame = ttk.Frame(main_notebook, padding="10")
        main_notebook.add(gpio_frame, text="GPIO端口寄存器")
        self._create_gpio_config_content(gpio_frame)
        
        # 定时器寄存器配置标签页
        timer_frame = ttk.Frame(main_notebook, padding="10")
        main_notebook.add(timer_frame, text="定时器寄存器")
        self._create_timer_config_content(timer_frame)
        
        # 中断寄存器配置标签页
        interrupt_frame = ttk.Frame(main_notebook, padding="10")
        main_notebook.add(interrupt_frame, text="中断寄存器")
        self._create_interrupt_register_config_content(interrupt_frame)
    
    def _create_main_basic_config_ui(self):
        """创建 main.c / main.h 的基础配置界面"""
        cfg_timer = self.controller.get_config()["timer"]["TC0"]
        cfg_isr = self.controller.get_config().get("isr", {})
        
        title = ttk.Label(self.config_scrollable_frame, text="main.c / main.h - 基础配置",
                         font=("Arial", 12, "bold"))
        title.pack(anchor=tk.W, pady=(5, 10))
        
        # TCC_NUM 配置（实际存储在 TC0 的 count_value 中）
        tcc_frame = ttk.LabelFrame(self.config_scrollable_frame, text="TC0 计数常量 (TCC_NUM)", padding="10")
        tcc_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(tcc_frame, text="TCC_NUM:").grid(row=0, column=0, sticky=tk.W)
        tcc_var = tk.IntVar(value=cfg_timer["count_value"])
        spin = ttk.Spinbox(tcc_frame, from_=0, to=255, width=10, textvariable=tcc_var)
        spin.grid(row=0, column=1, sticky=tk.W, padx=5)
        tcc_var.trace_add("write",
                          lambda *args: self._update_timer_count("TC0", tcc_var.get()))
        
        ttk.Label(tcc_frame, text="说明: 对应 isr.c 中 TC0C += TCC_NUM 的增量").grid(
            row=1, column=0, columnspan=2, sticky=tk.W, pady=(4, 0))
        
        # 标志变量宏名（与 isr / main.h 联动）
        flag_frame = ttk.LabelFrame(self.config_scrollable_frame, text="时间标志宏 (main.h)", padding="10")
        flag_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(flag_frame, text="10ms 标志宏名:").grid(row=0, column=0, sticky=tk.W, pady=2)
        t10_flag_var = tk.StringVar(value=cfg_isr.get("time_10ms_flag", "Time_10ms"))
        ttk.Entry(flag_frame, textvariable=t10_flag_var, width=20).grid(row=0, column=1, sticky=tk.W, pady=2)
        t10_flag_var.trace_add("write",
                               lambda *args: self._update_isr_config("time_10ms_flag", t10_flag_var.get()))
        
        ttk.Label(flag_frame, text="200us 标志宏名:").grid(row=1, column=0, sticky=tk.W, pady=2)
        t200_flag_var = tk.StringVar(value=cfg_isr.get("time_200us_flag", "Time_200us"))
        ttk.Entry(flag_frame, textvariable=t200_flag_var, width=20).grid(row=1, column=1, sticky=tk.W, pady=2)
        t200_flag_var.trace_add("write",
                                lambda *args: self._update_isr_config("time_200us_flag", t200_flag_var.get()))
        
        desc = ("main.h 中会生成对应的宏，例如:\n"
                "  #define {10ms宏名}   (U_Flage1.SYS_Flg.bit0)\n"
                "  #define {200us宏名}  (U_Flage1.SYS_Flg.bit1)")
        ttk.Label(flag_frame, text=desc, justify=tk.LEFT).grid(
            row=2, column=0, columnspan=2, sticky=tk.W, pady=(4, 0))
    
    def _create_isr_config_ui(self):
        """创建isr.c配置界面"""
        cfg = self.controller.get_config()["isr"]
        
        ttk.Label(self.config_scrollable_frame, text="isr.c - 中断服务程序配置",
                  font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(5, 10))
        
        content_frame = ttk.Frame(self.config_scrollable_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # 10ms计时配置
        block1 = ttk.LabelFrame(content_frame, text="10ms计数配置", padding="10")
        block1.pack(fill=tk.X, padx=5, pady=5)
        
        t10_enable_var = tk.BooleanVar(value=cfg["enable_time_10ms"])
        ttk.Checkbutton(block1, text="启用10ms计时", variable=t10_enable_var,
                        command=lambda: self._update_isr_config("enable_time_10ms", t10_enable_var.get())
                        ).grid(row=0, column=0, sticky=tk.W)
        
        # 计数变量名
        ttk.Label(block1, text="计数变量名:").grid(row=1, column=0, sticky=tk.W, pady=2)
        t10_reg_var = tk.StringVar(value=cfg.get("reg_10ms_name", "reg_10ms"))
        ttk.Entry(block1, textvariable=t10_reg_var, width=20).grid(row=1, column=1, sticky=tk.W, pady=2)
        t10_reg_var.trace_add("write",
                              lambda *args: self._update_isr_config("reg_10ms_name", t10_reg_var.get()))
        
        ttk.Label(block1, text="阈值:").grid(row=2, column=0, sticky=tk.W, pady=2)
        t10_threshold_var = tk.IntVar(value=cfg["time_10ms_threshold"])
        t10_spin = ttk.Spinbox(block1, from_=1, to=1000, width=10,
                               textvariable=t10_threshold_var)
        t10_spin.grid(row=2, column=1, sticky=tk.W, pady=2)
        t10_threshold_var.trace_add("write",
                                    lambda *args: self._update_isr_int_var("time_10ms_threshold", t10_threshold_var))
        
        ttk.Label(block1, text="标志变量:").grid(row=3, column=0, sticky=tk.W, pady=2)
        t10_flag_var = tk.StringVar(value=cfg["time_10ms_flag"])
        ttk.Entry(block1, textvariable=t10_flag_var, width=20).grid(row=3, column=1, sticky=tk.W, pady=2)
        t10_flag_var.trace_add("write",
                               lambda *args: self._update_isr_config("time_10ms_flag", t10_flag_var.get()))
        
        # 200us计时配置
        block2 = ttk.LabelFrame(content_frame, text="200us计数配置", padding="10")
        block2.pack(fill=tk.X, padx=5, pady=5)
        
        t200_enable_var = tk.BooleanVar(value=cfg["enable_time_200us"])
        ttk.Checkbutton(block2, text="启用200us计时", variable=t200_enable_var,
                        command=lambda: self._update_isr_config("enable_time_200us", t200_enable_var.get())
                        ).grid(row=0, column=0, sticky=tk.W)
        
        # 计数变量名
        ttk.Label(block2, text="计数变量名:").grid(row=1, column=0, sticky=tk.W, pady=2)
        t200_reg_var = tk.StringVar(value=cfg.get("reg_200us_name", "reg_200us"))
        ttk.Entry(block2, textvariable=t200_reg_var, width=20).grid(row=1, column=1, sticky=tk.W, pady=2)
        t200_reg_var.trace_add("write",
                               lambda *args: self._update_isr_config("reg_200us_name", t200_reg_var.get()))
        
        ttk.Label(block2, text="阈值:").grid(row=2, column=0, sticky=tk.W, pady=2)
        t200_threshold_var = tk.IntVar(value=cfg["time_200us_threshold"])
        t200_spin = ttk.Spinbox(block2, from_=1, to=1000, width=10,
                                textvariable=t200_threshold_var)
        t200_spin.grid(row=2, column=1, sticky=tk.W, pady=2)
        t200_threshold_var.trace_add("write",
                                     lambda *args: self._update_isr_int_var("time_200us_threshold", t200_threshold_var))
        
        ttk.Label(block2, text="标志变量:").grid(row=3, column=0, sticky=tk.W, pady=2)
        t200_flag_var = tk.StringVar(value=cfg["time_200us_flag"])
        ttk.Entry(block2, textvariable=t200_flag_var, width=20).grid(row=3, column=1, sticky=tk.W, pady=2)
        t200_flag_var.trace_add("write",
                                lambda *args: self._update_isr_config("time_200us_flag", t200_flag_var.get()))
        
        # 这里只配置计数和标志变量，暂不包含显示扫描相关配置
    
    def _create_sleep_config_ui(self):
        """创建sleep.c配置界面"""
        cfg = self.controller.get_config()["sleep"]
        
        ttk.Label(self.config_scrollable_frame, text="sleep.c - 睡眠配置",
                  font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(5, 10))
        
        enable_var = tk.BooleanVar(value=cfg["enabled"])
        ttk.Checkbutton(self.config_scrollable_frame, text="启用睡眠功能", variable=enable_var,
                       command=lambda: self._update_sleep_config("enabled", enable_var.get())
                       ).pack(anchor=tk.W, padx=5, pady=5)
        
        block = ttk.LabelFrame(self.config_scrollable_frame, text="睡眠参数", padding="10")
        block.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(block, text="计数变量名:").grid(row=0, column=0, sticky=tk.W, pady=2)
        counter_var = tk.StringVar(value=cfg["counter_name"])
        ttk.Entry(block, textvariable=counter_var, width=20).grid(row=0, column=1, sticky=tk.W, pady=2)
        counter_var.trace_add("write",
                              lambda *args: self._update_sleep_config("counter_name", counter_var.get()))
        
        ttk.Label(block, text="阈值:").grid(row=1, column=0, sticky=tk.W, pady=2)
        threshold_var = tk.IntVar(value=cfg["threshold"])
        ttk.Spinbox(block, from_=1, to=255, width=10,
                    textvariable=threshold_var).grid(row=1, column=1, sticky=tk.W, pady=2)
        threshold_var.trace_add("write",
                                lambda *args: self._update_sleep_config("threshold", threshold_var.get()))
        
        ttk.Label(block, text="进入睡眠条件表达式:").grid(row=2, column=0, sticky=tk.W, pady=2)
        condition_var = tk.StringVar(value=cfg["condition"])
        ttk.Entry(block, textvariable=condition_var, width=50).grid(row=2, column=1, sticky=tk.W, pady=2)
        condition_var.trace_add("write",
                                lambda *args: self._update_sleep_config("condition", condition_var.get()))
        
        wake_frame = ttk.LabelFrame(self.config_scrollable_frame, text="唤醒端口", padding="10")
        wake_frame.pack(fill=tk.X, padx=5, pady=5)
        wake_ports = cfg.get("wake_ports", ["P6"])
        
        p5_var = tk.BooleanVar(value="P5" in wake_ports)
        ttk.Checkbutton(wake_frame, text="P5 端口唤醒", variable=p5_var,
                        command=lambda: self._update_sleep_wake_port("P5", p5_var.get())
                        ).grid(row=0, column=0, sticky=tk.W, pady=2)
        
        p6_var = tk.BooleanVar(value="P6" in wake_ports)
        ttk.Checkbutton(wake_frame, text="P6 端口唤醒", variable=p6_var,
                        command=lambda: self._update_sleep_wake_port("P6", p6_var.get())
                        ).grid(row=0, column=1, sticky=tk.W, pady=2)
    
    def _create_gpio_config_content(self, parent):
        """创建GPIO配置内容（用于标签页）"""
        # 创建Notebook用于切换P5和P6
        notebook = ttk.Notebook(parent)
        notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # P5端口配置
        p5_frame = ttk.Frame(notebook, padding="10")
        notebook.add(p5_frame, text="P5端口")
        self._create_port_config_ui(p5_frame, "P5")
        
        # P6端口配置
        p6_frame = ttk.Frame(notebook, padding="10")
        notebook.add(p6_frame, text="P6端口")
        self._create_port_config_ui(p6_frame, "P6", is_p6=True)
    
    def _create_gpio_config_ui(self):
        """创建GPIO配置界面（保留用于兼容）"""
        # 清空配置面板
        for widget in self.config_scrollable_frame.winfo_children():
            widget.destroy()
        
        # 标题
        title = ttk.Label(self.config_scrollable_frame, text="GPIO端口配置", 
                         font=("Arial", 12, "bold"))
        title.pack(pady=(5, 10))
        
        # 创建Notebook用于切换P5和P6
        notebook = ttk.Notebook(self.config_scrollable_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # P5端口配置
        p5_frame = ttk.Frame(notebook, padding="10")
        notebook.add(p5_frame, text="P5端口")
        self._create_port_config_ui(p5_frame, "P5")
        
        # P6端口配置
        p6_frame = ttk.Frame(notebook, padding="10")
        notebook.add(p6_frame, text="P6端口")
        self._create_port_config_ui(p6_frame, "P6", is_p6=True)
    
    def _create_port_config_ui(self, parent, port_name, is_p6=False):
        """创建端口配置界面"""
        config = self.controller.get_config()["gpio"][port_name]
        
        # 创建表格框架
        table_frame = ttk.Frame(parent)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # 表头
        headers = ["引脚", "方向", "上拉", "下拉"]
        if is_p6:
            headers.extend(["开漏", "弱驱动"])
        headers.append("唤醒")
        
        for i, header in enumerate(headers):
            label = ttk.Label(table_frame, text=header, font=("Arial", 10, "bold"))
            label.grid(row=0, column=i, padx=5, pady=5, sticky=tk.W)
        
        # 存储控件引用
        if not hasattr(self, 'gpio_widgets'):
            self.gpio_widgets = {}
        if port_name not in self.gpio_widgets:
            self.gpio_widgets[port_name] = {}
        
        # 为每个引脚创建配置控件
        for pin in range(8):
            row = pin + 1
            pin_name = f"{port_name}{pin}"
            
            # 引脚名称
            ttk.Label(table_frame, text=pin_name).grid(row=row, column=0, padx=5, pady=2)
            
            # 方向选择（输入/输出）
            direction_var = tk.StringVar(value="输出" if config["direction"][pin] == 0 else "输入")
            direction_combo = ttk.Combobox(table_frame, textvariable=direction_var, 
                                          values=["输出", "输入"], state="readonly", width=8)
            direction_combo.grid(row=row, column=1, padx=5, pady=2)
            direction_combo.bind("<<ComboboxSelected>>", 
                               lambda e, p=pin, port=port_name: self._update_gpio_direction(p, port, e))
            self.gpio_widgets[port_name][f"direction_{pin}"] = direction_combo
            
            # 上拉使能
            pullup_var = tk.BooleanVar(value=config["pullup"][pin] == 0)
            pullup_check = ttk.Checkbutton(table_frame, variable=pullup_var,
                                          command=lambda p=pin, port=port_name: 
                                          self._update_gpio_pullup(p, port))
            pullup_check.grid(row=row, column=2, padx=5, pady=2)
            self.gpio_widgets[port_name][f"pullup_{pin}"] = pullup_var
            
            # 下拉使能
            pulldown_var = tk.BooleanVar(value=config["pulldown"][pin] == 0)
            pulldown_check = ttk.Checkbutton(table_frame, variable=pulldown_var,
                                           command=lambda p=pin, port=port_name: 
                                           self._update_gpio_pulldown(p, port))
            pulldown_check.grid(row=row, column=3, padx=5, pady=2)
            self.gpio_widgets[port_name][f"pulldown_{pin}"] = pulldown_var
            
            # P6特有：开漏和弱驱动
            if is_p6:
                # 开漏使能
                opendrain_var = tk.BooleanVar(value=config["opendrain"][pin] == 1)
                opendrain_check = ttk.Checkbutton(table_frame, variable=opendrain_var,
                                                 command=lambda p=pin, port=port_name: 
                                                 self._update_gpio_opendrain(p, port))
                opendrain_check.grid(row=row, column=4, padx=5, pady=2)
                self.gpio_widgets[port_name][f"opendrain_{pin}"] = opendrain_var
                
                # 弱驱动使能
                weakdrive_var = tk.BooleanVar(value=config["weakdrive"][pin] == 1)
                weakdrive_check = ttk.Checkbutton(table_frame, variable=weakdrive_var,
                                                 command=lambda p=pin, port=port_name: 
                                                 self._update_gpio_weakdrive(p, port))
                weakdrive_check.grid(row=row, column=5, padx=5, pady=2)
                self.gpio_widgets[port_name][f"weakdrive_{pin}"] = weakdrive_var
                
                # 唤醒使能
                wakeup_var = tk.BooleanVar(value=config["wakeup"][pin] == 1)
                wakeup_check = ttk.Checkbutton(table_frame, variable=wakeup_var,
                                             command=lambda p=pin, port=port_name: 
                                             self._update_gpio_wakeup(p, port))
                wakeup_check.grid(row=row, column=6, padx=5, pady=2)
                self.gpio_widgets[port_name][f"wakeup_{pin}"] = wakeup_var
            else:
                # P5唤醒使能
                wakeup_var = tk.BooleanVar(value=config["wakeup"][pin] == 1)
                wakeup_check = ttk.Checkbutton(table_frame, variable=wakeup_var,
                                             command=lambda p=pin, port=port_name: 
                                             self._update_gpio_wakeup(p, port))
                wakeup_check.grid(row=row, column=4, padx=5, pady=2)
                self.gpio_widgets[port_name][f"wakeup_{pin}"] = wakeup_var
    
    def _update_gpio_direction(self, pin, port, event):
        """更新GPIO方向配置"""
        widget = self.gpio_widgets[port][f"direction_{pin}"]
        value = 1 if widget.get() == "输入" else 0
        self.controller.config_data["gpio"][port]["direction"][pin] = value
    
    def _update_gpio_pullup(self, pin, port):
        """更新GPIO上拉配置"""
        var = self.gpio_widgets[port][f"pullup_{pin}"]
        value = 0 if var.get() else 1  # 0=使能, 1=禁止
        self.controller.config_data["gpio"][port]["pullup"][pin] = value
    
    def _update_gpio_pulldown(self, pin, port):
        """更新GPIO下拉配置"""
        var = self.gpio_widgets[port][f"pulldown_{pin}"]
        value = 0 if var.get() else 1  # 0=使能, 1=禁止
        self.controller.config_data["gpio"][port]["pulldown"][pin] = value
    
    def _update_gpio_opendrain(self, pin, port):
        """更新GPIO开漏配置"""
        var = self.gpio_widgets[port][f"opendrain_{pin}"]
        value = 1 if var.get() else 0  # 0=禁止, 1=使能
        self.controller.config_data["gpio"][port]["opendrain"][pin] = value
    
    def _update_gpio_weakdrive(self, pin, port):
        """更新GPIO弱驱动配置"""
        var = self.gpio_widgets[port][f"weakdrive_{pin}"]
        value = 1 if var.get() else 0  # 0=禁止, 1=使能
        self.controller.config_data["gpio"][port]["weakdrive"][pin] = value
    
    def _update_gpio_wakeup(self, pin, port):
        """更新GPIO唤醒配置"""
        var = self.gpio_widgets[port][f"wakeup_{pin}"]
        value = 1 if var.get() else 0  # 0=禁止, 1=使能
        self.controller.config_data["gpio"][port]["wakeup"][pin] = value
    
    def _create_adc_init_config_content(self, parent):
        """创建ADC初始化配置内容（用于标签页）"""
        info_label = ttk.Label(parent, 
                              text="配置 P5ADE, P6ADE, ADCON0, ADCON1",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        config = self.controller.get_config()["adc"]
        
        # ADC使能
        adc_enable_var = tk.BooleanVar(value=config["enabled"])
        ttk.Checkbutton(parent, text="使能ADC", variable=adc_enable_var,
                       command=lambda: self._update_adc_enabled(adc_enable_var)).pack(anchor=tk.W, padx=10, pady=5)
        
        # 参考电压选择
        ttk.Label(parent, text="参考电压:").pack(anchor=tk.W, padx=10, pady=5)
        vref_var = tk.StringVar(value=config["reference"])
        vref_combo = ttk.Combobox(parent, textvariable=vref_var,
                                 values=["VDD", "4V", "3V", "2V", "1.5V"], 
                                 state="readonly", width=15)
        vref_combo.pack(anchor=tk.W, padx=30, pady=2)
        vref_combo.bind("<<ComboboxSelected>>", 
                       lambda e: self._update_adc_reference(vref_var.get()))
        
        # 时钟分频选择
        ttk.Label(parent, text="时钟分频:").pack(anchor=tk.W, padx=10, pady=5)
        clkdiv_var = tk.StringVar(value=config["clock_div"])
        clkdiv_combo = ttk.Combobox(parent, textvariable=clkdiv_var,
                                   values=["Fosc/1", "Fosc/4", "Fosc/16", "Fosc/64"],
                                   state="readonly", width=15)
        clkdiv_combo.pack(anchor=tk.W, padx=30, pady=2)
        clkdiv_combo.bind("<<ComboboxSelected>>",
                         lambda e: self._update_adc_clockdiv(clkdiv_var.get()))
        
        # 校准使能
        calib_var = tk.BooleanVar(value=config["calibration"])
        ttk.Checkbutton(parent, text="使能校准", variable=calib_var,
                       command=lambda: self._update_adc_calibration(calib_var)).pack(anchor=tk.W, padx=10, pady=5)
        
        # ADC通道选择
        ttk.Label(parent, text="ADC通道选择:").pack(anchor=tk.W, padx=10, pady=5)
        channel_frame = ttk.Frame(parent)
        channel_frame.pack(anchor=tk.W, padx=30, pady=2)
        
        channels = config.get("channels", [])
        channel_vars = {}
        for ch in range(14):
            var = tk.BooleanVar(value=ch in channels)
            channel_vars[ch] = var
            ch_name = f"AD{ch}"
            if ch < 6:
                ch_name += f" (P5{ch})"
            else:
                ch_name += f" (P6{ch-6})"
            ttk.Checkbutton(channel_frame, text=ch_name, variable=var,
                           command=lambda c=ch: self._update_adc_channels()).grid(
                           row=ch//7, column=ch%7, padx=5, pady=2, sticky=tk.W)
        
        if not hasattr(self, 'adc_widgets'):
            self.adc_widgets = {}
        self.adc_widgets['channels'] = channel_vars
        self.adc_widgets['enabled'] = adc_enable_var
        self.adc_widgets['reference'] = vref_var
        self.adc_widgets['clock_div'] = clkdiv_var
        self.adc_widgets['calibration'] = calib_var
    
    def _create_adc_init_config_ui(self):
        """创建ADC初始化配置界面（保留用于兼容）"""
        for widget in self.config_scrollable_frame.winfo_children():
            widget.destroy()
        
        # 标题
        title_frame = ttk.Frame(self.config_scrollable_frame)
        title_frame.pack(fill=tk.X, pady=(5, 10))
        
        title = ttk.Label(title_frame, text="init.c - ADC初始化寄存器配置", 
                         font=("Arial", 12, "bold"))
        title.pack(side=tk.LEFT)
        
        self._create_adc_init_config_content(self.config_scrollable_frame)
    
    def _update_adc_enabled(self, var):
        """更新ADC使能状态"""
        self.controller.config_data["adc"]["enabled"] = var.get()
    
    def _update_adc_reference(self, value):
        """更新ADC参考电压"""
        self.controller.config_data["adc"]["reference"] = value
    
    def _update_adc_clockdiv(self, value):
        """更新ADC时钟分频"""
        self.controller.config_data["adc"]["clock_div"] = value
    
    def _update_adc_calibration(self, var):
        """更新ADC校准使能"""
        self.controller.config_data["adc"]["calibration"] = var.get()
    
    def _update_adc_channels(self):
        """更新ADC通道选择"""
        channels = []
        for ch, var in self.adc_widgets['channels'].items():
            if var.get():
                channels.append(ch)
        self.controller.config_data["adc"]["channels"] = channels
    
    def _create_timer_config_content(self, parent):
        """创建定时器配置内容（用于标签页）"""
        info_label = ttk.Label(parent, 
                              text="配置 TC0CON, TC0C, TC1, TC2等",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        # 创建Notebook用于切换不同定时器
        notebook = ttk.Notebook(parent)
        notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # TC0配置
        tc0_frame = ttk.Frame(notebook, padding="10")
        notebook.add(tc0_frame, text="TC0")
        self._create_tc0_config_ui(tc0_frame)
        
        # TC1配置
        tc1_frame = ttk.Frame(notebook, padding="10")
        notebook.add(tc1_frame, text="TC1")
        self._create_tc1_config_ui(tc1_frame)
        
        # TC2配置
        tc2_frame = ttk.Frame(notebook, padding="10")
        notebook.add(tc2_frame, text="TC2")
        self._create_tc2_config_ui(tc2_frame)
    
    def _create_timer_config_ui(self):
        """创建定时器配置界面（保留用于兼容）"""
        for widget in self.config_scrollable_frame.winfo_children():
            widget.destroy()
        
        # 标题
        title_frame = ttk.Frame(self.config_scrollable_frame)
        title_frame.pack(fill=tk.X, pady=(5, 10))
        
        title = ttk.Label(title_frame, text="init.c - 定时器寄存器配置", 
                         font=("Arial", 12, "bold"))
        title.pack(side=tk.LEFT)
        
        self._create_timer_config_content(self.config_scrollable_frame)
    
    def _create_tc0_config_ui(self, parent):
        """创建TC0配置界面"""
        config = self.controller.get_config()["timer"]["TC0"]
        
        # 使能
        enable_var = tk.BooleanVar(value=config["enabled"])
        ttk.Checkbutton(parent, text="使能TC0", variable=enable_var,
                       command=lambda: self._update_timer_enabled("TC0", enable_var)).pack(anchor=tk.W, pady=5)
        
        # 时钟源
        ttk.Label(parent, text="时钟源:").pack(anchor=tk.W, pady=5)
        clk_var = tk.StringVar(value=config["clock_source"])
        clk_combo = ttk.Combobox(parent, textvariable=clk_var,
                                values=["system", "instruction", "external"],
                                state="readonly", width=15)
        clk_combo.pack(anchor=tk.W, padx=20, pady=2)
        clk_combo.bind("<<ComboboxSelected>>",
                      lambda e: self._update_timer_clock_source("TC0", clk_var.get()))
        
        # 分频器
        ttk.Label(parent, text="分频器 (TCOPSR<2:0>):").pack(anchor=tk.W, pady=5)
        prescaler_var = tk.IntVar(value=config["prescaler"])
        prescaler_map = {0: "1:2", 1: "1:4", 2: "1:8", 3: "1:16", 
                         4: "1:32", 5: "1:64", 6: "1:128", 7: "1:256"}
        
        prescaler_frame = ttk.Frame(parent)
        prescaler_frame.pack(anchor=tk.W, padx=20, pady=2, fill=tk.X)
        prescaler_spin = ttk.Spinbox(prescaler_frame, from_=0, to=7, textvariable=prescaler_var,
                                    width=10, command=lambda: 
                                    self._update_timer_prescaler("TC0", prescaler_var.get()))
        prescaler_spin.pack(side=tk.LEFT)
        
        def update_prescaler_label(*args):
            val = prescaler_var.get()
            prescaler_label.config(text=f"分频系数: {prescaler_map[val]}")
        
        prescaler_var.trace('w', update_prescaler_label)
        prescaler_label = ttk.Label(prescaler_frame, text=f"分频系数: {prescaler_map[prescaler_var.get()]}")
        prescaler_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # 显示映射表
        map_text = "映射: 0=2分频, 1=4分频, 2=8分频, 3=16分频, 4=32分频, 5=64分频, 6=128分频, 7=256分频"
        ttk.Label(parent, text=map_text, font=("TkDefaultFont", 8), foreground="gray").pack(anchor=tk.W, padx=20, pady=2)
        
        # 计数值
        ttk.Label(parent, text="计数值:").pack(anchor=tk.W, pady=5)
        count_var = tk.IntVar(value=config["count_value"])
        count_spin = ttk.Spinbox(parent, from_=0, to=255, textvariable=count_var,
                                width=10, command=lambda:
                                self._update_timer_count("TC0", count_var.get()))
        count_spin.pack(anchor=tk.W, padx=20, pady=2)
        
        # 中断使能
        int_var = tk.BooleanVar(value=config["interrupt"])
        ttk.Checkbutton(parent, text="使能中断", variable=int_var,
                       command=lambda: self._update_timer_interrupt("TC0", int_var)).pack(anchor=tk.W, pady=5)
    
    def _create_tc1_config_ui(self, parent):
        """创建TC1配置界面"""
        config = self.controller.get_config()["timer"]["TC1"]
        
        enable_var = tk.BooleanVar(value=config["enabled"])
        ttk.Checkbutton(parent, text="使能TC1", variable=enable_var,
                       command=lambda: self._update_timer_enabled("TC1", enable_var)).pack(anchor=tk.W, pady=5)
        
        ttk.Label(parent, text="模式:").pack(anchor=tk.W, pady=5)
        mode_var = tk.StringVar(value=config["mode"])
        mode_combo = ttk.Combobox(parent, textvariable=mode_var,
                                  values=["10bit", "20bit"],
                                  state="readonly", width=15)
        mode_combo.pack(anchor=tk.W, padx=20, pady=2)
        mode_combo.bind("<<ComboboxSelected>>",
                       lambda e: self._update_timer_mode("TC1", mode_var.get()))
        
        ttk.Label(parent, text="周期:").pack(anchor=tk.W, pady=5)
        period_var = tk.IntVar(value=config["period"])
        period_spin = ttk.Spinbox(parent, from_=0, to=65535, textvariable=period_var,
                                 width=10, command=lambda:
                                 self._update_timer_period("TC1", period_var.get()))
        period_spin.pack(anchor=tk.W, padx=20, pady=2)
        
        pwm_var = tk.BooleanVar(value=config["pwm_enabled"])
        ttk.Checkbutton(parent, text="关联PWM", variable=pwm_var,
                       command=lambda: self._update_timer_pwm("TC1", pwm_var)).pack(anchor=tk.W, pady=5)
        
        int_var = tk.BooleanVar(value=config["interrupt"])
        ttk.Checkbutton(parent, text="使能中断", variable=int_var,
                       command=lambda: self._update_timer_interrupt("TC1", int_var)).pack(anchor=tk.W, pady=5)
    
    def _create_tc2_config_ui(self, parent):
        """创建TC2配置界面"""
        config = self.controller.get_config()["timer"]["TC2"]
        
        enable_var = tk.BooleanVar(value=config["enabled"])
        ttk.Checkbutton(parent, text="使能TC2", variable=enable_var,
                       command=lambda: self._update_timer_enabled("TC2", enable_var)).pack(anchor=tk.W, pady=5)
        
        ttk.Label(parent, text="模式:").pack(anchor=tk.W, pady=5)
        mode_var = tk.StringVar(value=config["mode"])
        mode_combo = ttk.Combobox(parent, textvariable=mode_var,
                                  values=["10bit", "20bit"],
                                  state="readonly", width=15)
        mode_combo.pack(anchor=tk.W, padx=20, pady=2)
        mode_combo.bind("<<ComboboxSelected>>",
                       lambda e: self._update_timer_mode("TC2", mode_var.get()))
        
        ttk.Label(parent, text="周期:").pack(anchor=tk.W, pady=5)
        period_var = tk.IntVar(value=config["period"])
        period_spin = ttk.Spinbox(parent, from_=0, to=65535, textvariable=period_var,
                                 width=10, command=lambda:
                                 self._update_timer_period("TC2", period_var.get()))
        period_spin.pack(anchor=tk.W, padx=20, pady=2)
        
        pwm_var = tk.BooleanVar(value=config["pwm_enabled"])
        ttk.Checkbutton(parent, text="关联PWM", variable=pwm_var,
                       command=lambda: self._update_timer_pwm("TC2", pwm_var)).pack(anchor=tk.W, pady=5)
        
        int_var = tk.BooleanVar(value=config["interrupt"])
        ttk.Checkbutton(parent, text="使能中断", variable=int_var,
                       command=lambda: self._update_timer_interrupt("TC2", int_var)).pack(anchor=tk.W, pady=5)
    
    def _update_timer_enabled(self, timer, var):
        """更新定时器使能"""
        self.controller.config_data["timer"][timer]["enabled"] = var.get()
    
    def _update_timer_clock_source(self, timer, value):
        """更新定时器时钟源"""
        self.controller.config_data["timer"][timer]["clock_source"] = value
    
    def _update_timer_prescaler(self, timer, value):
        """更新定时器分频器"""
        self.controller.config_data["timer"][timer]["prescaler"] = value
    
    def _update_timer_count(self, timer, value):
        """更新定时器计数值"""
        self.controller.config_data["timer"][timer]["count_value"] = value
    
    def _update_timer_mode(self, timer, value):
        """更新定时器模式"""
        self.controller.config_data["timer"][timer]["mode"] = value
    
    def _update_timer_period(self, timer, value):
        """更新定时器周期"""
        self.controller.config_data["timer"][timer]["period"] = value
    
    def _update_timer_pwm(self, timer, var):
        """更新定时器PWM关联"""
        self.controller.config_data["timer"][timer]["pwm_enabled"] = var.get()
    
    def _update_timer_interrupt(self, timer, var):
        """更新定时器中断使能"""
        self.controller.config_data["timer"][timer]["interrupt"] = var.get()
    
    def _create_pwm_config_content(self, parent):
        """创建PWM配置内容（用于标签页）"""
        info_label = ttk.Label(parent, 
                              text="配置 PWM相关寄存器",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        config = self.controller.get_config()["pwm"]
        
        # 创建表格
        table_frame = ttk.Frame(parent)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 表头
        headers = ["PWM通道", "使能", "周期(TCxPRD)", "占空比(%)", "输出引脚映射", "PWM时钟"]
        for i, header in enumerate(headers):
            ttk.Label(table_frame, text=header, font=("Arial", 10, "bold")).grid(
                row=0, column=i, padx=10, pady=5)
        
        # PWM通道配置
        clock_display_map = {"instruction": "指令周期", "system": "系统时钟"}
        reverse_clock_map = {v: k for k, v in clock_display_map.items()}
        
        for idx, pwm_name in enumerate(["PWM1", "PWM2", "PWM3", "PWM4"], 1):
            row = idx
            pwm_config = config[pwm_name]
            
            # 通道名
            ttk.Label(table_frame, text=pwm_name).grid(row=row, column=0, padx=10, pady=5)
            
            # 使能
            enable_var = tk.BooleanVar(value=pwm_config["enabled"])
            ttk.Checkbutton(table_frame, variable=enable_var,
                           command=lambda p=pwm_name, v=enable_var: 
                           self._update_pwm_enabled(p, v)).grid(row=row, column=1, padx=10, pady=5)

            # 周期
            period_var = tk.IntVar(value=pwm_config["period"])
            period_spin = ttk.Spinbox(
                table_frame,
                from_=0,
                to=1023,
                textvariable=period_var,
                width=10,
            )
            period_spin.grid(row=row, column=2, padx=10, pady=5)
            # 通过 trace 保证键盘输入也能实时更新配置
            period_var.trace_add(
                "write",
                lambda *args, p=pwm_name, v=period_var: self._update_pwm_period(p, v.get()),
            )

            # 占空比
            duty_var = tk.IntVar(value=pwm_config["duty"])
            duty_spin = ttk.Spinbox(
                table_frame,
                from_=0,
                to=100,
                textvariable=duty_var,
                width=10,
            )
            duty_spin.grid(row=row, column=3, padx=10, pady=5)
            duty_var.trace_add(
                "write",
                lambda *args, p=pwm_name, v=duty_var: self._update_pwm_duty(p, v.get()),
            )

            # 引脚映射（依据数据手册 PWMIS 配置）
            if pwm_name == "PWM1":
                options = ["P60", "P52"]
            elif pwm_name == "PWM2":
                options = ["P61", "P53"]
            elif pwm_name == "PWM3":
                options = ["P62", "P54"]
            else:  # PWM4
                options = ["P63", "P55"]

            mapping_var = tk.StringVar(value=pwm_config.get("mapping", options[0]))
            mapping_combo = ttk.Combobox(
                table_frame,
                textvariable=mapping_var,
                values=options,
                state="readonly",
                width=8,
            )
            mapping_combo.grid(row=row, column=4, padx=10, pady=5)
            mapping_combo.bind(
                "<<ComboboxSelected>>",
                lambda e, p=pwm_name, v=mapping_var: self._update_pwm_mapping(p, v.get()),
            )
            
            clock_key = pwm_config.get("clock_source", "instruction")
            clock_var = tk.StringVar(value=clock_display_map.get(clock_key, "指令周期"))
            clock_combo = ttk.Combobox(
                table_frame,
                textvariable=clock_var,
                values=list(clock_display_map.values()),
                state="readonly",
                width=10,
            )
            clock_combo.grid(row=row, column=5, padx=10, pady=5)
            clock_combo.bind(
                "<<ComboboxSelected>>",
                lambda e, p=pwm_name, cv=clock_var: self._update_pwm_clock_source(p, reverse_clock_map.get(cv.get(), "instruction")),
            )
    
    def _create_pwm_config_ui(self):
        """创建PWM配置界面（保留用于兼容）"""
        for widget in self.config_scrollable_frame.winfo_children():
            widget.destroy()
        
        # 标题
        title_frame = ttk.Frame(self.config_scrollable_frame)
        title_frame.pack(fill=tk.X, pady=(5, 10))
        
        title = ttk.Label(title_frame, text="init.c - PWM初始化寄存器配置", 
                         font=("Arial", 12, "bold"))
        title.pack(side=tk.LEFT)
        
        self._create_pwm_config_content(self.config_scrollable_frame)
    
    def _update_pwm_enabled(self, pwm, var):
        """更新PWM使能"""
        self.controller.config_data["pwm"][pwm]["enabled"] = var.get()
    
    def _update_pwm_period(self, pwm, value):
        """更新PWM周期"""
        self.controller.config_data["pwm"][pwm]["period"] = value
    
    def _update_pwm_duty(self, pwm, value):
        """更新PWM占空比"""
        self.controller.config_data["pwm"][pwm]["duty"] = value
    
    def _update_pwm_mapping(self, pwm, pin):
        """更新PWM输出引脚映射"""
        self.controller.config_data["pwm"][pwm]["mapping"] = pin
    
    def _update_pwm_clock_source(self, pwm, clock_key):
        """更新PWM时钟源（PWMCON Bit6）"""
        self.controller.config_data["pwm"][pwm]["clock_source"] = clock_key
    
    def _create_interrupt_config_content(self, parent):
        """创建中断配置内容（用于标签页）"""
        info_label = ttk.Label(parent, 
                              text="配置 INTE0, INTE1, INTF0, INTF1, WDTCON",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        config = self.controller.get_config()["interrupt"]
        
        # 外部中断配置
        ext_frame = ttk.LabelFrame(parent, text="外部中断", padding="10")
        ext_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # INT0
        int0_frame = ttk.Frame(ext_frame)
        int0_frame.pack(fill=tk.X, pady=2)
        int0_enable_var = tk.BooleanVar(value=config["INT0"]["enabled"])
        ttk.Checkbutton(int0_frame, text="INT0 (P60)", variable=int0_enable_var,
                       command=lambda: self._update_int_enabled("INT0", int0_enable_var)).pack(side=tk.LEFT, padx=5)
        int0_edge_var = tk.StringVar(value=config["INT0"]["edge"])
        ttk.Label(int0_frame, text="触发边沿:").pack(side=tk.LEFT, padx=5)
        ttk.Combobox(int0_frame, textvariable=int0_edge_var, values=["rising", "falling"],
                    state="readonly", width=10).pack(side=tk.LEFT, padx=5)
        int0_edge_var.trace("w", lambda *args: self._update_int_edge("INT0", int0_edge_var.get()))
        
        # INT1
        int1_frame = ttk.Frame(ext_frame)
        int1_frame.pack(fill=tk.X, pady=2)
        int1_enable_var = tk.BooleanVar(value=config["INT1"]["enabled"])
        ttk.Checkbutton(int1_frame, text="INT1 (P53)", variable=int1_enable_var,
                       command=lambda: self._update_int_enabled("INT1", int1_enable_var)).pack(side=tk.LEFT, padx=5)
        int1_edge_var = tk.StringVar(value=config["INT1"]["edge"])
        ttk.Label(int1_frame, text="触发边沿:").pack(side=tk.LEFT, padx=5)
        ttk.Combobox(int1_frame, textvariable=int1_edge_var, values=["rising", "falling"],
                    state="readonly", width=10).pack(side=tk.LEFT, padx=5)
        int1_edge_var.trace("w", lambda *args: self._update_int_edge("INT1", int1_edge_var.get()))
        
        # 端口变化中断
        port_frame = ttk.LabelFrame(parent, text="端口变化中断", padding="10")
        port_frame.pack(fill=tk.X, padx=10, pady=5)
        
        p5_var = tk.BooleanVar(value=config["port_change"]["P5"])
        ttk.Checkbutton(port_frame, text="P5端口变化中断", variable=p5_var,
                       command=lambda: self._update_port_change("P5", p5_var)).pack(anchor=tk.W, pady=2)
        
        p6_var = tk.BooleanVar(value=config["port_change"]["P6"])
        ttk.Checkbutton(port_frame, text="P6端口变化中断", variable=p6_var,
                       command=lambda: self._update_port_change("P6", p6_var)).pack(anchor=tk.W, pady=2)
    
    def _create_interrupt_config_ui(self):
        """创建中断配置界面（保留用于兼容）"""
        for widget in self.config_scrollable_frame.winfo_children():
            widget.destroy()
        
        # 标题
        title_frame = ttk.Frame(self.config_scrollable_frame)
        title_frame.pack(fill=tk.X, pady=(5, 10))
        
        title = ttk.Label(title_frame, text="init.c - 中断寄存器配置", 
                         font=("Arial", 12, "bold"))
        title.pack(side=tk.LEFT)
        
        self._create_interrupt_config_content(self.config_scrollable_frame)
    
    def _update_int_enabled(self, int_name, var):
        """更新外部中断使能"""
        self.controller.config_data["interrupt"][int_name]["enabled"] = var.get()
    
    def _update_int_edge(self, int_name, value):
        """更新外部中断触发边沿"""
        self.controller.config_data["interrupt"][int_name]["edge"] = value
    
    def _update_port_change(self, port, var):
        """更新端口变化中断使能"""
        self.controller.config_data["interrupt"]["port_change"][port] = var.get()
    
    def _update_isr_config(self, key, value):
        """更新ISR配置"""
        self.controller.config_data["isr"][key] = value
    
    def _update_isr_int_var(self, key, var):
        """更新ISR整数配置"""
        try:
            value = var.get()
        except tk.TclError:
            return
        self.controller.config_data["isr"][key] = value
    
    def _update_sleep_config(self, key, value):
        """更新睡眠配置"""
        self.controller.config_data["sleep"][key] = value
    
    def _update_sleep_wake_port(self, port, enabled):
        wake_ports = set(self.controller.config_data["sleep"].get("wake_ports", ["P6"]))
        if enabled:
            wake_ports.add(port)
        else:
            wake_ports.discard(port)
        if not wake_ports:
            wake_ports.add(port)
        self.controller.config_data["sleep"]["wake_ports"] = list(wake_ports)
    
    def _create_interrupt_register_config_content(self, parent):
        """创建中断寄存器配置内容（用于标签页）"""
        info_label = ttk.Label(parent, 
                              text="配置 WDTCON, INTE0, INTE1, INTF0, INTF1",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        config = self.controller.get_config()["interrupt"]
        
        # WDTCON寄存器配置
        wdtcon_frame = ttk.LabelFrame(parent, text="WDTCON - 外部中断控制寄存器", padding="10")
        wdtcon_frame.pack(fill=tk.X, padx=10, pady=5)
        
        wdtcon_config = config["wdtcon"]
        
        # WDT使能
        wdt_enable_var = tk.BooleanVar(value=wdtcon_config["wdt_enabled"])
        ttk.Checkbutton(wdtcon_frame, text="WDT使能 (Bit7)", variable=wdt_enable_var,
                       command=lambda: self._update_wdtcon_wdt(wdt_enable_var)).pack(anchor=tk.W, pady=2)
        
        # INT0配置
        int0_frame = ttk.Frame(wdtcon_frame)
        int0_frame.pack(fill=tk.X, pady=2)
        int0_enable_var = tk.BooleanVar(value=wdtcon_config["int0_enabled"])
        ttk.Checkbutton(int0_frame, text="INT0使能 (P60, Bit6)", variable=int0_enable_var,
                       command=lambda: self._update_wdtcon_int0_enable(int0_enable_var)).pack(side=tk.LEFT, padx=5)
        int0_edge_var = tk.StringVar(value=wdtcon_config["int0_edge"])
        ttk.Label(int0_frame, text="触发边沿:").pack(side=tk.LEFT, padx=5)
        ttk.Combobox(int0_frame, textvariable=int0_edge_var, values=["rising", "falling"],
                    state="readonly", width=10).pack(side=tk.LEFT, padx=5)
        int0_edge_var.trace("w", lambda *args: self._update_wdtcon_int0_edge(int0_edge_var.get()))
        
        # INT1配置
        int1_frame = ttk.Frame(wdtcon_frame)
        int1_frame.pack(fill=tk.X, pady=2)
        int1_enable_var = tk.BooleanVar(value=wdtcon_config["int1_enabled"])
        ttk.Checkbutton(int1_frame, text="INT1使能 (P53, Bit5)", variable=int1_enable_var,
                       command=lambda: self._update_wdtcon_int1_enable(int1_enable_var)).pack(side=tk.LEFT, padx=5)
        int1_edge_var = tk.StringVar(value=wdtcon_config["int1_edge"])
        ttk.Label(int1_frame, text="触发边沿:").pack(side=tk.LEFT, padx=5)
        ttk.Combobox(int1_frame, textvariable=int1_edge_var, values=["rising", "falling"],
                    state="readonly", width=10).pack(side=tk.LEFT, padx=5)
        int1_edge_var.trace("w", lambda *args: self._update_wdtcon_int1_edge(int1_edge_var.get()))
        
        # 内部基准输出
        vfoe_var = tk.BooleanVar(value=wdtcon_config["vfoe"])
        ttk.Checkbutton(wdtcon_frame, text="内部基准输出使能 (Bit4)", variable=vfoe_var,
                       command=lambda: self._update_wdtcon_vfoe(vfoe_var)).pack(anchor=tk.W, pady=2)
        
        # INTE0寄存器配置
        inte0_frame = ttk.LabelFrame(parent, text="INTE0 - 中断使能控制寄存器0", padding="10")
        inte0_frame.pack(fill=tk.X, padx=10, pady=5)
        
        inte0_config = config["inte0"]
        
        ad_ie_var = tk.BooleanVar(value=inte0_config["ad_ie"])
        ttk.Checkbutton(inte0_frame, text="ADC中断使能 (Bit5)", variable=ad_ie_var,
                       command=lambda: self._update_inte0_ad_ie(ad_ie_var)).pack(anchor=tk.W, pady=2)
        
        ex1_ie_var = tk.BooleanVar(value=inte0_config["ex1_ie"])
        ttk.Checkbutton(inte0_frame, text="INT1中断使能 (Bit4)", variable=ex1_ie_var,
                       command=lambda: self._update_inte0_ex1_ie(ex1_ie_var)).pack(anchor=tk.W, pady=2)
        
        ex0_ie_var = tk.BooleanVar(value=inte0_config["ex0_ie"])
        ttk.Checkbutton(inte0_frame, text="INT0中断使能 (Bit3)", variable=ex0_ie_var,
                       command=lambda: self._update_inte0_ex0_ie(ex0_ie_var)).pack(anchor=tk.W, pady=2)
        
        p6ic_ie_var = tk.BooleanVar(value=inte0_config["p6ic_ie"])
        ttk.Checkbutton(inte0_frame, text="P6端口变化中断使能 (Bit2)", variable=p6ic_ie_var,
                       command=lambda: self._update_inte0_p6ic_ie(p6ic_ie_var)).pack(anchor=tk.W, pady=2)
        
        p5ic_ie_var = tk.BooleanVar(value=inte0_config["p5ic_ie"])
        ttk.Checkbutton(inte0_frame, text="P5端口变化中断使能 (Bit1)", variable=p5ic_ie_var,
                       command=lambda: self._update_inte0_p5ic_ie(p5ic_ie_var)).pack(anchor=tk.W, pady=2)
        
        tc0_ie_var = tk.BooleanVar(value=inte0_config["tc0_ie"])
        ttk.Checkbutton(inte0_frame, text="TC0中断使能 (Bit0)", variable=tc0_ie_var,
                       command=lambda: self._update_inte0_tc0_ie(tc0_ie_var)).pack(anchor=tk.W, pady=2)
        
        # INTE1寄存器配置
        inte1_frame = ttk.LabelFrame(parent, text="INTE1 - 中断使能控制寄存器1", padding="10")
        inte1_frame.pack(fill=tk.X, padx=10, pady=5)
        
        inte1_config = config["inte1"]
        
        dt4_ie_var = tk.BooleanVar(value=inte1_config["dt4_ie"])
        ttk.Checkbutton(inte1_frame, text="DT4中断使能 (Bit5)", variable=dt4_ie_var,
                       command=lambda: self._update_inte1_dt4_ie(dt4_ie_var)).pack(anchor=tk.W, pady=2)
        
        dt3_ie_var = tk.BooleanVar(value=inte1_config["dt3_ie"])
        ttk.Checkbutton(inte1_frame, text="DT3中断使能 (Bit4)", variable=dt3_ie_var,
                       command=lambda: self._update_inte1_dt3_ie(dt3_ie_var)).pack(anchor=tk.W, pady=2)
        
        dt2_ie_var = tk.BooleanVar(value=inte1_config["dt2_ie"])
        ttk.Checkbutton(inte1_frame, text="DT2中断使能 (Bit3)", variable=dt2_ie_var,
                       command=lambda: self._update_inte1_dt2_ie(dt2_ie_var)).pack(anchor=tk.W, pady=2)
        
        dt1_ie_var = tk.BooleanVar(value=inte1_config["dt1_ie"])
        ttk.Checkbutton(inte1_frame, text="DT1中断使能 (Bit2)", variable=dt1_ie_var,
                       command=lambda: self._update_inte1_dt1_ie(dt1_ie_var)).pack(anchor=tk.W, pady=2)
        
        tc2_ie_var = tk.BooleanVar(value=inte1_config["tc2_ie"])
        ttk.Checkbutton(inte1_frame, text="TC2中断使能 (Bit1)", variable=tc2_ie_var,
                       command=lambda: self._update_inte1_tc2_ie(tc2_ie_var)).pack(anchor=tk.W, pady=2)
        
        tc1_ie_var = tk.BooleanVar(value=inte1_config["tc1_ie"])
        ttk.Checkbutton(inte1_frame, text="TC1中断使能 (Bit0)", variable=tc1_ie_var,
                       command=lambda: self._update_inte1_tc1_ie(tc1_ie_var)).pack(anchor=tk.W, pady=2)
        
        # 存储控件引用
        if not hasattr(self, 'interrupt_register_widgets'):
            self.interrupt_register_widgets = {}
        self.interrupt_register_widgets['wdtcon'] = {
            'wdt_enabled': wdt_enable_var,
            'int0_enabled': int0_enable_var,
            'int0_edge': int0_edge_var,
            'int1_enabled': int1_enable_var,
            'int1_edge': int1_edge_var,
            'vfoe': vfoe_var
        }
    
    def _update_wdtcon_wdt(self, var):
        """更新WDTCON WDT使能"""
        self.controller.config_data["interrupt"]["wdtcon"]["wdt_enabled"] = var.get()
    
    def _update_wdtcon_int0_enable(self, var):
        """更新WDTCON INT0使能"""
        self.controller.config_data["interrupt"]["wdtcon"]["int0_enabled"] = var.get()
    
    def _update_wdtcon_int0_edge(self, value):
        """更新WDTCON INT0触发边沿"""
        self.controller.config_data["interrupt"]["wdtcon"]["int0_edge"] = value
    
    def _update_wdtcon_int1_enable(self, var):
        """更新WDTCON INT1使能"""
        self.controller.config_data["interrupt"]["wdtcon"]["int1_enabled"] = var.get()
    
    def _update_wdtcon_int1_edge(self, value):
        """更新WDTCON INT1触发边沿"""
        self.controller.config_data["interrupt"]["wdtcon"]["int1_edge"] = value
    
    def _update_wdtcon_vfoe(self, var):
        """更新WDTCON 内部基准输出使能"""
        self.controller.config_data["interrupt"]["wdtcon"]["vfoe"] = var.get()
    
    def _update_inte0_ad_ie(self, var):
        """更新INTE0 ADC中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["ad_ie"] = var.get()
    
    def _update_inte0_ex1_ie(self, var):
        """更新INTE0 INT1中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["ex1_ie"] = var.get()
    
    def _update_inte0_ex0_ie(self, var):
        """更新INTE0 INT0中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["ex0_ie"] = var.get()
    
    def _update_inte0_p6ic_ie(self, var):
        """更新INTE0 P6端口变化中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["p6ic_ie"] = var.get()
    
    def _update_inte0_p5ic_ie(self, var):
        """更新INTE0 P5端口变化中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["p5ic_ie"] = var.get()
    
    def _update_inte0_tc0_ie(self, var):
        """更新INTE0 TC0中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["tc0_ie"] = var.get()
    
    def _update_inte1_dt4_ie(self, var):
        """更新INTE1 DT4中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["dt4_ie"] = var.get()
    
    def _update_inte1_dt3_ie(self, var):
        """更新INTE1 DT3中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["dt3_ie"] = var.get()
    
    def _update_inte1_dt2_ie(self, var):
        """更新INTE1 DT2中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["dt2_ie"] = var.get()
    
    def _update_inte1_dt1_ie(self, var):
        """更新INTE1 DT1中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["dt1_ie"] = var.get()
    
    def _update_inte1_tc2_ie(self, var):
        """更新INTE1 TC2中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["tc2_ie"] = var.get()
    
    def _update_inte1_tc1_ie(self, var):
        """更新INTE1 TC1中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["tc1_ie"] = var.get()
    
    def _create_system_config_ui(self):
        """创建系统配置界面"""
        for widget in self.config_scrollable_frame.winfo_children():
            widget.destroy()
        
        ttk.Label(self.config_scrollable_frame, text="系统配置", font=("Arial", 12, "bold")).pack(pady=(5, 10))
        
        config = self.controller.get_config()["system"]
        
        # 时钟配置
        clock_frame = ttk.LabelFrame(self.config_scrollable_frame, text="时钟配置", padding="10")
        clock_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(clock_frame, text="时钟源:").pack(anchor=tk.W, pady=2)
        clk_source_var = tk.StringVar(value=config["clock"]["source"])
        ttk.Combobox(clock_frame, textvariable=clk_source_var, values=["IHRC", "ILRC"],
                    state="readonly", width=15).pack(anchor=tk.W, padx=20, pady=2)
        clk_source_var.trace("w", lambda *args: self._update_clock_source(clk_source_var.get()))
        
        ttk.Label(clock_frame, text="频率:").pack(anchor=tk.W, pady=2)
        freq_var = tk.StringVar(value=config["clock"]["frequency"])
        ttk.Combobox(clock_frame, textvariable=freq_var,
                    values=["8MHz", "6MHz", "5.4MHz", "4.8MHz", "3.4MHz", "1MHz"],
                    state="readonly", width=15).pack(anchor=tk.W, padx=20, pady=2)
        freq_var.trace("w", lambda *args: self._update_clock_frequency(freq_var.get()))
        
        ttk.Label(clock_frame, text="分频:").pack(anchor=tk.W, pady=2)
        div_var = tk.IntVar(value=config["clock"]["divider"])
        ttk.Spinbox(clock_frame, from_=1, to=16, textvariable=div_var, width=10,
                   command=lambda: self._update_clock_divider(div_var.get())).pack(anchor=tk.W, padx=20, pady=2)
        
        # 看门狗配置
        wdt_frame = ttk.LabelFrame(self.config_scrollable_frame, text="看门狗配置", padding="10")
        wdt_frame.pack(fill=tk.X, padx=10, pady=5)
        
        wdt_enable_var = tk.BooleanVar(value=config["wdt"]["enabled"])
        ttk.Checkbutton(wdt_frame, text="使能看门狗", variable=wdt_enable_var,
                       command=lambda: self._update_wdt_enabled(wdt_enable_var)).pack(anchor=tk.W, pady=2)
        
        ttk.Label(wdt_frame, text="超时时间:").pack(anchor=tk.W, pady=2)
        wdt_timeout_var = tk.IntVar(value=config["wdt"]["timeout"])
        ttk.Spinbox(wdt_frame, from_=0, to=65535, textvariable=wdt_timeout_var, width=10,
                   command=lambda: self._update_wdt_timeout(wdt_timeout_var.get())).pack(anchor=tk.W, padx=20, pady=2)
        
        # LVR配置
        lvr_frame = ttk.LabelFrame(self.config_scrollable_frame, text="低电压复位(LVR)配置", padding="10")
        lvr_frame.pack(fill=tk.X, padx=10, pady=5)
        
        lvr_enable_var = tk.BooleanVar(value=config["lvr"]["enabled"])
        ttk.Checkbutton(lvr_frame, text="使能LVR", variable=lvr_enable_var,
                       command=lambda: self._update_lvr_enabled(lvr_enable_var)).pack(anchor=tk.W, pady=2)
        
        ttk.Label(lvr_frame, text="阈值:").pack(anchor=tk.W, pady=2)
        lvr_threshold_var = tk.StringVar(value=config["lvr"]["threshold"])
        ttk.Combobox(lvr_frame, textvariable=lvr_threshold_var,
                    values=["2.4V", "1.8V", "1.6V", "1.2V"],
                    state="readonly", width=15).pack(anchor=tk.W, padx=20, pady=2)
        lvr_threshold_var.trace("w", lambda *args: self._update_lvr_threshold(lvr_threshold_var.get()))
    
    def _update_clock_source(self, value):
        """更新时钟源"""
        self.controller.config_data["system"]["clock"]["source"] = value
    
    def _update_clock_frequency(self, value):
        """更新时钟频率"""
        self.controller.config_data["system"]["clock"]["frequency"] = value
    
    def _update_clock_divider(self, value):
        """更新时钟分频"""
        self.controller.config_data["system"]["clock"]["divider"] = value
    
    def _update_wdt_enabled(self, var):
        """更新看门狗使能"""
        self.controller.config_data["system"]["wdt"]["enabled"] = var.get()
    
    def _update_wdt_timeout(self, value):
        """更新看门狗超时时间"""
        self.controller.config_data["system"]["wdt"]["timeout"] = value
    
    def _update_lvr_enabled(self, var):
        """更新LVR使能"""
        self.controller.config_data["system"]["lvr"]["enabled"] = var.get()
    
    def _update_lvr_threshold(self, value):
        """更新LVR阈值"""
        self.controller.config_data["system"]["lvr"]["threshold"] = value
    
    def _refresh_ui(self):
        """刷新UI显示"""
        # TODO: 根据配置数据更新UI
        pass
    
    def _new_config(self):
        """新建配置"""
        if messagebox.askyesno("确认", "是否创建新配置？当前配置将丢失。"):
            # 重置为默认配置
            self.controller.config_data = self.controller._init_default_config()
            self._refresh_ui()
            self.status_label.config(text="已创建新配置")
    
    def _open_config(self):
        """打开配置"""
        filepath = filedialog.askopenfilename(
            title="打开配置",
            filetypes=[("JSON文件", "*.json"), ("所有文件", "*.*")]
        )
        if filepath:
            if self.controller.load_config(filepath):
                self._refresh_ui()
                self.status_label.config(text=f"已加载配置: {filepath}")
            else:
                messagebox.showerror("错误", "加载配置失败")
    
    def _save_config(self):
        """保存配置"""
        filepath = filedialog.asksaveasfilename(
            title="保存配置",
            defaultextension=".json",
            filetypes=[("JSON文件", "*.json"), ("所有文件", "*.*")]
        )
        if filepath:
            if self.controller.save_config(filepath):
                self.status_label.config(text=f"配置已保存: {filepath}")
            else:
                messagebox.showerror("错误", "保存配置失败")
    
    def _reset_config(self):
        """重置配置"""
        if messagebox.askyesno("确认", "是否重置为默认配置？"):
            self.controller.config_data = self.controller._init_default_config()
            self._refresh_ui()
            self.status_label.config(text="已重置为默认配置")
    
    def _generate_init_code(self):
        """生成初始化代码"""
        code = self.controller.generate_init_code()
        self.code_editor.text_widget.delete(1.0, tk.END)
        self.code_editor.insert(1.0, code)
        # 生成后自动滚动到顶部
        self.code_editor.text_widget.see(1.0)
        self.code_editor.text_widget.mark_set(tk.INSERT, 1.0)
        self.status_label.config(text="初始化代码已生成")
    
    def _generate_main_code(self):
        """生成主程序代码"""
        code = self.controller.generate_main_code()
        self.code_editor.text_widget.delete(1.0, tk.END)
        self.code_editor.insert(1.0, code)
        # 生成后自动滚动到顶部
        self.code_editor.text_widget.see(1.0)
        self.code_editor.text_widget.mark_set(tk.INSERT, 1.0)
        self.status_label.config(text="主程序代码已生成")
    
    def _generate_all_code(self):
        """生成所有代码"""
        # 生成所有文件
        files = self.controller.generate_all_files()
        
        # 保存生成的文件
        self.generated_files = files
        
        # 显示文件列表，让用户选择查看哪个文件
        if not hasattr(self, 'file_list_frame'):
            self._create_file_list_panel()
        
        # 更新文件列表
        self._update_file_list(list(files.keys()))
        
        # 默认显示init.c
        if "init.c" in files:
            self._show_file_content("init.c", files["init.c"])
        elif files:
            # 如果没有init.c，显示第一个文件
            first_file = list(files.keys())[0]
            self._show_file_content(first_file, files[first_file])
        
        self.status_label.config(text=f"已生成 {len(files)} 个文件", foreground="#008000")
    
    def _create_file_list_panel(self):
        """创建文件列表面板"""
        # 找到代码预览框架
        # 在代码预览区域上方添加文件列表
        # 需要找到right_frame，它在_create_main_ui中创建
        # 我们通过查找包含代码编辑器的框架来定位
        if hasattr(self, 'code_editor'):
            # 找到代码编辑器的父框架（right_frame）
            parent = self.code_editor.master
            if parent:
                # 创建文件列表框架
                file_list_frame = ttk.LabelFrame(parent, text="生成的文件", padding="5")
                file_list_frame.pack(fill=tk.X, pady=(0, 5), before=self.code_editor)
                
                # 文件列表
                listbox_frame = ttk.Frame(file_list_frame)
                listbox_frame.pack(fill=tk.BOTH, expand=True)
                
                scrollbar = ttk.Scrollbar(listbox_frame)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                
                self.file_listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set, height=4)
                self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                scrollbar.config(command=self.file_listbox.yview)
                
                self.file_listbox.bind('<<ListboxSelect>>', self._on_file_select)
                
                self.file_list_frame = file_list_frame
                self.generated_files = {}
    
    def _update_file_list(self, file_names):
        """更新文件列表"""
        if hasattr(self, 'file_listbox'):
            self.file_listbox.delete(0, tk.END)
            for name in sorted(file_names):
                self.file_listbox.insert(tk.END, name)
    
    def _on_file_select(self, event):
        """文件选择事件"""
        selection = self.file_listbox.curselection()
        if selection:
            file_name = self.file_listbox.get(selection[0])
            if hasattr(self, 'generated_files') and file_name in self.generated_files:
                self._show_file_content(file_name, self.generated_files[file_name])
    
    def _show_file_content(self, file_name, content):
        """显示文件内容"""
        self.code_editor.text_widget.delete(1.0, tk.END)
        self.code_editor.insert(1.0, content)
        self.code_editor.text_widget.see(1.0)
        self.code_editor.text_widget.mark_set(tk.INSERT, 1.0)
        
        # 更新状态栏显示当前文件
        self.status_label.config(text=f"当前文件: {file_name}")
    
    def _show_about(self):
        """显示关于对话框"""
        about_text = """JZ8P2615 代码生成工具 v1.0

类似 STM32 CubeMX 的配置工具
用于 JZ8P2615 芯片的模块配置和代码生成

功能：
- GPIO端口配置
- ADC模数转换配置
- 定时器配置
- PWM脉宽调制配置
- 中断配置
- 系统配置

开发中...
"""
        messagebox.showinfo("关于", about_text)
    
    def run(self):
        """运行UI主循环"""
        self.root.mainloop()

