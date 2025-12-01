#include "init.h"
#include "type.h"
#include "main.h"
#include "JZ8P2615.h"

void file_clrRam(void)
{
	for(RSR=0x90;RSR<0xFF;RSR++)	//清零 BANK0 RAM  IAR-R0,RSR-R4
	{IAR = 0;}
	 IAR = 0;
}
//===================================//
//端口初始化
//===================================//
void file_init(void)
{
//===========端口初始化=============
	PORT5=0x00;
	PORT6=0x00;
	
	P5CON=0x00;			//P5端口控制	;0输出，1输入
	P6CON=0x38;			//P6端口控制    ;0输出，1输入
	
	P5PH=0xFF;			//P5口上拉		;0使能，1禁止
	P6PH=0xC7;			//P6口上拉		;0使能，1禁止

	P5PD=0xff;			//P5口下拉		;0使能，1禁止
	P6PD=0xff;			//P6口下拉		;0使能，1禁止	

	P6OD=0x00;			//P6口开漏		;0禁止，1使能
	P6WD=0x00;			//P6口弱驱动   ;0禁止，1使能	

	//-----端口变化中断唤醒------
	P5IWE=0X00;			//P5口状态变化唤醒使能
	P6IWE=0X38;			//P6口状态变化唤醒使能

	// -----使能外部中断设置------	
	WDTCON=0x00;		//bit6&5:P60&P53外部中断功能控制位，0:普通IO口, 1:外部中断口
	
	INTE0=0x01;			//中断使能 21
	INTE1=0x00;			//周期及占空比中断
	INTF0=0x00;			//清中断标志位
	INTF1=0x00;		
}
void file_tc0_Init(void)
{
	//===========TC0初始化==============
	TC0CON = 0x82;	//TC0控制寄存器			0分频	
	TC0C = TCC_NUM;		//TC0计数寄存器
	INTE0 |= 0x01;			//中断使能 21
}