#include "main.h"
#include "type.h"
#include "smg.h"
unsigned char reg_200us;  
unsigned char reg_10ms;

volatile unsigned char __at(0x00) A_Buff;
volatile unsigned char __at(0x01) S_Buff;
void int_isr(void) __interrupt 
{    	
	__asm__("org 0x08");			//中断入口地址	
    di();		
	push(A_Buff, S_Buff);			//中断入栈保护
//=========Tcc中断程序===============//
	if(TC0IF == 1)					//判断TCIF是否为1
	{
        
		TC0C  += TCC_NUM;		
		TC0IF = 0;		
		
		if(++reg_10ms >= 200)
		{
			reg_10ms  = 0;
			Time_10ms = 1;
		
		}
		if(++reg_200us >= 4)
		{
			reg_200us  = 0;
			Time_200us = 1;
		}
		if(r_g_workMod == 1 || F_CHARGE == 1)
		{
			SMG_Scan();
		}
		
	
	}	 
	INTF0=0x01;						//清除不用的标志位
	INTF1=0x00;
	pop(A_Buff, S_Buff);			//中断出栈保护恢复
    ei();
	ret();

}