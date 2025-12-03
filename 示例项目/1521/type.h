#ifndef _TYPE_H_
#define _TYPE_H_

#include "jz8p1521.h"

//************************************/
//-----------指令定义---------------- 
//************************************/

#define EI()  __asm__(" ei ")
#define DI()  __asm__(" di ")
#define NOP() __asm__(" nop ")
#define CWDT() __asm__(" CWDT ")
#define SLEEP() __asm__(" sleep ")
/************************************/
//-----------寄存器读写示例----------  
/************************************/
#define CONTW(VAL)			__asm__("mov a,@"#VAL"\n ctw")			//CTW = VAL：CONT寄存器赋值
#define IOCP_W(REG,VAL)		__asm__("mov a,@"#VAL"\n iw "#REG)		//REG = VAL：IOC页寄存器赋值
#define IOCP_R(RAM,REG)		__asm__("ir "#REG"\n mov "#RAM",a")		//RAM = REG：IOC页寄存器读值
#define PUSH(A_REG,R3_REG)	__asm__("mov "#A_REG",a\n swap "#A_REG"\n swapa STATUS\n mov "#R3_REG",a")	//中断入栈保护	
#define POP(A_REG,R3_REG)	__asm__("swapa "#R3_REG"\n mov STATUS,a\n swapa "#A_REG)


#define IOCP_W_AND(REG,VAL) __asm__("ir "#REG"\n and a,@"#VAL"\n iw "#REG)  // & 与
#define IOCP_W_OR(REG,VAL)  __asm__("ir "#REG"\n or a,@"#VAL"\n iw "#REG)   // | 或

//************************************/
//-----------  重定义 ---------------- 
//************************************/
typedef   unsigned char		uint8_t;
typedef   unsigned int 		uint16_t;

#define   ENABLE    1
#define   DISABLE   0

#endif